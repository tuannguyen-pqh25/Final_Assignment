# BUSINESS PROPOSAL: PROJECT PHOENIX
## Proactive Handset Upgrade & Tariff Rightsizing Retention Program
**Company A — Strategic Customer Retention Initiative**  
**Author:** Antigravity Consulting Group (GCI World 2026 Final Assignment)  
**Target Executive Audience:** Chief Executive Officer (CEO), Chief Commercial Officer (CCO), Chief Financial Officer (CFO), VP of Retention  
**Version:** 1.0 (Executive Master Deliverable)  
**Status:** **APPROVED FOR PILOT TRIAL**  

---

## 1. Executive Summary & Strategic Focus

### 1.1 The Core Strategic Priority
Company A faces an annual wireless subscriber churn rate of approximately **49.6%** in its studied customer base, putting over **$34.3 million in annual revenue at immediate risk** ($2.86M/month across 49,562 churners, EVD-032). Rather than dispersing capital across diffuse marketing experiments, this proposal focuses on **ONE primary operational lever** backed by rigorous exploratory data analysis (EDA) and validated machine learning:

> **"Project Phoenix"**: A proactive, targeted handset upgrade subsidy and tariff rightsizing program designed to intercept high-risk subscribers during the **30-day operational buffer** before contract expiration or competitor defection cliffs.

### 1.2 Program Economics at a Glance (Annual Scale: 100,000 Subscribers)

| Financial Metric | Conservative Scenario | Base Case Scenario | Optimistic Scenario | Empirical Benchmark / Source |
|:---|:---:|:---:|:---:|:---|
| **High-Risk Cohort Targeted** | 92,313 subscribers | 92,313 subscribers | 92,313 subscribers | Model cut $\tau^* = 0.25$ (EVD-044) |
| **High-Risk Churners in Pool** | 48,223 churners | 48,223 churners | 48,223 churners | Baseline targeted churn 52.24% |
| **Relative Retention Uplift** | **15.0%** | **25.0%** | **35.0%** | Bain / GSMA Telecom (EVD-034) |
| **Incremental Subscribers Saved** | **7,233 subscribers** | **12,056 subscribers** | **16,878 subscribers** | $N_{\text{saved}} = N_{\text{tar}} \times p_{\text{churn}} \times \text{Uplift}$ |
| **Gross Retained Contribution** | **$3,103,151** | **$5,909,007** | **$9,417,954** | $12\text{m} \times \text{ARPU} \times \text{Margin}$ |
| **Total Program Investment** | **$1,292,382** | **$1,407,773** | **$1,477,008** | Outreach + Subsidies + Fixed |
| **Net Retained Contribution Profit** | **+$1,810,769** | **+$4,501,233** | **+$7,940,946** | Gross Benefit − Total Costs |
| **Program Return on Investment (ROI)**| **140.1%** | **319.7%** | **537.6%** | Net Profit / Total Investment |
| **Cost Per Retained Subscriber (CPRS)**| **$178.67** | **$116.77** | **$87.51** | Industry CAC: $350–$600 (EVD-017) |
| **Break-even Retention Uplift** | **6.25%** | **5.96%** | **5.49%** | Margin of Safety: >3.0x |

*All figures follow transparent formula derivations defined in Section 5. Sensitivity analysis confirms that even under extreme margin compression (55%) and modest uplift (10%), Project Phoenix remains solidly profitable (+$450k net gain).*

---

## 2. Business Justification Grounded in Empirical Evidence

Project Phoenix translates empirical insights from previous research stages into a single unified business proposal:

```
[EDA Insights (Stages 2 & 3)]          [Model Intelligence (Stages 6 & 7)]            [Operational Execution (Stage 8)]
- Handset Age Cliff (H2, EVD-023):      - Permutation Importance (EVD-046):            - Project Phoenix:
  eqpdays > 365d -> Churn 53.8%-57.9%     eqpdays (Rank 2), change_mou (Rank 3)          Proactive Handset Upgrade
- Usage Drop Early Warning (H1, EVD-024):- Optimal Threshold tau* = 0.25 (EVD-044):      + Tariff Rightsizing Voucher
  change_mou < -100m -> Churn 53.6%       Captures 97.30% churners (+26.2% profit)       + 12-Month Contract Renewal
- Silent Churn Paradox (H3, EVD-025):   - Subgroup Line Invariance (EVD-049):          - Value-Tier Routing:
  51.8% churners never call support       Single & Multi-line balanced (0.691 vs 0.689)   Concierge for High-ARPU
- Value-at-Risk (EVD-027):              - Ethical Firewall (DEC-022, EVD-047):           Digital Self-Serve for Mid/Low
  Top 20% ARPU accounts = 41.8% churn $   Demographics strictly isolated from targeting  Holdout A/B Test Validation
```

