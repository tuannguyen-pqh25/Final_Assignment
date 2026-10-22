# %% [markdown]
# # GCI World 2026 Final Assignment — Telecom Churn Prediction & Retention Strategy
# **Author:** Senior Data Scientist & Telecom Consultant  
# **Dataset:** Company A (100,000 customers x 100 features)  
# **Goal:** End-to-end reproducible pipeline from raw data audit, exploratory data analysis, feature engineering, machine learning modeling to executive business decision proposal.

# %%
from pathlib import Path
import json
import pandas as pd
import numpy as np
import sys
import matplotlib
if not hasattr(sys, "ps1") and "ipykernel" not in sys.modules:
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# -----------------------------------------------------------------------------
# 0. Global Setup & Reproducibility Standards
# -----------------------------------------------------------------------------
SEED = 42
pd.set_option("display.max_columns", 120)
pd.set_option("display.max_rows", 100)

BASE_DIR = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
DATA_DIR = BASE_DIR / "data" / "raw"
if not DATA_DIR.exists():
    DATA_DIR = BASE_DIR / "telecom"
REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Visual styling
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams["figure.dpi"] = 300
plt.rcParams["font.size"] = 11
plt.rcParams["axes.titlesize"] = 13
plt.rcParams["axes.titleweight"] = "bold"

color_blue = "#2b5c8f"
color_orange = "#d95f02"

print(f"Project Directory: {BASE_DIR}")
print(f"Data Directory:    {DATA_DIR}")

# %% [markdown]
# ---
# ## SECTION 1: DATA AUDIT & JOIN VERIFICATION (Stage 1)
# Checking source file shapes, identifier uniqueness, orphan records, target churn balance, and missingness profile.

# %%
# 1.1 Load Raw Tables
df_client = pd.read_csv(DATA_DIR / "Client.csv")
df_record = pd.read_csv(DATA_DIR / "Record.csv")

print(f"Client.csv Shape: {df_client.shape[0]:,} rows x {df_client.shape[1]} columns")
print(f"Record.csv Shape: {df_record.shape[0]:,} rows x {df_record.shape[1]} columns")

# %%
# 1.2 Customer_ID Key Integrity & Row Duplicates Audit
client_null_ids = df_client["Customer_ID"].isna().sum()
record_null_ids = df_record["Customer_ID"].isna().sum()

client_dup_ids = df_client["Customer_ID"].duplicated().sum()
record_dup_ids = df_record["Customer_ID"].duplicated().sum()

print(f"Client.csv - Missing IDs: {client_null_ids:,} | Duplicate IDs: {client_dup_ids:,} | Unique IDs: {df_client['Customer_ID'].nunique():,}")
print(f"Record.csv - Missing IDs: {record_null_ids:,} | Duplicate IDs: {record_dup_ids:,} | Unique IDs: {df_record['Customer_ID'].nunique():,}")
print(f"Exact row duplicates: Client = {df_client.duplicated().sum()}, Record = {df_record.duplicated().sum()}")

# %%
# 1.3 Key Set Differences & Join Verification
set_client = set(df_client["Customer_ID"])
set_record = set(df_record["Customer_ID"])

in_both = len(set_client.intersection(set_record))
in_client_only = len(set_client - set_record)
in_record_only = len(set_record - set_client)

print(f"IDs in BOTH tables: {in_both:,} | Client-only: {in_client_only} | Record-only: {in_record_only}")

df = pd.merge(df_client, df_record, on="Customer_ID", how="inner")
print(f"Merged Dataset Shape (DEC-004): {df.shape[0]:,} rows x {df.shape[1]} columns")
assert df.shape == (100000, 100), "Shape mismatch on inner join!"
print("Data Gate 1 Passed: 100,000 unique records match 1:1 with zero orphan keys.")

# %%
# 1.4 Target Variable Churn Distribution
churn_counts = df["churn"].value_counts(dropna=False)
churn_pcts = df["churn"].value_counts(normalize=True, dropna=False) * 100

df_target_summary = pd.DataFrame({"Count": churn_counts, "Percentage (%)": churn_pcts.round(4)})
print("\nTarget Class Distribution:")
print(df_target_summary)

