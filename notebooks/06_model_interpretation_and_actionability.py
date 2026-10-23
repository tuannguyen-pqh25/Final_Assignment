# %% [markdown]
# # GCI World 2026 Final Assignment — Stage 7: Model Interpretation, Robustness & Strategic Actionability
# **Dataset:** Company A (100,000 customers x 100 features)  
# **Objective:** Compute permutation feature importance on champion model, enforce ethical firewall on demographics, and execute subgroup robustness audit across key operational segments.

# %%
from pathlib import Path
import joblib
import pandas as pd
import numpy as np
import matplotlib
import sys
if not hasattr(sys, "ps1") and "ipykernel" not in sys.modules:
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from sklearn.inspection import permutation_importance
from sklearn.metrics import roc_auc_score, average_precision_score, precision_score, recall_score

# Reproducibility settings
SEED = 42
BASE_DIR = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
DATA_PROCESSED_DIR = BASE_DIR / "data" / "processed"
MODELS_DIR = BASE_DIR / "models"
REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# %% [markdown]
# ## 1. Instant Load of Preprocessed Matrices & Champion Model (0.2s)

# %%
checkpoint_path = DATA_PROCESSED_DIR / "pipeline_data.joblib"
model_path = MODELS_DIR / "champion_hist_gradient_boosting.joblib"

assert checkpoint_path.exists(), "pipeline_data.joblib missing! Run 04_data_preparation_and_features.py first."
assert model_path.exists(), "champion_model missing! Run 05_model_benchmarking_and_evaluation.py first."

checkpoint = joblib.load(checkpoint_path)
champion_model = joblib.load(model_path)

X_val_proc = checkpoint["X_val_proc"]
y_val = checkpoint["y_val"]
X_val_df = checkpoint["X_val_df"]
feature_names = checkpoint["feature_names"]
opt_threshold = checkpoint["opt_threshold"]

print(f"Loaded Preprocessed Validation Matrix: {X_val_proc.shape}")
print(f"Loaded Champion Model: {champion_model.__class__.__name__}")

# %% [markdown]
# ## 2. Permutation Feature Importance Analysis
# Evaluated on 2,000 representative validation samples over 5 repeats. Single-threaded (n_jobs=1).

# %%
np.random.seed(SEED)
val_subsample_idx = np.random.choice(len(X_val_proc), size=2000, replace=False)
X_val_sub = X_val_proc[val_subsample_idx]
y_val_sub = y_val[val_subsample_idx]

perm_importance = permutation_importance(
    champion_model,
    X_val_sub,
    y_val_sub,
    n_repeats=5,
    scoring="roc_auc",
    random_state=SEED,
    n_jobs=1
)

sorted_importances_idx = np.argsort(perm_importance.importances_mean)[::-1]

df_perm_imp = pd.DataFrame({
    "feature": [feature_names[i] for i in sorted_importances_idx],
    "importance_mean": perm_importance.importances_mean[sorted_importances_idx],
    "importance_std": perm_importance.importances_std[sorted_importances_idx]
})

print("\nTop 15 Features by Permutation Importance (ROC-AUC drop):")
for rank, row in df_perm_imp.head(15).reset_index().iterrows():
    print(f"{rank + 1:2d}. {row['feature']:35s} | Mean: {row['importance_mean']:+.4f} | Std: {row['importance_std']:.4f}")

# %% [markdown]
# ## 3. Strategic Actionability & Governance Taxonomy (DEC-021 & DEC-022)