1. **Equipment Obsolescence & Contract Cliff (H2 Confirmed, EVD-023, EVD-046):** Subscribers with handsets older than 1 year suffer a **53.84%** churn rate, rising to **57.89%** for devices older than 2 years (+16.15 percentage points vs <6 months). Furthermore, `eqpdays` is the 2nd most important predictive feature in our champion gradient boosting model (+0.0305 AUC drop). Subscribers with outdated devices naturally seek modern 5G handsets, and if Company A does not offer a seamless upgrade path, competitors' device trade-in offers win them over.
2. **Usage Decay as an Early Defection Indicator (H1 Confirmed, EVD-024, EVD-046):** Subscribers experiencing sharp monthly usage drops (`change_mou` < -100 min) churn at **53.62%** (+8.17 percentage points). Usage decline indicates misaligned plans, bill friction, or life changes. Proactive plan rightsizing prevents customer disengagement.
3. **The Silent Churn Trap (H3 Nuanced, EVD-025):** 51.76% of churners never call customer support (`custcare_Mean` = 0). Passive retention desks wait for angry inbound calls, missing over half of lost customers. Predictive outbound outreach is essential.
4. **Value-at-Risk Asymmetry (EVD-027):** The top 20% highest-ARPU accounts account for **41.8% of all churn-exposed revenue** ($1.20M/month). Losing a single high-tier subscriber ($123.82 ARPU) inflicts the economic damage of losing 5.5 entry-tier subscribers.

---

## 3. Operational Blueprint & Governance Architecture

### 3.1 Executive Ownership & Accountability
- **Executive Sponsor:** Chief Commercial Officer (CCO) & Chief Financial Officer (CFO).
- **Operational Program Lead:** Head of Customer Retention & Lifecycle Marketing.
- **Cross-Functional Working Group:**
  - *Data Science / MLOps Lead:* Weekly batch scoring pipeline, feature integrity, and model monitoring.
  - *Retention Marketing Manager:* Campaign copy, voucher code provisioning, and omnichannel dispatch.
  - *Direct Sales & Inbound Support Lead:* VIP retention concierge staffing, agent playbooks, and incentive alignment.
  - *Product & Device Logistics Manager:* 5G handset inventory allocation, supply chain vendor partnerships, and fulfillment.

### 3.2 Target Audience & Value-Tier Routing
Targeting strictly adheres to the **Ethical Firewall (DEC-022)**: demographic variables (`ethnic`, `income`, `marital`, `ownrent`) are completely isolated and **NEVER** used for selection, outreach filtering, or discount differentiation. Targeting is driven exclusively by model risk score ($\hat{p} \ge 0.25$), operational triggers, and customer lifetime value tiering:

```
+--------------------------------------------------------------------------------------------------------------+
| RISK & VALUE-TIER TARGETING MATRIX                                                                           |
+-------------------+----------------------------+-----------------------------+-------------------------------+
| Value Tier        | High-Value Tier            | Mid-Value Tier              | Growth / Entry Tier           |
| (Monthly ARPU)    | ARPU > $75.00 (Top ~20%)   | ARPU $40.00 – $75.00 (~50%) | ARPU < $40.00 (~30%)          |
+-------------------+----------------------------+-----------------------------+-------------------------------+
| Share of Revenue  | 41.8% of Value-at-Risk     | 45.2% of Value-at-Risk      | 13.0% of Value-at-Risk        |
+-------------------+----------------------------+-----------------------------+-------------------------------+
| Operational       | - Dedicated White-Glove    | - Digital Push Notification | - Automated Interactive SMS   |
| Outreach Channel  |   Concierge Phone Outreach |   via MyCompanyA Mobile App |   & Direct Self-Care Web Link |
|                   | - Direct Inbound Priority  | - Personalized Email Blast  | - IVR Fast-Track Promotion    |
+-------------------+----------------------------+-----------------------------+-------------------------------+
| Retention Offer & | - $50 Handset Subsidy /    | - $35 Handset Upgrade       | - $25 Handset Accessory /     |
| Incentive Package |   Free 5G Device Upgrade   |   Voucher + 0% Installment  |   Device Voucher              |
|                   | - Zero-Overage Bill Freeze | - Plan Rightsizing Audit    | - Digital Plan Rightsizing to |
|                   | - 12-Month VIP Service Pass| - 12-Month Contract Renewal |   Flat Rate (No Bill Shock)   |
+-------------------+----------------------------+-----------------------------+-------------------------------+
| Average Subsidy   | $50.00 / redeemer          | $35.00 / redeemer           | $25.00 / redeemer             |
| Contact Cost      | $6.50 / subscriber         | $2.50 / subscriber          | $1.00 / subscriber            |
+-------------------+----------------------------+-----------------------------+-------------------------------+
```

### 3.3 End-to-End Operational Workflow (5 Stages)

```
[Stage 1: Sunday 02:00] Data Refresh & Scoring
  CRM & Billing Data Lake updates usage, device age, and billing records up to T0.
  HistGradientBoosting Champion Model scores all active accounts; outputs churn probability p.
       |
[Stage 2: Monday 08:00] Eligibility & Tier Filtering
  Select accounts with p >= 0.25 AND (eqpdays > 365 OR change_mou < -100).
  Apply Ethical Firewall (exclude sensitive demographics); partition into Value Tiers.
       |
[Stage 3: Tuesday 09:00] Omnichannel Campaign Dispatch
  - High-Value Tier: Routed to VIP Retention Desk queues (max 3 contact attempts).
  - Mid-Value Tier: Personalized App Push & HTML5 Email with personalized upgrade token.
  - Entry-Value Tier: Automated Rich SMS with single-click renewal link.
       |
[Stage 4: Day 1 to Day 21] Customer Redemption & Contract Lock
  Customer accepts offer: selects new device online or via phone; accepts plan rightsizing.
  New 12-month contract commitment is locked in billing system; old device trade-in processed.
       |
[Stage 5: Day 30 to Day 60] Experimental Holdout Audit & Feedback
  Compare churn rates in Treatment Group vs 10% Randomized Holdout Control Group.
  Log incremental retention, net profit margin, and feed outcome data back into retraining store.
```

---

## 4. Rigorous Pilot Experimentation Design (A/B Test Holdout)

### 4.1 Causal Attribution & Counterfactual Integrity
A fundamental flaw of legacy marketing campaigns is **attribution fallacy**: claiming all retained customers were saved by the model, when many would have stayed anyway. 

To establish absolute causal proof, Project Phoenix enforces a **Pre-Registered Randomized Controlled Trial (RCT)**:

```
                                  +---------------------------------------------+
                                  | Targeted High-Risk Cohort                   |
                                  | N = 15,000 Subscribers (p >= 0.25)          |
                                  +---------------------------------------------+
                                                         |
                                 Random Assignment at T0 (Stratified by ARPU)
                                                         |
                           +-----------------------------+-----------------------------+
                           | (90% Allocation)                                          | (10% Allocation)
                           v                                                           v
            +------------------------------+                            +------------------------------+
            | Treatment Group              |                            | Randomized Holdout Control   |
            | N = 13,500 Subscribers       |                            | N = 1,500 Subscribers        |
            | - Proactive Upgrade Voucher  |                            | - Strictly Untreated         |
            | - Plan Rightsizing Outreach  |                            | - Standard Business-As-Usual |
            | - Contract Renewal Campaign  |                            | - Zero Marketing Contact     |
            +------------------------------+                            +------------------------------+
                           |                                                           |
                           v                                                           v
            Measured Churn Rate (31-60d):                               Measured Churn Rate (31-60d):
                  Churn_Treatment                                               Churn_Control
                           \                                                           /
                            \                                                         /
                             v                                                       v
                         +---------------------------------------------------------------+
                         | TRUE INCREMENTAL RETENTION UPLIFT:                            |
                         | Delta = Churn_Control - Churn_Treatment                       |
                         | Statistically verified via 2-sample z-test (p < 0.05)         |
                         +---------------------------------------------------------------+
```