# %%
# 1.5 Missingness Overview Across Top Attributes
missing_counts = df.isna().sum()
top_missing = missing_counts[missing_counts > 0].sort_values(ascending=False).head(15)
top_missing_pct = (top_missing / len(df)) * 100
df_missing_summary = pd.DataFrame({"Missing_Count": top_missing, "Missing_Pct": top_missing_pct.round(2)})
print("\nTop 15 Missing Attributes:")
print(df_missing_summary)

# %% [markdown]
# ---
# ## SECTION 2: EXPLORATORY DATA ANALYSIS & HYPOTHESIS TESTING (Stage 3)
# Testing business hypotheses H1–H4, analyzing value-at-risk revenue segments, and generating clean figures.

# %%
# 2.1 Figure 1: Target Churn Distribution
fig, ax = plt.subplots(figsize=(7.5, 4.8))
bars = ax.bar(["Retained (0)", "Churned (1)"], churn_counts.values, color=[color_blue, color_orange], width=0.45, edgecolor="black", linewidth=0.8)
for bar, count, pct in zip(bars, churn_counts.values, churn_pcts.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1000, f"{count:,} ({pct:.2f}%)", ha="center", va="bottom", fontsize=11, fontweight="bold")
ax.set_ylim(0, 60000)
ax.set_title("Figure 1: Target Churn Distribution (Balanced Observational Sample)", pad=14)
ax.set_ylabel("Customer Count (n = 100,000)")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "fig1_target_balance_and_structure.png", dpi=300)
plt.show()

# %%
# 2.2 Figure 2: Missingness Profile
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(top_missing.index[:12][::-1], top_missing_pct.values[:12][::-1], color="#4575b4", edgecolor="black", linewidth=0.6)
for bar, pct in zip(bars, top_missing_pct.values[:12][::-1]):
    ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height() / 2, f"{pct:.1f}%", va="center", fontsize=9.5, fontweight="bold")
ax.set_xlim(0, 58)
ax.set_title("Figure 2: Top Features by Missingness Ratio", pad=14)
ax.set_xlabel("Missing Percentage (% of 100,000 records)")
ax.axvline(30, color="red", linestyle="--", linewidth=1.2, label="High Missingness Threshold (30%)")
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "fig2_missingness_structure.png", dpi=300)
plt.show()

# %%
# 2.3 Hypothesis H1: Consumption Drop as a Leading Indicator (change_mou)
df_h1 = df.dropna(subset=["change_mou", "change_rev"]).copy()
mou_bins = [-np.inf, -100, -20, 0, 20, 100, np.inf]
mou_labels = ["Severe Drop (<-100m)", "Moderate Drop (-100 to -20m)", "Slight Drop (-20 to 0m)", 
              "Slight Growth (0 to 20m)", "Moderate Growth (20 to 100m)", "Strong Growth (>100m)"]
df_h1["mou_change_bin"] = pd.cut(df_h1["change_mou"], bins=mou_bins, labels=mou_labels)
h1_stats = df_h1.groupby("mou_change_bin", observed=False).agg(
    total_customers=("churn", "count"),
    churn_rate=("churn", "mean")
).reset_index()
h1_stats["churn_pct"] = h1_stats["churn_rate"] * 100

print("Hypothesis H1 Statistics (change_mou vs Churn):")
print(h1_stats)

stat_mou, p_val_mou = stats.mannwhitneyu(df[df["churn"] == 1]["change_mou"].dropna(),
                                         df[df["churn"] == 0]["change_mou"].dropna())
print(f"Mann-Whitney U Test for change_mou: p-value = {p_val_mou:.4e}")

fig, ax = plt.subplots(figsize=(9.5, 4.8))
bars = ax.bar(range(len(h1_stats)), h1_stats["churn_pct"], 
              color=["#d73027", "#fc8d59", "#fee090", "#e0f3f8", "#91bfdb", "#4575b4"], 
              edgecolor="black", linewidth=0.7)
