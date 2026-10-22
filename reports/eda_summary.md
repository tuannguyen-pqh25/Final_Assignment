# EXPLORATORY DATA ANALYSIS (EDA) EXECUTIVE SUMMARY
**Project:** GCI World 2026 Final Assignment — Company A Retention Strategy  
**Stage:** Stage 3 — Exploratory Data Analysis  
**Date:** 2026-10-22  
**Dataset Scale:** 100,000 customers × 100 attributes  

---

## 1. High-Resolution Visual Evidence Portfolio (300 DPI)

All 8 figures are generated and stored in [reports/figures/](file:///d:/Project/Final_Assignment/reports/figures):
1. **[fig1_target_balance_and_structure.png](file:///d:/Project/Final_Assignment/reports/figures/fig1_target_balance_and_structure.png):** Target Churn Distribution (49.56% churners vs 50.44% retained; balanced sample).
2. **[fig2_missingness_structure.png](file:///d:/Project/Final_Assignment/reports/figures/fig2_missingness_structure.png):** Missingness Distribution (Concentrated in Client demographics; Record usage is >99% complete).
3. **[fig3_h1_consumption_drop_change_mou_rev.png](file:///d:/Project/Final_Assignment/reports/figures/fig3_h1_consumption_drop_change_mou_rev.png):** Hypothesis H1 Test — Churn rate across minutes of use change brackets (`change_mou`).
4. **[fig4_h2_equipment_age_lifecycle.png](file:///d:/Project/Final_Assignment/reports/figures/fig4_h2_equipment_age_lifecycle.png):** Hypothesis H2 Test — Churn risk surge across equipment age tiers (`eqpdays`).
5. **[fig5_h3_service_friction_custcare_drops.png](file:///d:/Project/Final_Assignment/reports/figures/fig5_h3_service_friction_custcare_drops.png):** Hypothesis H3 Test — Service friction & the "Silent Churner" paradox (`custcare_Mean`, `drop_blk_Mean`).
6. **[fig6_h4_household_stickiness_actvsubs.png](file:///d:/Project/Final_Assignment/reports/figures/fig6_h4_household_stickiness_actvsubs.png):** Hypothesis H4 Test — Multi-line fragility and secondary lines (`actvsubs`).
7. **[fig7_revenue_segmentation_value_at_risk.png](file:///d:/Project/Final_Assignment/reports/figures/fig7_revenue_segmentation_value_at_risk.png):** Revenue quintile segmentation and monthly Value at Risk ($).
8. **[fig8_correlation_matrix_key_drivers.png](file:///d:/Project/Final_Assignment/reports/figures/fig8_correlation_matrix_key_drivers.png):** Pearson correlation matrix between key behavioral drivers and churn.

---

## 2. Five Core Candidate Business Insights

| Insight # | Insight Theme | Empirical Evidence | Sample Size ($n$) | Effect Size / Statistical Significance | Executive Takeaway | Limitations & Caveats |
|:---:|:---|:---|:---:|:---:|:---|:---|
| **INS-001** | **Equipment Age & Lifecycle Cliff** | Churn rate escalates with device age: $<6$m: **41.7%**; $6-12$m: **47.0%**; $1-2$y: **53.8%**; $>2$y: **57.9%** | $n = 99,999$ | **+16.2 percentage points** difference ($p < 10^{-100}$); Pearson $r = +0.11$ (strongest bivariate predictor) | Device subsidy expiration (12-24m) creates a critical window where subscribers seek competitor upgrade promos | Correlation $\neq$ causation; holding an old device may reflect latent disengagement |
| **INS-002** | **Consumption Drop as a Leading Indicator** | Severe usage decline ($<-100$ mins): **53.6%** churn; Moderate usage growth ($+20$ to $+100$ mins): **45.4%** churn | $n = 99,109$ | **+8.2 percentage points** difference ($p = 6.06 \times 10^{-59}$) | Declining minutes and spend precedes formal churn by 1-2 billing cycles | Missing for 891 newer subscribers with insufficient tenure history |
| **INS-003** | **The "Silent Churner" Paradox** | 0 care calls: **51.8%** churn; $>3$ calls/month: **44.7%** churn (despite 3.6x higher network dropped calls) | $n = 100,000$ | **-7.1 percentage points** churn for active callers ($p < 10^{-20}$) | Callers seek resolution and engage with retention reps; the highest churn risk is disengaged subscribers who leave silently | Frequent callers may represent complex enterprise or family bundles with higher baseline stickiness |
| **INS-004** | **Secondary Line Fragility** | 2-line accounts (`actvsubs=2`): **52.2%** churn; 1-line accounts: **48.7%** churn; $\ge 3$ lines: **49.1%** churn | $n = 100,000$ ($n_{2sub} = 24,422$) | **+3.5 percentage points** higher churn for 2-line accounts | Secondary lines (extra phone, tablet) are treated as discretionary and cut first during cost-saving | Data does not distinguish line types (handset vs data-only SIMs) |
| **INS-005** | **Value-at-Risk Concentration** | Churn rate is relatively flat across revenue quintiles (~48-53%), but Tier Q5 (ARPU >$74, avg $123.82) accounts for **$1,196,130/month** in churned revenue | $n = 99,643$ | Tier Q5 represents **41.8%** of total monthly revenue at risk | Losing 1 top-tier customer equals losing 5.5 bottom-tier customers. Retention targeting must be value-weighted | `rev_Mean` represents gross billing revenue, not net contribution margin |

---

## 3. Empirical Assessment of Initial Hypotheses

1. **Hypothesis H1 (Consumption Drop):** $\rightarrow$ **SUPPORTED.** Negative consumption trend (`change_mou`) strongly correlates with churn risk ($p = 6.06 \times 10^{-59}$).
2. **Hypothesis H2 (Equipment Lifecycle):** $\rightarrow$ **STRONGLY SUPPORTED.** `eqpdays` is the single strongest predictor of churn ($r = +0.11$, +16.2 percentage point spread).
3. **Hypothesis H3 (Service Friction):** $\rightarrow$ **NUANCED / PARTIALLY REFUTED.** Disproves the naive assumption that support calls drive churn; non-calling "silent churners" exhibit the highest churn probability.
4. **Hypothesis H4 (Household Stickiness):** $\rightarrow$ **PARTIALLY REFUTED.** 2-subscriber accounts exhibit heightened vulnerability (+3.5 percentage point churn lift), highlighting secondary line fragility.