# %%
actionability_map = {
    # Actionable Levers
    "num__eqpdays": {"category": "Actionable Lever", "concept": "Handset Age", "intervention": "Targeted handset upgrade subsidy"},
    "num__change_mou": {"category": "Actionable Lever", "concept": "Usage Drop", "intervention": "Plan rightsizing, rollover minutes"},
    "num__rev_per_mou": {"category": "Actionable Lever", "concept": "Effective Cost per Min", "intervention": "Bill shock mitigation, flat-rate plan"},
    "num__hnd_price": {"category": "Actionable Lever", "concept": "Handset Price Tier", "intervention": "Premium handset trade-in plans"},
    "num__drop_per_call": {"category": "Actionable Lever", "concept": "Dropped Call Rate", "intervention": "Network cell optimization, service credit"},
    "num__drop_vce_Mean": {"category": "Actionable Lever", "concept": "Dropped Voice Calls", "intervention": "Proactive outreach to poor coverage areas"},
    "num__overage_rev_ratio": {"category": "Actionable Lever", "concept": "Overage Rev Share", "intervention": "Zero-overage migration, auto-safety threshold"},
    "num__eqp_to_tenure_ratio": {"category": "Actionable Lever", "concept": "Handset-to-Tenure Ratio", "intervention": "Lifecycle milestone renewal bonus"},
    "num__severe_mou_drop": {"category": "Actionable Lever", "concept": "Severe MOU Drop Flag", "intervention": "Automated concierge re-activation offer"},
    # Observational Signals
    "num__months": {"category": "Observational Signal", "concept": "Account Tenure", "intervention": "Contract milestone loyalty tiers"},
    "num__totmrc_Mean": {"category": "Observational Signal", "concept": "Base Monthly Recurring Charge", "intervention": "Value segmentation anchor"},
    "num__mou_Mean": {"category": "Observational Signal", "concept": "Recent Monthly MOU", "intervention": "Capacity sizing context"},
    "num__avgqty": {"category": "Observational Signal", "concept": "Baseline Call Quantity", "intervention": "Behavioral profile"},
    "num__avgmou": {"category": "Observational Signal", "concept": "Baseline Average MOU", "intervention": "Long-term usage baseline"},
    "num__totcalls": {"category": "Observational Signal", "concept": "Total Calls to Date", "intervention": "Historical volume context"},
    "num__uniqsubs": {"category": "Observational Signal", "concept": "Unique Handsets Used", "intervention": "Account tech complexity"},
    "num__avgrev": {"category": "Observational Signal", "concept": "Average Monthly Revenue", "intervention": "Customer Value segmentation tier"},
    "num__missingindicator_change_mou": {"category": "Observational Signal", "concept": "Missing Usage History", "intervention": "Onboarding journey trigger"},
    # Sensitive Demographics (STRICTLY NON-TARGETABLE)
    "num__lor": {"category": "Sensitive / Demographic", "concept": "Length of Residence", "intervention": "NON-TARGETABLE (Demographic proxy)"},
    "cat__ethnic_O": {"category": "Sensitive / Demographic", "concept": "Ethnicity Code", "intervention": "STRICTLY FORBIDDEN FROM RETENTION TARGETING"},
    "num__income": {"category": "Sensitive / Demographic", "concept": "Household Income", "intervention": "NON-TARGETABLE (Socioeconomic proxy)"}
}

df_perm_imp["category"] = df_perm_imp["feature"].apply(
    lambda f: actionability_map.get(f, {}).get("category", "Observational Signal")
)
df_perm_imp["concept"] = df_perm_imp["feature"].apply(
    lambda f: actionability_map.get(f, {}).get("concept", f.replace("num__", "").replace("cat__", ""))
)

# %% [markdown]
# ## 4. Subgroup Robustness Audit (Validation Set: N = 15,000)

# %%
val_audit_df = X_val_df.copy()
val_audit_df["actual_churn"] = y_val
val_audit_df["pred_prob"] = champion_model.predict_proba(X_val_proc)[:, 1]
val_audit_df["pred_label"] = (val_audit_df["pred_prob"] >= opt_threshold).astype(int)

def evaluate_subgroup_metrics(sub_df, segment_name, sub_name):
    n = len(sub_df)
    actual_churn_rate = sub_df["actual_churn"].mean() * 100
    y_t = sub_df["actual_churn"].values
    y_p = sub_df["pred_prob"].values
    y_b = sub_df["pred_label"].values
    
    auc = roc_auc_score(y_t, y_p)
    ap = average_precision_score(y_t, y_p)
    prec = precision_score(y_t, y_b, zero_division=0) * 100
    rec = recall_score(y_t, y_b, zero_division=0) * 100
    
    return {
        "Segment": segment_name, "Subgroup": sub_name, "N": n,
        "Share (%)": (n / len(val_audit_df)) * 100,
        "Actual Churn (%)": actual_churn_rate,
        "ROC-AUC": auc, "PR-AUC": ap,
        "Precision@0.25 (%)": prec, "Recall@0.25 (%)": rec
    }

