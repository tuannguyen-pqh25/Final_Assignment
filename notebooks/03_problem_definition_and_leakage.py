# %% [markdown]
# # GCI World 2026 Final Assignment — Stage 4: Problem Definition & Data Leakage Review
# **Dataset:** Company A (100,000 customers x 100 features)  
# **Objective:** Audit 98 modeling candidate predictors for target proxy or future data leakage, confirm zero-variance features, and configure the business metric hierarchy.

# %%
from pathlib import Path
import pandas as pd
import numpy as np

# Reproducibility settings
SEED = 42
pd.set_option("display.max_columns", 120)
pd.set_option("display.max_rows", 100)

BASE_DIR = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
DATA_DIR = BASE_DIR / "data" / "raw"
if not DATA_DIR.exists():
    DATA_DIR = BASE_DIR / "telecom"
REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

print(f"Base Directory: {BASE_DIR}")
print(f"Data Directory: {DATA_DIR}")

# %% [markdown]
# ## 1. Load Merged Audited Dataset

# %%
df_client = pd.read_csv(DATA_DIR / "Client.csv")
df_record = pd.read_csv(DATA_DIR / "Record.csv")
df = pd.merge(df_client, df_record, on="Customer_ID", how="inner")

print(f"Merged Dataset Shape: {df.shape[0]:,} rows x {df.shape[1]} columns")

# %% [markdown]
# ## 2. Feature Space Composition & Identifier Isolation
# Confirming that Customer_ID is excluded from modeling features and target variable is isolated.

# %%
target_col = "churn"
id_col = "Customer_ID"

modeling_features = [col for col in df.columns if col not in [id_col, target_col]]
cat_features = df[modeling_features].select_dtypes(include=["object"]).columns.tolist()
num_features = [c for c in modeling_features if c not in cat_features]

print(f"Total Columns in Dataset:  {len(df.columns)}")
print(f"Target Column:             '{target_col}' (Distribution: {df[target_col].mean()*100:.2f}% Churned)")
print(f"Identifier (Excluded):     '{id_col}' (Uniqueness: {df[id_col].nunique():,} unique IDs)")
print(f"Modeling Predictors:       {len(modeling_features)} features ({len(num_features)} Numerical, {len(cat_features)} Categorical)")

assert len(modeling_features) == 98, f"Expected exactly 98 predictors, found {len(modeling_features)}"
assert id_col not in modeling_features, "Data leakage critical: Customer_ID found in predictor list!"
print("Assertion Passed: Feature space contains exactly 98 predictors with zero ID leakage.")

# %% [markdown]
# ## 3. Data Leakage & Feature Sanity Audit
# Auditing linear correlation ceiling with target churn and checking for zero-variance constant features.

# %%
numeric_leakage = df[num_features].corrwith(df[target_col]).abs().sort_values(ascending=False)

print("Top 10 Numerical Features by Absolute Correlation with Churn:")
print(numeric_leakage.head(10))

max_linear_corr = numeric_leakage.max()
max_corr_feature = numeric_leakage.idxmax()
print(f"\nMax Correlation: {max_corr_feature} = {max_linear_corr:.4f}")

# Threshold for suspecting proxy leakage is |r| >= 0.20
assert max_linear_corr < 0.20, f"Potential proxy data leakage detected in feature '{max_corr_feature}'!"
print("Leakage Gate Passed: No single feature exhibits deterministic or proxy leakage with target churn.")

# Constant feature verification
constant_features = [col for col in modeling_features if df[col].nunique() <= 1]
print(f"Zero-variance (constant) features count: {len(constant_features)}")
assert len(constant_features) == 0, f"Constant features detected: {constant_features}"
print("Sanity Gate Passed: Zero constant features found across 100,000 subscriber records.")

# %% [markdown]
# ## 4. Business Metric Hierarchy Configuration (DEC-015)
# 1. Primary Ranking Metric:     ROC-AUC (Global threshold-independent discrimination)
# 2. Operational Efficiency:    PR-AUC & Precision @ Top 20% (Lift @ Quintile 1)
# 3. Financial ROI Metric:       Net Expected Retained Profit (Cost-Benefit Matrix)
# 4. Diagnostic Metrics:         Accuracy, Recall, F1-Score at business-optimal threshold tau*

# %%
print("Stage 4 Completed: Problem Definition & Data Leakage Review PASSED.")