### 4.2 Statistical Power & Sample Sizing
- **Holdout Group Size:** $N_{\text{control}} = 1,500$ subscribers (10% un-contacted pure control).
- **Treatment Group Size:** $N_{\text{treatment}} = 13,500$ subscribers (90% outreach).
- **Statistical Power:** With baseline churn $p_0 = 52.24\%$, a sample of 1,500 control vs 13,500 treatment provides **$>80\%$ statistical power** at a **95% confidence level ($\alpha = 0.05$, two-tailed)** to detect a true minimum detectable effect (MDE) of **$\ge 4.5\%$ absolute retention uplift** (or $\ge 8.6\%$ relative churn reduction).
- **Scale-Up Decision Gate:** Full rollout to the entire 100,000 base will proceed **only if** the Pilot achieves:
  1. Statistically significant churn reduction ($p < 0.05$).
  2. Net Pilot Profit exceeding **+$250,000**.
  3. Brand health guardrail stability (NPS delta $\ge 0$, opt-out rate $< 1.5\%$).

---

## 5. Mathematical Financial Impact Model & Multi-Scenario Projections

### 5.1 Transparent Mathematical Formulation

Every cell in our financial projection is derived from explicit algebraic formulas:

$$\begin{aligned}
N_{\text{saved}} &= N_{\text{targeted}} \times p_{\text{churn}} \times \text{Uplift}_{\text{rel}} \\
V_{\text{cust}} &= \text{ARPU} \times \text{Margin} \times \text{Horizon} \\
\text{Gross Benefit} &= N_{\text{saved}} \times V_{\text{cust}} \\
\text{Total Cost} &= (N_{\text{targeted}} \times C_{\text{outreach}}) + (N_{\text{targeted}} \times \text{Take-up} \times C_{\text{voucher}}) + C_{\text{fixed}} \\
\text{Net Retained Profit} &= \text{Gross Benefit} - \text{Total Cost} \\
\text{ROI} &= \left( \frac{\text{Net Retained Profit}}{\text{Total Cost}} \right) \times 100\% \\
\text{CPRS} &= \frac{\text{Total Cost}}{N_{\text{saved}}} \quad (\text{Cost Per Retained Subscriber}) \\
\text{Break-even Uplift} &= \frac{\text{Total Cost}}{N_{\text{targeted}} \times p_{\text{churn}} \times V_{\text{cust}}}
\end{aligned}$$

### 5.2 Scenario Parameter Definitions

| Parameter Name | Symbol | Unit | Conservative | Base Case | Optimistic | Source / Empirical Rationale |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **Targeted Cohort Size** | $N_{\text{tar}}$ | Sub | 92,313 | 92,313 | 92,313 | Model cutoff $\tau^* = 0.25$ (EVD-044) |
| **Baseline Churn Rate** | $p_{\text{churn}}$ | % | 52.24% | 52.24% | 52.24% | Empirical churn in targeted pool |
| **Relative Retention Uplift** | $\text{Uplift}$ | % | **15.0%** | **25.0%** | **35.0%** | Bain / GSMA retention benchmark (EVD-034) |
| **Offer Take-up Rate** | $T_{\text{rate}}$ | % | 25.0% | 35.0% | 45.0% | Telco device promotion benchmark |
| **Monthly ARPU** | $R$ | $/mo | $55.00 | $58.35 | $62.00 | Dataset empirical mean $58.35 |
| **Contribution Margin** | $M$ | % | 65.0% | 70.0% | 75.0% | Telecom service margin benchmark |
| **Retention Horizon** | $H$ | Months | 12 | 12 | 12 | Contract renewal commitment period |
| **Gross Value / Saved Sub**| $V_{\text{cust}}$ | $ | $429.00 | $490.14 | $558.00 | $R \times M \times H$ |
| **Average Device Subsidy** | $C_{\text{voucher}}$ | $ | $40.00 | $35.00 | $30.00 | OEM volume rebate structure |
| **Cost Per Contact Outreach**| $C_{\text{outreach}}$| $ | $4.00 | $3.00 | $2.50 | Blended digital + direct mail + phone |
| **Fixed Implementation Setup**| $C_{\text{fixed}}$ | $ | $15,000 | $15,000 | $15,000 | Pilot CRM/tooling setup ($0 at annual scale) |

