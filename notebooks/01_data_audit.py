# %% [markdown]
# # GCI World 2026 Final Assignment — Stage 1: Data Audit & Key Join Verification
# **Objective:** Systematically audit raw dataset quality for `Client.csv` and `Record.csv`, verify the join key `Customer_ID`, validate target variable `churn` balance, identify missingness profiles, and document domain anomalies for reproducible data science modeling.

# %%
from pathlib import Path
import json
import pandas as pd
import numpy as np

# Reproducibility settings
SEED = 42
pd.set_option("display.max_columns", 120)
pd.set_option("display.max_rows", 150)

# Robust relative path handling (works in both local IDE and Google Colab)
BASE_DIR = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
DATA_DIR = BASE_DIR / "data" / "raw"
if not DATA_DIR.exists():
    DATA_DIR = BASE_DIR / "telecom"
REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

print(f"Project Base Directory: {BASE_DIR}")
print(f"Data Directory: {DATA_DIR}")

# %% [markdown]
# ## 1. Load Raw Source Tables

# %%
client_path = DATA_DIR / "Client.csv"
record_path = DATA_DIR / "Record.csv"

df_client = pd.read_csv(client_path)
df_record = pd.read_csv(record_path)

print(f"Client.csv shape: {df_client.shape[0]:,} rows x {df_client.shape[1]} columns")
print(f"Record.csv shape: {df_record.shape[0]:,} rows x {df_record.shape[1]} columns")

# %% [markdown]
# ## 2. Customer_ID Integrity & Exact Row Duplicates Audit

# %%
print("=== CUSTOMER_ID AUDIT ===")
client_null_ids = df_client["Customer_ID"].isna().sum()
record_null_ids = df_record["Customer_ID"].isna().sum()

client_dup_ids = df_client["Customer_ID"].duplicated().sum()
record_dup_ids = df_record["Customer_ID"].duplicated().sum()

client_unique_ids = df_client["Customer_ID"].nunique()
record_unique_ids = df_record["Customer_ID"].nunique()

print(f"Client.csv - Missing Customer_ID: {client_null_ids:,} | Duplicate IDs: {client_dup_ids:,} | Unique IDs: {client_unique_ids:,}")
print(f"Record.csv - Missing Customer_ID: {record_null_ids:,} | Duplicate IDs: {record_dup_ids:,} | Unique IDs: {record_unique_ids:,}")

client_row_dups = df_client.duplicated().sum()
record_row_dups = df_record.duplicated().sum()
print(f"Client.csv exact row duplicates: {client_row_dups}")
print(f"Record.csv exact row duplicates: {record_row_dups}")

# %% [markdown]
# ## 3. Set Differences & Join Verification (Inner vs Left vs Outer)

# %%
set_client = set(df_client["Customer_ID"])
set_record = set(df_record["Customer_ID"])

in_both = len(set_client.intersection(set_record))
in_client_only = len(set_client - set_record)
in_record_only = len(set_record - set_client)

print(f"Customer_IDs present in BOTH tables: {in_both:,}")
print(f"Customer_IDs ONLY in Client.csv: {in_client_only:,}")
print(f"Customer_IDs ONLY in Record.csv: {in_record_only:,}")

df_inner = pd.merge(df_client, df_record, on="Customer_ID", how="inner")
df_left = pd.merge(df_client, df_record, on="Customer_ID", how="left")
df_outer = pd.merge(df_client, df_record, on="Customer_ID", how="outer")

print(f"Inner Join shape: {df_inner.shape}")
print(f"Left Join shape:  {df_left.shape}")
print(f"Outer Join shape: {df_outer.shape}")

assert df_inner.shape == (100000, 100), "Inner join shape mismatch!"
assert in_client_only == 0 and in_record_only == 0, "Orphan IDs detected between tables!"
print("VERIFICATION CONFIRMED: 100,000 unique records match 1:1 with zero orphans.")

# %% [markdown]
# ## 4. Target Variable 'churn' Distribution

# %%
print("=== TARGET VARIABLE 'churn' AUDIT ===")
print("churn column found in:", [name for name, df in [("Client.csv", df_client), ("Record.csv", df_record)] if "churn" in df.columns])

churn_series = df_inner["churn"]
churn_nulls = churn_series.isna().sum()
churn_counts = churn_series.value_counts(dropna=False)
churn_pct = churn_series.value_counts(normalize=True, dropna=False) * 100

print(f"Missing values in 'churn': {churn_nulls}")
print("\nTarget Class Distribution:")
df_target_summary = pd.DataFrame({
    "Count": churn_counts,
    "Percentage (%)": churn_pct.round(4)
})
print(df_target_summary)

# %% [markdown]
# ## 5. Missingness Profile Across All Attributes

# %%
missing_summary = []
for name, df in [("Client", df_client), ("Record", df_record)]:
    null_counts = df.isna().sum()
    null_pcts = (null_counts / len(df)) * 100
    for col in df.columns:
        if null_counts[col] > 0:
            missing_summary.append({
                "Table": name,
                "Column": col,
                "Dtype": str(df[col].dtype),
                "Missing_Count": int(null_counts[col]),
                "Missing_Pct": round(float(null_pcts[col]), 4)
            })

df_missing = pd.DataFrame(missing_summary).sort_values(by="Missing_Pct", ascending=False).reset_index(drop=True)
print(f"Total attributes with missing values: {len(df_missing)} (out of 101 columns across both tables)")
print("\nTop 15 Features by Missingness Ratio:")
print(df_missing.head(15))

# %% [markdown]
# ## 6. Domain Range & Negative Value Anomalies

# %%
neg_summary = []
for name, df in [("Client", df_client), ("Record", df_record)]:
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        neg_count = (df[col] < 0).sum()
        if neg_count > 0:
            neg_summary.append({
                "Table": name,
                "Column": col,
                "Negative_Count": int(neg_count),
                "Min_Val": round(float(df[col].min()), 4),
                "Max_Val": round(float(df[col].max()), 4),
                "Negative_Pct": round(float(neg_count / len(df) * 100), 4)
            })

df_neg = pd.DataFrame(neg_summary).sort_values(by="Negative_Count", ascending=False).reset_index(drop=True)
print("=== FEATURES WITH NEGATIVE VALUES ===")
print(df_neg)

# %% [markdown]
# ## 7. Categorical Features & String Sentinels Audit

# %%
sentinel_check = []
cat_cols = df_client.select_dtypes(include=["object"]).columns
for col in cat_cols:
    val_counts = df_client[col].value_counts(dropna=False).head(5).to_dict()
    sentinel_check.append({
        "Column": col,
        "Unique_Values_Count": df_client[col].nunique(dropna=True),
        "Top_Values": str(val_counts)
    })

df_cat = pd.DataFrame(sentinel_check)
print("=== CATEGORICAL ATTRIBUTES AUDIT (Client.csv) ===")
print(df_cat.head(10))

# %% [markdown]
# ## 8. Export Detailed Audit Reports

# %%
from src.run_data_audit import run_audit
run_audit()
print("Execution Complete: Detailed audit exported to reports/data_audit.csv and reports/data_audit_summary.json")