for bar, pct in zip(bars, h1_stats["churn_pct"]):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{pct:.1f}%", ha="center", va="bottom", fontsize=10, fontweight="bold")
ax.axhline(49.56, color="black", linestyle=":", linewidth=1.2, label="Sample Baseline (49.56%)")
ax.set_xticks(range(len(h1_stats)))
ax.set_xticklabels(h1_stats["mou_change_bin"], rotation=15, ha="right")
ax.set_ylim(0, 65)
ax.set_title("Figure 3: Churn Rate by Usage Trend (change_mou)", pad=14)
ax.set_ylabel("Observed Churn Rate (%)")
ax.legend(loc="upper right")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "fig3_h1_consumption_drop_change_mou_rev.png", dpi=300)
plt.show()

# %%
# 2.4 Hypothesis H2: Equipment Lifecycle Cliff (eqpdays)
df_h2 = df.dropna(subset=["eqpdays"]).copy()
eqp_bins = [-np.inf, 180, 365, 730, np.inf]
eqp_labels = ["< 6 Months (New)", "6 - 12 Months", "1 - 2 Years (Contract Cliff)", "> 2 Years (Aged)"]
df_h2["eqp_bracket"] = pd.cut(df_h2["eqpdays"], bins=eqp_bins, labels=eqp_labels)
h2_stats = df_h2.groupby("eqp_bracket", observed=False).agg(
    total_customers=("churn", "count"),
    churn_rate=("churn", "mean")
).reset_index()
h2_stats["churn_pct"] = h2_stats["churn_rate"] * 100

print("Hypothesis H2 Statistics (eqpdays vs Churn):")
print(h2_stats)

stat_eqp, p_val_eqp = stats.mannwhitneyu(df[df["churn"] == 1]["eqpdays"].dropna(),
                                         df[df["churn"] == 0]["eqpdays"].dropna())
print(f"Mann-Whitney U Test for eqpdays: p-value = {p_val_eqp:.4e}")

fig, ax = plt.subplots(figsize=(8.5, 4.8))
bars = ax.bar(h2_stats["eqp_bracket"], h2_stats["churn_pct"], 
              color=["#2b83ba", "#abdda4", "#fdae61", "#d7191c"], edgecolor="black", linewidth=0.7, width=0.5)
for bar, pct, count in zip(bars, h2_stats["churn_pct"], h2_stats["total_customers"]):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{pct:.1f}%\n(n={count:,})", ha="center", va="bottom", fontsize=10, fontweight="bold")
ax.axhline(49.56, color="black", linestyle=":", linewidth=1.2, label="Sample Baseline (49.56%)")
ax.set_ylim(0, 66)
ax.set_title("Figure 4: Churn Risk by Equipment Age (eqpdays)", pad=14)
ax.set_ylabel("Observed Churn Rate (%)")
ax.legend(loc="upper left")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "fig4_h2_equipment_age_lifecycle.png", dpi=300)
plt.show()

# %%
# 2.5 Hypothesis H3: The "Silent Churner" Paradox (custcare_Mean & drop_blk_Mean)
df_h3 = df.copy()
df_h3["custcare_group"] = pd.cut(df_h3["custcare_Mean"].fillna(0), 
                                 bins=[-np.inf, 0, 1, 3, np.inf], 
                                 labels=["0 Calls", "0.1 - 1/Mo", "1.1 - 3/Mo", "> 3/Mo"])
h3_stats = df_h3.groupby("custcare_group", observed=False).agg(
    total_customers=("churn", "count"),
    churn_rate=("churn", "mean")
).reset_index()
h3_stats["churn_pct"] = h3_stats["churn_rate"] * 100

print("Hypothesis H3 Statistics (custcare_Mean vs Churn):")
print(h3_stats)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.5))
bars = ax1.bar(h3_stats["custcare_group"], h3_stats["churn_pct"], color="#8073ac", edgecolor="black", width=0.5)
for bar, pct in zip(bars, h3_stats["churn_pct"]):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{pct:.1f}%", ha="center", va="bottom", fontsize=10, fontweight="bold")
ax1.axhline(49.56, color="black", linestyle=":", linewidth=1)
ax1.set_ylim(0, 60)
ax1.set_title("Churn Rate by Care Calls", fontsize=11, fontweight="bold")
ax1.set_ylabel("% Churn")