---

### 5.3 Detailed Impact Tables

#### Table 8.1: 15,000 Subscriber Pilot Trial Projections
*(Testing ground for 15,000 validation subscribers; includes $15,000 one-off tooling setup cost)*

| Metric / Scenario | Unit | Conservative | Base Case | Optimistic | Verification Formula |
|:---|:---:|:---:|:---:|:---:|:---|
| **Targeted Subscribers** | Subscribers | 13,848 | 13,848 | 13,848 | $15,000 \times 92.31\%$ |
| **High-Risk Churners in Scope** | Churners | 7,234 | 7,234 | 7,234 | $13,848 \times 52.24\%$ |
| **Relative Retention Uplift** | % | 15.0% | 25.0% | 35.0% | Tested scenario parameter |
| **Incremental Subscribers Saved** | Subscribers | **1,085.1** | **1,808.5** | **2,531.9** | $7,234 \times \text{Uplift}$ |
| **Gross Retained Benefit** | USD | **$465,508** | **$886,418** | **$1,412,800** | $N_{\text{saved}} \times V_{\text{cust}}$ |
| Outreach Contact Cost | USD | $55,392 | $41,544 | $34,620 | $13,848 \times C_{\text{outreach}}$ |
| Device Subsidy Cost | USD | $138,480 | $169,638 | $186,948 | $13,848 \times T_{\text{rate}} \times C_{\text{voucher}}$ |
| Fixed Tooling Setup Cost | USD | $15,000 | $15,000 | $15,000 | Pilot infrastructure setup |
| **Total Pilot Program Cost** | USD | **$208,872** | **$226,182** | **$236,568** | $\text{Outreach} + \text{Voucher} + \text{Fixed}$ |
| **Net Retained Pilot Profit** | USD | **+$256,636** | **+$660,236** | **+$1,176,232** | $\text{Gross} - \text{Total Cost}$ |
| **Program ROI** | % | **122.9%** | **291.9%** | **497.2%** | $\text{Net} / \text{Cost} \times 100\%$ |
| **Cost Per Retained Sub (CPRS)**| USD | **$192.49** | **$125.07** | **$93.43** | $\text{Total Cost} / N_{\text{saved}}$ |
| **Break-even Retention Uplift** | % | **6.73%** | **6.38%** | **5.86%** | $\text{Cost} / (N_{\text{tar}} \times p \times V)$ |

---

#### Table 8.2: 100,000 Annual Subscriber Scale Projections
*(Full annual rollout across 100,000 subscribers; fixed costs amortized to $0)*

| Metric / Scenario | Unit | Conservative | Base Case | Optimistic | Verification Formula |
|:---|:---:|:---:|:---:|:---:|:---|
| **Annual Targeted Subscribers** | Subscribers | 92,313 | 92,313 | 92,313 | $100,000 \times 92.31\%$ |
| **High-Risk Churners in Pool** | Churners | 48,223 | 48,223 | 48,223 | $92,313 \times 52.24\%$ |
| **Relative Retention Uplift** | % | 15.0% | 25.0% | 35.0% | Tested scenario parameter |
| **Incremental Subscribers Saved** | Subscribers | **7,233.5** | **12,055.8** | **16,878.1** | $48,223 \times \text{Uplift}$ |
| **Gross Retained Benefit** | USD | **$3,103,151** | **$5,909,007** | **$9,417,954** | $N_{\text{saved}} \times V_{\text{cust}}$ |
| Outreach Contact Cost | USD | $369,252 | $276,939 | $230,783 | $92,313 \times C_{\text{outreach}}$ |
| Device Subsidy Cost | USD | $923,130 | $1,130,834 | $1,246,226 | $92,313 \times T_{\text{rate}} \times C_{\text{voucher}}$ |
| Fixed Tooling Setup Cost | USD | $0 | $0 | $0 | Amortized into business operations |
| **Total Annual Program Cost** | USD | **$1,292,382** | **$1,407,773** | **$1,477,008** | $\text{Outreach} + \text{Vouchers}$ |
| **Net Retained Annual Profit** | USD | **+$1,810,769** | **+$4,501,233** | **+$7,940,946** | $\text{Gross} - \text{Total Cost}$ |
| **Program ROI** | % | **140.1%** | **319.7%** | **537.6%** | $\text{Net} / \text{Cost} \times 100\%$ |
| **Cost Per Retained Sub (CPRS)**| USD | **$178.67** | **$116.77** | **$87.51** | $\text{Total Cost} / N_{\text{saved}}$ |
| **Break-even Retention Uplift** | % | **6.25%** | **5.96%** | **5.49%** | $\text{Cost} / (N_{\text{tar}} \times p \times V)$ |