subgroup_results = [
    evaluate_subgroup_metrics(val_audit_df[val_audit_df['eqpdays'] < 365], "Equipment Lifecycle", "New (< 1 Year)"),
    evaluate_subgroup_metrics(val_audit_df[(val_audit_df['eqpdays'] >= 365) & (val_audit_df['eqpdays'] < 730)], "Equipment Lifecycle", "Maturing (1-2 Years)"),
    evaluate_subgroup_metrics(val_audit_df[val_audit_df['eqpdays'] >= 730], "Equipment Lifecycle", "Aged (2+ Years)"),
    evaluate_subgroup_metrics(val_audit_df[val_audit_df['rev_Mean'] < 35], "ARPU Tier", "Low (< $35)"),
    evaluate_subgroup_metrics(val_audit_df[(val_audit_df['rev_Mean'] >= 35) & (val_audit_df['rev_Mean'] < 50)], "ARPU Tier", "Mid-Low ($35-$50)"),
    evaluate_subgroup_metrics(val_audit_df[(val_audit_df['rev_Mean'] >= 50) & (val_audit_df['rev_Mean'] < 75)], "ARPU Tier", "Mid-High ($50-$75)"),
    evaluate_subgroup_metrics(val_audit_df[val_audit_df['rev_Mean'] >= 75], "ARPU Tier", "High ($75+)"),
    evaluate_subgroup_metrics(val_audit_df[val_audit_df['actvsubs'] == 1], "Line Count", "Single-Line (1)"),
    evaluate_subgroup_metrics(val_audit_df[val_audit_df['actvsubs'] >= 2], "Line Count", "Multi-Line (2+)"),
    evaluate_subgroup_metrics(val_audit_df[val_audit_df['months'] < 12], "Account Tenure", "Early (< 1 Year)"),
    evaluate_subgroup_metrics(val_audit_df[(val_audit_df['months'] >= 12) & (val_audit_df['months'] < 24)], "Account Tenure", "Mid (1-2 Years)"),
    evaluate_subgroup_metrics(val_audit_df[val_audit_df['months'] >= 24], "Account Tenure", "Mature (2+ Years)")
]

df_subgroups = pd.DataFrame(subgroup_results)
print("\n--- Subgroup Robustness Audit Results ---")
print(df_subgroups.to_string(index=False))

min_auc = df_subgroups["ROC-AUC"].min()
print(f"\nMinimum Subgroup ROC-AUC: {min_auc:.4f} (Quality Gate: >= 0.6000)")
assert min_auc >= 0.60, "Subgroup collapse detected!"
print("Robustness Gate Passed: Discrimination is stable across all operational segments.")

# %% [markdown]
# ## 5. Visualizing Figure 11 (Feature Actionability) and Figure 12 (Subgroup Robustness)

# %%
top_plot_df = df_perm_imp.head(15).iloc[::-1]
color_map = {"Actionable Lever": "#1b9e77", "Observational Signal": "#2b5c8f", "Sensitive / Demographic": "#e7298a"}
bar_colors = [color_map.get(cat, "#7570b3") for cat in top_plot_df["category"]]

fig, ax = plt.subplots(figsize=(12, 7.5))
y_positions = np.arange(len(top_plot_df))
ax.barh(y_positions, top_plot_df["importance_mean"], xerr=top_plot_df["importance_std"], color=bar_colors, edgecolor="black", linewidth=0.8, capsize=4, alpha=0.9)
clean_labels = [f"{row['concept']} ({row['feature'].replace('num__', '').replace('cat__', '')})" for _, row in top_plot_df.iterrows()]
ax.set_yticks(y_positions)
ax.set_yticklabels(clean_labels, fontsize=10)
ax.set_xlabel("Permutation Feature Importance (Mean ROC-AUC Drop ± 1 Std)", fontsize=11, fontweight="bold")
ax.set_title("Figure 11: Top 15 Feature Importances & Strategic Actionability Classification", fontsize=13, fontweight="bold", pad=14)

legend_elements = [
    Patch(facecolor="#1b9e77", edgecolor="black", label="Actionable Lever (Direct Marketing / Plan / Network Intervention)"),
    Patch(facecolor="#2b5c8f", edgecolor="black", label="Observational Signal (Lifecycle / Usage Context for Triggering)"),
    Patch(facecolor="#e7298a", edgecolor="black", label="Sensitive Demographic (Strictly Non-Targetable / Governance Only)")
]
ax.legend(handles=legend_elements, loc="lower right", frameon=True, fontsize=9.5)
ax.grid(axis="x", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "fig11_feature_importance_actionability.png", dpi=300, bbox_inches="tight")
plt.close()
print(f"Saved Figure 11 to {FIGURES_DIR / 'fig11_feature_importance_actionability.png'}")

print("\nStage 7 Completed: Model Interpretation & Actionability PASSED.")
