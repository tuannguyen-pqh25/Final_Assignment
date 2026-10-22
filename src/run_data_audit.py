import sys
from pathlib import Path
import json
import pandas as pd
import numpy as np

def run_audit():
    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir / "data" / "raw"
    if not data_dir.exists():
        data_dir = base_dir / "telecom"
    
    reports_dir = base_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Loading data from: {data_dir}")
    client_path = data_dir / "Client.csv"
    record_path = data_dir / "Record.csv"
    
    df_client = pd.read_csv(client_path)
    df_record = pd.read_csv(record_path)
    
    print(f"Client shape: {df_client.shape}")
    print(f"Record shape: {df_record.shape}")
    
    # 1. Customer_ID & Duplicate Audit
    client_id_col = "Customer_ID"
    record_id_col = "Customer_ID"
    
    client_ids = df_client[client_id_col]
    record_ids = df_record[record_id_col]
    
    client_id_nulls = int(client_ids.isna().sum())
    record_id_nulls = int(record_ids.isna().sum())
    
    client_id_dups = int(client_ids.duplicated().sum())
    record_id_dups = int(record_ids.duplicated().sum())
    
    client_id_set = set(client_ids.dropna().unique())
    record_id_set = set(record_ids.dropna().unique())
    
    in_both = len(client_id_set.intersection(record_id_set))
    in_client_only = len(client_id_set - record_id_set)
    in_record_only = len(record_id_set - client_id_set)
    
    client_row_dups = int(df_client.duplicated().sum())
    record_row_dups = int(df_record.duplicated().sum())
    
    # 2. Overlapping columns (excluding Customer_ID)
    common_cols = sorted(list(set(df_client.columns).intersection(set(df_record.columns)) - {client_id_col}))
    
    # 3. Join Verification
    df_merged_inner = pd.merge(df_client, df_record, on="Customer_ID", how="inner")
    df_merged_left = pd.merge(df_client, df_record, on="Customer_ID", how="left")
    df_merged_outer = pd.merge(df_client, df_record, on="Customer_ID", how="outer")
    
    merged_inner_shape = df_merged_inner.shape
    merged_left_shape = df_merged_left.shape
    merged_outer_shape = df_merged_outer.shape
    
    # 4. Target variable 'churn' audit
    target_found_in = []
    if "churn" in df_client.columns:
        target_found_in.append("Client.csv")
    if "churn" in df_record.columns:
        target_found_in.append("Record.csv")
        
    target_series = df_merged_inner["churn"] if "churn" in df_merged_inner.columns else None
    target_nulls = int(target_series.isna().sum()) if target_series is not None else -1
    target_counts = target_series.value_counts(dropna=False).to_dict() if target_series is not None else {}
    target_dist = {str(k): int(v) for k, v in target_counts.items()}
    
    # 5. Column-by-column detailed audit
    audit_rows = []
    
    sentinel_strings = {"nan", "null", "none", "?", "na", "", "unknown", " "}
    
    for table_name, df in [("Client", df_client), ("Record", df_record)]:
        n_rows = len(df)
        for col in df.columns:
            s = df[col]
            dtype_str = str(s.dtype)
            null_count = int(s.isna().sum())
            null_pct = round(null_count / n_rows * 100, 4)
            n_unique = int(s.nunique(dropna=True))
            
            # String sentinel check
            has_str_nan = False
            if s.dtype == object or s.dtype == "string":
                str_lower = s.dropna().astype(str).str.strip().str.lower()
                matches = str_lower.isin(sentinel_strings)
                if matches.sum() > 0:
                    has_str_nan = True
            
            # Numeric range check
            is_numeric = pd.api.types.is_numeric_dtype(s)
            neg_count = 0
            min_val = None
            max_val = None
            if is_numeric:
                non_nulls = s.dropna()
                if len(non_nulls) > 0:
                    neg_count = int((non_nulls < 0).sum())
                    min_val = round(float(non_nulls.min()), 4)
                    max_val = round(float(non_nulls.max()), 4)
            else:
                non_nulls = s.dropna()
                if len(non_nulls) > 0:
                    min_val = str(non_nulls.min())[:30]
                    max_val = str(non_nulls.max())[:30]
            
            # Quality notes & proposed handling
            notes = []
            proposed = "Keep as feature"
            
            if col == "Customer_ID":
                notes.append("Identifier key")
                proposed = "Drop from modeling features; use only for join & QA"
            elif col == "churn":
                notes.append(f"Target variable; distribution: {target_dist}")
                proposed = "Target variable (Y)"
            elif null_pct > 50.0:
                notes.append(f"High missingness ({null_pct}%)")
                proposed = "Assess imputation with missing indicator vs drop; evaluate in ablation"
            elif null_pct > 30.0:
                notes.append(f"Moderate missingness ({null_pct}%)")
                proposed = "Impute (median/mode) + missing indicator flag"
            elif null_pct > 0.0:
                notes.append(f"Low missingness ({null_pct}%)")
                proposed = "Standard median/mode imputation within training pipeline"
            
            if n_unique <= 1:
                notes.append("Zero variance / constant column")
                proposed = "Drop (no predictive variance)"
            
            if neg_count > 0:
                notes.append(f"Contains {neg_count} negative values")
                if "rev" in col or "mou" in col or "change" in col or "adj" in col:
                    notes.append("Negative revenue/mou/change may represent billing adjustments or delta")
            
            if has_str_nan:
                notes.append("Contains string sentinels resembling NaN")
            
            audit_rows.append({
                "table": table_name,
                "column_name": col,
                "dtype": dtype_str,
                "null_count": null_count,
                "null_pct": null_pct,
                "unique_count": n_unique,
                "min_val": min_val,
                "max_val": max_val,
                "negative_count": neg_count,
                "has_string_nan": has_str_nan,
                "notes": "; ".join(notes) if notes else "Clean",
                "proposed_handling": proposed
            })
            
    df_audit = pd.DataFrame(audit_rows)
    audit_csv_path = reports_dir / "data_audit.csv"
    df_audit.to_csv(audit_csv_path, index=False)
    print(f"Saved detailed audit to: {audit_csv_path}")
    
    # Summary dictionary
    summary = {
        "client_shape": list(df_client.shape),
        "record_shape": list(df_record.shape),
        "client_id_nulls": client_id_nulls,
        "record_id_nulls": record_id_nulls,
        "client_id_duplicates": client_id_dups,
        "record_id_duplicates": record_id_dups,
        "client_unique_ids": len(client_id_set),
        "record_unique_ids": len(record_id_set),
        "ids_in_both": in_both,
        "ids_in_client_only": in_client_only,
        "ids_in_record_only": in_record_only,
        "client_row_duplicates": client_row_dups,
        "record_row_duplicates": record_row_dups,
        "common_columns_excluding_id": common_cols,
        "merged_inner_shape": list(merged_inner_shape),
        "merged_left_shape": list(merged_left_shape),
        "merged_outer_shape": list(merged_outer_shape),
        "target_variable": "churn",
        "target_found_in": target_found_in,
        "target_nulls": target_nulls,
        "target_distribution": target_dist,
        "target_percentages": {k: round(v / len(df_merged_inner) * 100, 4) for k, v in target_dist.items()},
        "total_columns_audited": len(df_audit),
        "columns_with_missing": int((df_audit["null_count"] > 0).sum()),
        "columns_missing_gt_30pct": df_audit[df_audit["null_pct"] > 30]["column_name"].tolist(),
        "columns_negative_vals": df_audit[df_audit["negative_count"] > 0]["column_name"].tolist(),
        "zero_variance_columns": df_audit[df_audit["unique_count"] <= 1]["column_name"].tolist()
    }
    
    summary_json_path = reports_dir / "data_audit_summary.json"
    with open(summary_json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"Saved summary to: {summary_json_path}")
    
    print("\n=== AUDIT SUMMARY ===")
    print(f"Client: {summary['client_shape']}, Record: {summary['record_shape']}")
    print(f"Inner Join Shape: {summary['merged_inner_shape']}")
    print(f"Target distribution: {summary['target_distribution']} ({summary['target_percentages']}%)")
    print(f"Columns with >30% missing: {summary['columns_missing_gt_30pct']}")
    print(f"Zero variance columns: {summary['zero_variance_columns']}")
    print(f"Columns with negatives: {summary['columns_negative_vals']}")

if __name__ == "__main__":
    run_audit()