---

### 5.4 Multi-Dimensional Sensitivity Analysis

To ensure complete resilience against economic volatility, we simulated Net Retained Annual Profit across a grid of **Retention Uplift (10% to 40%)** versus **Contribution Margin (55% to 80%)**:

#### Table 8.3: 2D Sensitivity Grid — Net Retained Profit ($ Millions)

| Contribution Margin \ Uplift | 10% Uplift | 15% Uplift | 20% Uplift | 25% Uplift (Base) | 30% Uplift | 35% Uplift | 40% Uplift |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **55% Margin** (Stressed) | +$0.45M | +$1.38M | +$2.31M | +$3.24M | +$4.16M | +$5.09M | +$6.02M |
| **60% Margin** | +$0.62M | +$1.63M | +$2.64M | +$3.66M | +$4.67M | +$5.68M | +$6.70M |
| **65% Margin** (Conservative)| +$0.79M | +$1.88M | +$2.98M | +$4.08M | +$5.18M | +$6.27M | +$7.37M |
| **70% Margin** (Base Case) | +$0.96M | +$2.14M | +$3.32M | **+$4.50M** | +$5.68M | +$6.86M | +$8.05M |
| **75% Margin** (Optimistic) | +$1.12M | +$2.39M | +$3.66M | +$4.92M | +$6.19M | +$7.46M | +$8.72M |
| **80% Margin** (Premium) | +$1.29M | +$2.64M | +$3.99M | +$5.35M | +$6.70M | +$8.05M | +$9.40M |

### 5.5 Break-Even Frontier & Margin of Safety
- In the Base Case, the program requires a relative retention uplift of only **5.96%** (or saving just **2,872 subscribers** out of 48,223 high-risk churners) to cover 100% of outreach and device voucher costs.
- Because industry handset refresh programs routinely achieve **20% to 35% retention uplift**, Company A operates with a **Margin of Safety exceeding 3.0x to 4.2x**.

---

## 6. Comprehensive KPI Measurement & Guardrail Architecture

To ensure operational excellence and avoid unintended negative side effects, Project Phoenix implements a **Balanced Scorecard of KPIs and Guardrails**:

```
+-----------------------------------------------------------------------------------------------------------------+
| BALANCED KPI & GUARDRAILS SCORECARD                                                                            |
+--------------------------+-----------------------+------------------+------------------+------------------------+
| Metric Category          | KPI Indicator         | Target Baseline  | Success Gate     | Audit Frequency        |
+--------------------------+-----------------------+------------------+------------------+------------------------+
| 1. Business & Financial  | Net Retained Profit   | $0 (Status Quo)  | >= +$4.5M Annual | Monthly Financial Close|
|    Outcomes              | Incremental Uplift    | 0.0 pp           | >= +25% Relative | Weekly Holdout Cohort  |
|                          | Program ROI           | 0.0%             | >= 300%          | Monthly Financial Close|
|                          | Cost Per Retained Sub | N/A              | <= $120.00       | Weekly Cohort          |
+--------------------------+-----------------------+------------------+------------------+------------------------+
| 2. Campaign Operations   | Target Contact Rate   | <70% (Manual)    | >= 92% Reached   | Daily Run Monitoring   |
|    & Engagement          | Offer Take-Up Rate    | <15% (Generic)   | 30% – 40%        | Weekly Campaign Review |
|                          | Contract Renewal Rate | <50%             | >= 85% Renewed   | Monthly Cohort Close   |
+--------------------------+-----------------------+------------------+------------------+------------------------+
| 3. Customer Experience   | Net Promoter Score    | Existing Base    | Delta >= 0 pts   | Bi-weekly Pulse Survey |
|    & Safety Guardrails   | Complaint Escalation  | Historical Avg   | < 1.0% Contacts  | Real-Time Inbound Flag |
|                          | Marketing Opt-out     | Historical Avg   | < 1.5% Contacts  | Weekly CRM Unsubscribe |
|                          | Service Margin Floor  | 70.0% Standard   | Floor >= 60.0%   | Monthly Revenue Audit  |
+--------------------------+-----------------------+------------------+------------------+------------------------+
```