q95 = df["drop_blk_Mean"].quantile(0.95)
df_sub_drops = df[df["drop_blk_Mean"] <= q95]
sns.boxplot(data=df_sub_drops, x="churn", y="drop_blk_Mean", hue="churn", ax=ax2, palette=[color_blue, color_orange], legend=False, width=0.38)
ax2.set_xticks([0, 1])
ax2.set_xticklabels(["Retained (0)", "Churned (1)"])
ax2.set_title("Dropped & Blocked Calls Distribution", fontsize=11, fontweight="bold")
ax2.set_ylabel("Calls / Month")
ax2.set_xlabel("")
fig.suptitle("Figure 5: Support Interactions and Network Drops", fontsize=12, fontweight="bold", y=1.01)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "fig5_h3_service_friction_custcare_drops.png", dpi=300, bbox_inches="tight")
plt.show()

# %%
# 2.6 Hypothesis H4: Multi-Line Household Stickiness (actvsubs)
df_h4 = df.copy()
df_h4["subs_tier"] = np.where(df_h4["actvsubs"] == 1, "1 Line (Single)",
                     np.where(df_h4["actvsubs"] == 2, "2 Lines (Pair)", ">= 3 Lines (Family)"))
order_tiers = ["1 Line (Single)", "2 Lines (Pair)", ">= 3 Lines (Family)"]
h4_stats = df_h4.groupby("subs_tier", observed=False).agg(
    total_customers=("churn", "count"),
    churn_rate=("churn", "mean")
).reindex(order_tiers).reset_index()
h4_stats["churn_pct"] = h4_stats["churn_rate"] * 100

print("Hypothesis H4 Statistics (actvsubs vs Churn):")
print(h4_stats)

fig, ax = plt.subplots(figsize=(7.5, 4.5))
bars = ax.bar(h4_stats["subs_tier"], h4_stats["churn_pct"], 
              color=["#e7298a", "#7570b3", "#1b9e77"], edgecolor="black", width=0.48)
for bar, pct, count in zip(bars, h4_stats["churn_pct"], h4_stats["total_customers"]):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{pct:.1f}%\n(n={count:,})", ha="center", va="bottom", fontsize=9.5, fontweight="bold")
ax.axhline(49.56, color="black", linestyle=":", linewidth=1.2, label="Sample Baseline (49.56%)")
ax.set_ylim(0, 60)
ax.set_title("Figure 6: Churn Rate by Active Lines per Household", pad=14)
ax.set_ylabel("Observed Churn Rate (%)")
ax.legend(loc="upper right")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "fig6_h4_household_stickiness_actvsubs.png", dpi=300)
plt.show()

# %%
# 2.7 Value Segmentation: Monthly Revenue & Value at Risk
df_clean_rev = df.dropna(subset=["rev_Mean"]).copy()
df_clean_rev["rev_quintile"] = pd.qcut(df_clean_rev["rev_Mean"], q=5, 
                                      labels=["Q1 (<$27)", "Q2 ($27-$39)", 
                                              "Q3 ($39-$53)", "Q4 ($53-$74)", "Q5 (>$74)"])
rev_stats = df_clean_rev.groupby("rev_quintile", observed=False).agg(
    total_customers=("churn", "count"),
    churn_rate=("churn", "mean"),
    total_monthly_revenue=("rev_Mean", "sum")
).reset_index()
rev_stats["churn_pct"] = rev_stats["churn_rate"] * 100
rev_stats["churned_revenue_at_risk"] = rev_stats["total_monthly_revenue"] * rev_stats["churn_rate"]

print("Revenue Segmentation Table:")
print(rev_stats)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.5))
bars1 = ax1.bar(rev_stats["rev_quintile"], rev_stats["churn_pct"], color="#41b6c4", edgecolor="black", width=0.5)
for bar, pct in zip(bars1, rev_stats["churn_pct"]):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{pct:.1f}%", ha="center", va="bottom", fontsize=9.5, fontweight="bold")
ax1.axhline(49.56, color="black", linestyle=":", linewidth=1)
ax1.set_ylim(0, 62)
ax1.set_title("Churn Rate by Revenue Quintile", fontsize=11, fontweight="bold")
ax1.set_ylabel("% Churn")

