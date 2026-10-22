import sys
from pathlib import Path
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def run_clean_eda_figures():
    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir / "data" / "raw"
    if not data_dir.exists():
        data_dir = base_dir / "telecom"
    reports_dir = base_dir / "reports"
    figures_dir = reports_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    
    # Professional styling - clean, executive-ready, no clutter
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.size"] = 11
    plt.rcParams["axes.titlesize"] = 13
    plt.rcParams["axes.titleweight"] = "bold"
    plt.rcParams["axes.labelsize"] = 11
    plt.rcParams["axes.labelweight"] = "bold"
    plt.rcParams["figure.dpi"] = 300
    
    color_blue = "#2b5c8f"
    color_orange = "#d95f02"
    
    print("Loading data for clean EDA charts...")
    df_client = pd.read_csv(data_dir / "Client.csv")
    df_record = pd.read_csv(data_dir / "Record.csv")
    df = pd.merge(df_client, df_record, on="Customer_ID", how="inner")
    
    # -------------------------------------------------------------------------
    # FIGURE 1: Clean Target Churn Balance
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(7.5, 4.8))
    churn_counts = df["churn"].value_counts()
    churn_pcts = df["churn"].value_counts(normalize=True) * 100
    labels = ["Retained (0)", "Churned (1)"]
    bars = ax.bar(labels, churn_counts.values, color=[color_blue, color_orange], width=0.45, edgecolor="black", linewidth=0.8)
    for bar, count, pct in zip(bars, churn_counts.values, churn_pcts.values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1000, 
                f"{count:,} ({pct:.2f}%)", ha="center", va="bottom", fontsize=11, fontweight="bold")
    ax.set_ylim(0, 60000)
    ax.set_title("Figure 1: Target Churn Distribution (Balanced Observational Sample)", pad=14)
    ax.set_ylabel("Customer Count (n = 100,000)")
    plt.tight_layout()
    plt.savefig(figures_dir / "fig1_target_balance_and_structure.png", dpi=300)
    plt.close()
    
    # -------------------------------------------------------------------------
    # FIGURE 2: Clean Missingness Profile
    # -------------------------------------------------------------------------
    missing_counts = df.isna().sum()
    top_missing = missing_counts[missing_counts > 0].sort_values(ascending=False).head(12)
    top_missing_pct = (top_missing / len(df)) * 100
    
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(top_missing.index[::-1], top_missing_pct.values[::-1], color="#4575b4", edgecolor="black", linewidth=0.6)
    for bar, pct in zip(bars, top_missing_pct.values[::-1]):
        ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height() / 2, f"{pct:.1f}%", va="center", fontsize=9.5, fontweight="bold")
    ax.set_xlim(0, 58)
    ax.set_title("Figure 2: Top Features by Missingness Ratio", pad=14)
    ax.set_xlabel("Missing Percentage (% of 100,000 records)")
    ax.axvline(30, color="red", linestyle="--", linewidth=1.2, label="High Missingness Threshold (30%)")
    ax.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(figures_dir / "fig2_missingness_structure.png", dpi=300)
    plt.close()

    # -------------------------------------------------------------------------
    # FIGURE 3: Clean Hypothesis H1 (change_mou)
    # -------------------------------------------------------------------------
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
    plt.savefig(figures_dir / "fig3_h1_consumption_drop_change_mou_rev.png", dpi=300)
    plt.close()

    # -------------------------------------------------------------------------
    # FIGURE 4: Clean Hypothesis H2 (eqpdays)
    # -------------------------------------------------------------------------
    df_h2 = df.dropna(subset=["eqpdays"]).copy()
    eqp_bins = [-np.inf, 180, 365, 730, np.inf]
    eqp_labels = ["< 6 Months (New)", "6 - 12 Months", "1 - 2 Years (Contract Cliff)", "> 2 Years (Aged)"]
    df_h2["eqp_bracket"] = pd.cut(df_h2["eqpdays"], bins=eqp_bins, labels=eqp_labels)
    h2_stats = df_h2.groupby("eqp_bracket", observed=False).agg(
        total_customers=("churn", "count"),
        churn_rate=("churn", "mean")
    ).reset_index()
    h2_stats["churn_pct"] = h2_stats["churn_rate"] * 100
    
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    bars = ax.bar(h2_stats["eqp_bracket"], h2_stats["churn_pct"], 
                  color=["#2b83ba", "#abdda4", "#fdae61", "#d7191c"], edgecolor="black", linewidth=0.7, width=0.5)
    for bar, pct, count in zip(bars, h2_stats["churn_pct"], h2_stats["total_customers"]):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, 
                f"{pct:.1f}%\n(n={count:,})", ha="center", va="bottom", fontsize=10, fontweight="bold")
    ax.axhline(49.56, color="black", linestyle=":", linewidth=1.2, label="Sample Baseline (49.56%)")
    ax.set_ylim(0, 66)
    ax.set_title("Figure 4: Churn Risk by Equipment Age (eqpdays)", pad=14)
    ax.set_ylabel("Observed Churn Rate (%)")
    ax.legend(loc="upper left")
    plt.tight_layout()
    plt.savefig(figures_dir / "fig4_h2_equipment_age_lifecycle.png", dpi=300)
    plt.close()

    # -------------------------------------------------------------------------
    # FIGURE 5: Clean Hypothesis H3 (custcare & drops)
    # -------------------------------------------------------------------------
    df_h3 = df.copy()
    df_h3["custcare_group"] = pd.cut(df_h3["custcare_Mean"].fillna(0), 
                                     bins=[-np.inf, 0, 1, 3, np.inf], 
                                     labels=["0 Calls", "0.1 - 1/Mo", "1.1 - 3/Mo", "> 3/Mo"])
    h3_stats = df_h3.groupby("custcare_group", observed=False).agg(
        total_customers=("churn", "count"),
        churn_rate=("churn", "mean")
    ).reset_index()
    h3_stats["churn_pct"] = h3_stats["churn_rate"] * 100
    
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
    plt.savefig(figures_dir / "fig5_h3_service_friction_custcare_drops.png", dpi=300, bbox_inches="tight")
    plt.close()

    # -------------------------------------------------------------------------
    # FIGURE 6: Clean Hypothesis H4 (actvsubs)
    # -------------------------------------------------------------------------
    df_h4 = df.copy()
    df_h4["subs_tier"] = np.where(df_h4["actvsubs"] == 1, "1 Line (Single)",
                         np.where(df_h4["actvsubs"] == 2, "2 Lines (Pair)", ">= 3 Lines (Family)"))
    order_tiers = ["1 Line (Single)", "2 Lines (Pair)", ">= 3 Lines (Family)"]
    h4_stats = df_h4.groupby("subs_tier", observed=False).agg(
        total_customers=("churn", "count"),
        churn_rate=("churn", "mean")
    ).reindex(order_tiers).reset_index()
    h4_stats["churn_pct"] = h4_stats["churn_rate"] * 100
    
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    bars = ax.bar(h4_stats["subs_tier"], h4_stats["churn_pct"], 
                  color=["#e7298a", "#7570b3", "#1b9e77"], edgecolor="black", width=0.48)
    for bar, pct, count in zip(bars, h4_stats["churn_pct"], h4_stats["total_customers"]):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, 
                f"{pct:.1f}%\n(n={count:,})", ha="center", va="bottom", fontsize=9.5, fontweight="bold")
    ax.axhline(49.56, color="black", linestyle=":", linewidth=1.2, label="Sample Baseline (49.56%)")
    ax.set_ylim(0, 60)
    ax.set_title("Figure 6: Churn Rate by Active Lines per Household", pad=14)
    ax.set_ylabel("Observed Churn Rate (%)")
    ax.legend(loc="upper right")
    plt.tight_layout()
    plt.savefig(figures_dir / "fig6_h4_household_stickiness_actvsubs.png", dpi=300)
    plt.close()

    # -------------------------------------------------------------------------
    # FIGURE 7: Clean Value at Risk (ARPU Quintiles)
    # -------------------------------------------------------------------------
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
    plt.savefig(figures_dir / "fig7_revenue_segmentation_value_at_risk.png", dpi=300, bbox_inches="tight")
    plt.close()

    # -------------------------------------------------------------------------
    # FIGURE 8: Clean Correlation Matrix
    # -------------------------------------------------------------------------
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
    plt.savefig(figures_dir / "fig8_correlation_matrix_key_drivers.png", dpi=300)
    plt.close()
    
    print("All 8 clean, clutter-free figures generated successfully!")

if __name__ == "__main__":
    run_clean_eda_figures()