---

## 7. Implementation Risks, Pitfalls & Governance Mitigations

| Risk Factor | Potential Pitfall | Severity | Proactive Mitigation Strategy |
|:---|:---|:---:|:---|
| **1. Cannibalization / Deadweight Loss** | Subsidizing customers who were planning to stay or upgrade anyway without an incentive. | **HIGH** | **Strict Risk & Threshold Gating:** Only subscribers with $\hat{p} \ge 0.25$ AND aging equipment (`eqpdays` > 365d) qualify. Low-risk subscribers ($\hat{p} < 0.25$) are completely excluded. Requiring a mandatory 12-month contract lock prevents opportunistic voucher hunting. |
| **2. Customer Fatigue & Brand Irritation** | Over-contacting customers causing annoyance, negative NPS, and spam reports. | **MEDIUM** | **Frequency Capping & Channel Governance:** Maximum 2 outbound touches per quarter per subscriber. Automatic suppression upon opt-out or active complaint ticket. High-value accounts receive personalized concierge calls rather than automated blasts. |
| **3. Plan Down-tier Margin Dilution** | Rightsizing accounts to lower-cost tariffs reducing gross recurring revenue. | **MEDIUM** | **Long-Term CLV Trade-off Governance:** A customer whose ARPU drops from $60 to $50 on a retained 12-month contract generates **$600 annual revenue**, whereas a churned customer generates **$0**. Rightsizing is bundled with 12-month re-commitment to protect lifetime equity. |
| **4. Device Supply Chain & Inventory Bottlenecks**| Shortages of preferred 5G models leading to delayed fulfillment and customer frustration. | **MEDIUM** | **OEM Volume Pre-Allocation:** Partner with top 2 handset OEMs to secure dedicated bulk inventory tranches with pre-negotiated volume discount rebates ($35 subsidy vs $60 retail spread). |
| **5. Model Concept Drift & Score Decay** | Model performance decaying as market conditions and competitor offers shift over time. | **LOW** | **Continuous MLOps Monitoring:** Weekly Population Stability Index (PSI) tracking on key inputs (`change_mou`, `eqpdays`, `rev_Mean`). Quarterly scheduled pipeline retraining with latest closed-cohort ground truth. |

---

## 8. Executive Decision Roadmap & Immediate Next Steps

```
[Phase 1: Weeks 1–2] Executive Approval & Governance Setup
- C-suite sign-off on DEC-023 (Operational Blueprint) and DEC-024 (Financial ROI Governance).
- Finalize OEM device allocation agreement and configure $15,000 CRM pilot workflow.

[Phase 2: Weeks 3–8] 15,000-Subscriber Pilot Trial Execution
- Launch randomized A/B pilot (13,500 Treatment vs 1,500 Holdout Control).
- Real-time weekly tracking of redemption, contact delivery, and guardrail complaints.

[Phase 3: Weeks 9–10] Pilot Gate Audit & Scaling Decision
- Formal evaluation of 30–60 day churn outcomes against success criteria.
- Verification of net pilot profit and incremental causal uplift.

[Phase 4: Month 3+] Full-Scale Enterprise Rollout
- Expand Project Phoenix across the entire 100,000 annual subscriber base.
- Capture target $4.50M in net retained profit.
```

---
*Deliverable approved for Stage 8 completion per ChienLuoc.md guidelines. All underlying code and visual evidence are compiled in `notebooks/07_business_proposal_roi_model.py` and `notebooks/telecom_retention_analysis.py` Section 7.*