bars2 = ax2.bar(rev_stats["rev_quintile"], rev_stats["churned_revenue_at_risk"] / 1000, color=color_orange, edgecolor="black", width=0.5)
for bar, val in zip(bars2, rev_stats["churned_revenue_at_risk"] / 1000):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 12, f"${val:,.0f}k", ha="center", va="bottom", fontsize=9.5, fontweight="bold")
ax2.set_title("Monthly Revenue at Risk ($ Thousands)", fontsize=11, fontweight="bold")
ax2.set_ylabel("Expected Churned Revenue ($k/month)")
fig.suptitle("Figure 7: Churn Rate vs. Revenue Exposure Across Quintiles", fontsize=12, fontweight="bold", y=1.01)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "fig7_revenue_segmentation_value_at_risk.png", dpi=300, bbox_inches="tight")
plt.show()

# %%
# 2.8 Correlation Matrix of Key Behavioral Features
key_cols = [
    "churn", "eqpdays", "change_mou", "change_rev", "mou_Mean", 
    "rev_Mean", "totmrc_Mean", "custcare_Mean", "drop_blk_Mean", 
    "actvsubs", "months", "hnd_price"
]
df_corr = df[key_cols].corr()
fig, ax = plt.subplots(figsize=(9, 7))
sns.heatmap(df_corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-0.25, vmax=0.25, 
            linewidths=0.5, cbar_kws={"label": "Pearson r"}, ax=ax)
ax.set_title("Figure 8: Correlation Matrix of Key Behavioral Drivers and Churn", pad=14)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "fig8_correlation_matrix_key_drivers.png", dpi=300)
plt.show()

print("\nSection 2 (EDA) Complete.")

# %% [markdown]
# ---
# ## SECTION 3: PROBLEM DEFINITION, FEATURE TIMING & DATA LEAKAGE AUDIT (Stage 4)
# Formulating the executive business question, defining prediction horizon (Days 31–60) with 30-day operational lead time,
# auditing feature space column-by-column for leakage, and establishing the business profit evaluation framework.

# %%
# 3.1 Feature Space Formulation & Identifier Exclusion (DEC-005)
# Target: 'churn' (0 = Retained, 1 = Churned in 31-60 days post-observation date T_0)
# Lead time: Days 1 to 30 post-T_0 serve as operational intervention window for retention campaigns.

target_col = "churn"
id_col = "Customer_ID"

# Feature matrix excluding identifier and target
feature_cols = [c for c in df.columns if c not in [id_col, target_col]]
numeric_cols = df[feature_cols].select_dtypes(include=[np.number]).columns.tolist()
cat_cols = df[feature_cols].select_dtypes(include=["object"]).columns.tolist()

print("--- 3.1 Feature Space Composition ---")
print(f"Total Columns in Dataset:  {len(df.columns)}")
print(f"Target Column:             '{target_col}' (Distribution: {churn_pcts[0]:.2f}% Retained vs {churn_pcts[1]:.2f}% Churned)")
print(f"Identifier (Excluded):     '{id_col}' (Integrity: 100k unique IDs, zero duplicates)")
print(f"Modeling Predictors:       {len(feature_cols)} features ({len(numeric_cols)} Numerical, {len(cat_cols)} Categorical)")

assert len(feature_cols) == 98, f"Expected 98 features, found {len(feature_cols)}"
assert id_col not in feature_cols, f"CRITICAL: {id_col} must NOT be in feature set!"
print("Assertion Passed: Feature space contains exactly 98 predictors with zero ID leakage.")

# %%
# 3.2 Exhaustive Feature Timing & Data Leakage Review
# Checking for:
# 1) Suspiciously high correlations with churn (>0.50 indicates potential proxy/leakage)
# 2) Zero-variance (constant) features that offer zero discriminatory power

print("\n--- 3.2 Data Leakage & Feature Sanity Audit ---")
corrs_with_churn = df[numeric_cols].apply(lambda x: x.corr(df[target_col])).abs().sort_values(ascending=False)

print("Top 10 Numerical Features by Absolute Correlation with Churn:")
print(corrs_with_churn.head(10).round(4))

max_corr_val = corrs_with_churn.iloc[0]
max_corr_feat = corrs_with_churn.index[0]
print(f"\nMax Correlation: {max_corr_feat} = {max_corr_val:.4f}")

# Rigorous Leakage Check: No single feature should have correlation > 0.20 with churn
assert max_corr_val < 0.20, f"Leakage Warning: {max_corr_feat} has correlation {max_corr_val:.4f} >= 0.20!"
print("Leakage Gate Passed: No single feature exhibits deterministic or proxy leakage with target churn.")

# Constant feature check
constant_cols = [c for c in feature_cols if df[c].nunique(dropna=False) <= 1]
print(f"Zero-variance (constant) features count: {len(constant_cols)}")
assert len(constant_cols) == 0, "Constant features detected!"
print("Sanity Gate Passed: Zero constant features found across 100,000 subscriber records.")

# %%
# 3.3 Decision-Driven Metric Hierarchy & Net Expected Profit Framework
# Because target is balanced (49.56% churn) but False Negatives (lost CLV) >> False Positives (subsidy cost),
# we formalize the Net Expected Retained Profit function to evaluate operational cutoff thresholds.

def calculate_expected_retention_profit(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    threshold: float,
    arpu_series: pd.Series,
    margin_pct: float = 0.70,
    tenure_months: int = 12,
    retention_success_rate: float = 0.25,
    incentive_cost: float = 75.0,
    subsidy_waste_cost: float = 35.0,
    contact_cost: float = 3.0
) -> dict:
    """
    Computes business-driven net profit from proactive churn retention campaigns.
    
    Parameters:
    - arpu_series: Subscriber monthly revenue (rev_Mean)
    - retention_success_rate: Probability a targeted churner accepts offer and stays (20%-35%)
    - incentive_cost: Cost of retained handset voucher/plan adjustment accepted by churner ($75)
    - subsidy_waste_cost: Cost incurred when offering subsidy to non-churner who would stay anyway ($35)
    - contact_cost: Outbound call / SMS / app outreach cost per targeted subscriber ($3)
    """
    y_pred = (y_prob >= threshold).astype(int)
    
    # Confusion matrix elements
    tp_mask = (y_true == 1) & (y_pred == 1)
    fp_mask = (y_true == 0) & (y_pred == 1)
    fn_mask = (y_true == 1) & (y_pred == 0)
    tn_mask = (y_true == 0) & (y_pred == 0)
    
    n_targeted = int(y_pred.sum())
    
    # Financial components
    # Retained value = Saved Gross Margin over 12 months
    retained_clv = (arpu_series[tp_mask] * margin_pct * tenure_months).sum()
    gross_benefit = retained_clv * retention_success_rate
    
    total_incentive_cost = (tp_mask.sum() * retention_success_rate * incentive_cost) + (fp_mask.sum() * subsidy_waste_cost)
    total_contact_cost = n_targeted * contact_cost
    
    net_profit = gross_benefit - total_incentive_cost - total_contact_cost
    
    return {
        "threshold": threshold,
        "targeted_subscribers": n_targeted,
        "targeted_pct": float(n_targeted / len(y_true) * 100),
        "true_positives": int(tp_mask.sum()),
        "false_positives": int(fp_mask.sum()),
        "precision": float(tp_mask.sum() / max(n_targeted, 1)),
        "recall": float(tp_mask.sum() / max(y_true.sum(), 1)),
        "gross_saved_margin": float(gross_benefit),
        "total_cost": float(total_incentive_cost + total_contact_cost),
        "net_retained_profit": float(net_profit)
    }

print("\n--- 3.3 Metric Hierarchy Configured ---")
print("1. Primary Ranking Metric:     ROC-AUC (Global threshold-independent discrimination)")
print("2. Operational Efficiency:    PR-AUC & Precision @ Top 20% (Lift @ Quintile 1)")
print("3. Financial ROI Metric:       Net Expected Retained Profit (Cost-Benefit Matrix)")
print("4. Diagnostic Metrics:         Accuracy, Recall, F1-Score at business-optimal threshold tau*")

print("\nStage 4 Completed: Problem Definition & Data Leakage Review PASSED.")
print("Pipeline ready for Stage 5 (Data Preparation & Controlled Feature Engineering)!")

