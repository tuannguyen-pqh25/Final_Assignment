# FEATURE ENGINEERING & PREPROCESSING DECISIONS — GCI WORLD 2026 FINAL ASSIGNMENT
**Document Reference:** `reports/feature_decisions.md`  
**Dataset:** Company A (100,000 subscribers × 100 raw attributes)  
**Target Variable:** `churn` (0 = Retained, 1 = Churned within 31–60 days after $T_0$)  
**Pipeline Execution File:** [notebooks/telecom_retention_analysis.py](file:///d:/Project/Final_Assignment/notebooks/telecom_retention_analysis.py) Section 4  
**Date of Audit & Implementation:** 2026-10-23  

---

## 1. Executive Summary & Architecture Overview

In strict accordance with **Stage 5 of [ChienLuoc.md](file:///d:/Project/Final_Assignment/ChienLuoc.md)** and the technical governance rules (DEC-002, DEC-005, DEC-013, DEC-016, DEC-017), we have established a leak-free, production-grade feature engineering and preprocessing pipeline.

### Core Preprocessing Achievements:
1. **Zero Information Leakage:** All preprocessing estimators (median imputers, missing indicators, standard scalers, and one-hot encoders) are fitted strictly on `X_train` (70,000 records). Transformation on `X_val` (15,000) and `X_test` (15,000) utilizes parameters frozen from training data.
2. **Exclusion of Non-Predictive Identifiers:** `Customer_ID` is strictly quarantined and excluded from $X$.
3. **Preservation of Missingness Signals (MNAR):** Rather than arbitrarily deleting the 6 columns with >30% missing values, we introduced `MissingIndicator` flags for numerical variables and an explicit `'Missing'` category for categorical variables. Empirical ablation proves this strategy yields a **+0.0051 ROC-AUC lift (+0.51%)** over the drop baseline.
4. **Business-Grounded Feature Engineering:** 12 domain features derived from Stage 3 EDA insights (H1 Consumption Drop, H2 Handset Contract Cliff, H3 Silent Churners, H4 Multi-Line Vulnerability, and Value-at-Risk ARPU Tiers) were engineered row-wise, yielding a further **+0.0062 ROC-AUC lift (+0.62%)** (total cumulative gain **+0.0113 ROC-AUC** on Logistic Regression).
5. **Stratified Split Integrity:** The dataset is split into 70% Train (70,000), 15% Validation (15,000), and 15% Held-out Test (15,000), preserving the exact ~49.56% churn balance across all splits. The held-out test set is locked and untouched.

---

## 2. Feature Space Partitioning & Column Taxonomy

The 100 columns of the merged dataset are partitioned into four strict functional tiers:

| Tier | Count | Column Names / Description | Treatment in Pipeline |
|:---|:---:|:---|:---|
| **Identifier** | 1 | `Customer_ID` | **Excluded from $X$**. Retained strictly in separate index series for subscriber tracking and cohort allocation. |
| **Target Variable** | 1 | `churn` | Binary ground truth label (0 = Retained, 1 = Churned). Isolated into $y$. |
| **Raw Numerical Predictors** | 77 | Usage (`mou_Mean`, `totcalls`), Billing (`rev_Mean`, `totmrc_Mean`, `ovrrev_Mean`), Trend (`change_mou`, `change_rev`), Handset age (`eqpdays`), Account tenure (`months`), Care (`custcare_Mean`), Network friction (`drop_blk_Mean`), Demographics (`income`, `adults`, `lor`, `numbcars`, `truck`, `rv`, `forgntvl`). | Median imputation with `add_indicator=True` + `StandardScaler()`. `eqpdays` clipped at $\ge 0$. |
| **Raw Categorical Predictors** | 21 | Credit class (`crclscod`), Geography (`area`), Demographic profiles (`prizm_social_one`, `ethnic`, `marital`, `dwllsize`, `dwlltype`, `ownrent`, `HHstatin`), Device & Plan flags (`new_cell`, `asl_flag`, `dualband`, `refurb_new`, `hnd_webcap`, `infobase`, `kid0_2`, `kid3_5`, `kid6_10`, `kid11_15`, `kid16_17`, `creditcd`). | Imputation with constant string `'Missing'` + `OneHotEncoder(handle_unknown='ignore', sparse_output=False)`. |
| **Engineered Domain Features** | 12 | Row-wise transformations linking subscriber state at $T_0$ to business risk levers (see Section 4). | Added to numerical feature block for scaling and modeling. |

**Total Transformed Feature Space:** **279 dense features** after ColumnTransformer fit.

---

## 3. Missing Data Strategy & Empirical Ablation Study

### 3.1 The Missingness Dilemma in Telecom CRM
The Stage 1 data audit revealed 6 attributes with missingness exceeding 30%:
1. `numbcars` (49.37% missing) — Number of vehicles owned
2. `dwllsize` (38.31% missing) — Dwelling size code
3. `HHstatin` (37.92% missing) — Household status indicator
4. `ownrent` (33.71% missing) — Home owner vs renter
5. `dwlltype` (31.91% missing) — Dwelling type (Single vs Multi-unit)
6. `lor` (30.19% missing) — Length of residence

In telecom customer relationship management, demographic non-reporting is rarely Missing Completely At Random (MCAR). It is frequently Missing Not At Random (MNAR) or Missing At Random (MAR) conditioned on channel acquisition type (e.g., third-party dealers vs direct corporate retail) or customer privacy preferences. Deleting these features destroys this latent socio-demographic posture.

### 3.2 Controlled Ablation Benchmark
To empirically evaluate the optimal missingness treatment, we conducted a controlled benchmark using `LogisticRegression(max_iter=300, random_state=42)` evaluated on the isolated 15,000-sample Validation Set:

| Experiment / Strategy | Description | Validation ROC-AUC | PR-AUC (Average Precision) | Strategic Assessment |
|:---|:---|:---:|:---:|:---|
| **Ablation 1: Drop High-Missing (>30%)** | Dropped `numbcars`, `dwllsize`, `HHstatin`, `ownrent`, `dwlltype`, `lor`. Median impute remaining numerics without indicators. One-hot encode categoricals. | **0.6278** | **0.6135** | Sub-optimal. Deletes demographic differentiation and loses 6 predictive attributes. |
| **Ablation 2: Retain All + Missing Indicators** | Retained all 98 attributes. Numerical median imputation with `add_indicator=True` (capturing who did not disclose car/residence). Categoricals imputed with `'Missing'` token + One-hot. | **0.6329** | **0.6198** | **Superior (+0.0051 ROC-AUC gain)**. Confirms missingness pattern contains predictive signal. |
| **Ablation 3: Full Pipeline (Domain Levers + Indicators)** | All 98 raw features + 12 business engineered features + Missing Indicators + Standard Scaling. | **0.6391** | **0.6274** | **Best Performance (+0.0113 cumulative ROC-AUC gain)**. Adopted as production standard. |

**Decision (DEC-017):** Retain all high-missingness variables using dual imputation (median + missing indicator for numeric; explicit `'Missing'` category for nominal).

---

## 4. Business-Grounded Feature Engineering Specifications

All engineered features are computed **strictly row-wise** using observations available prior to $T_0$, guaranteeing zero future leakage:

| Feature Name | Category / Hypothesis | Formula / Logic | Domain Intuition & Business Rationale |
|:---|:---|:---|:---|
| `eqpdays_years` | H2 Equipment Lifecycle | $\text{eqpdays} / 365.25$ | Linearized equipment age in years for interpretable hazard modeling. |
| `eqp_over_1yr` | H2 Equipment Lifecycle | $\mathbb{I}(\text{eqpdays} \ge 365)$ | Indicator for passing standard 12-month manufacturer warranty threshold. |
| `eqp_over_2yr` | H2 Equipment Lifecycle | $\mathbb{I}(\text{eqpdays} \ge 730)$ | Handset subsidy contract cliff. Churn rate jumps to **57.89%** beyond 24 months. |
| `eqp_to_tenure_ratio` | H2 Equipment Lifecycle | $\frac{\max(\text{eqpdays}, 0)}{\max(\text{months} \times 30.4375, 1)}$ | Ratio of current device age to account tenure. Identifies subscribers still on their initial onboarding phone vs frequent upgraders. |
| `severe_mou_drop` | H1 Consumption Drop | $\mathbb{I}(\text{change\_mou} < -100)$ | Flag for severe voice traffic contraction. EDA demonstrated **53.62% churn rate** in this cohort vs 45.45% for moderate growth. |
| `severe_rev_drop` | H1 Consumption Drop | $\mathbb{I}(\text{change\_rev} < -20)$ | Flag for revenue defection. Indicates subscriber is actively pruning service add-ons prior to departure. |
| `rev_per_mou` | Cost Friction | $\frac{\text{rev\_Mean}}{\max(\text{mou\_Mean}, 1)}$ | Effective realized price per minute. Identifies high price-burden subscribers vulnerable to low-cost competitor promotions. |
| `overage_rev_ratio` | Bill Shock Exposure | $\frac{\text{ovrrev\_Mean}}{\max(\text{rev\_Mean}, 1)}$ | Proportion of bill derived from overage penalties. High overage triggers sudden dissatisfaction and churn. |
| `silent_churner_flag` | H3 Service Friction | $\mathbb{I}(\text{custcare\_Mean} == 0)$ | Captures the "Silent Churner" paradox: **51.76% churn** among subscribers with 0 calls to care vs 44.66% for frequent callers. |
| `drop_per_call` | Network Quality | $\frac{\text{drop\_blk\_Mean}}{\max(\text{totcalls}, 1)}$ | Network friction index: proportion of attempted calls dropped or blocked due to network congestion or poor coverage. |
| `multi_line_flag` | H4 Account Fragility | $\mathbb{I}(\text{actvsubs} > 1)$ | Secondary line vulnerability indicator. EDA confirmed 2-line accounts churn at **52.22%** (cutting secondary line during economic tightening). |
| `high_arpu_tier` | Value at Risk | $\mathbb{I}(\text{rev\_Mean} \ge 75.0)$ | Top ARPU quintile Q5 holding **41.8% of Company A's monthly revenue at risk** ($1,196,130/month). |

---

## 5. Preprocessing Pipeline Architecture & Scaler Design

The complete scikit-learn `ColumnTransformer` is structured as follows:

```mermaid
graph TD
    A[Raw Merged Dataset: 100,000 x 100] --> B[Quarantine Customer_ID & Target Churn]
    B --> C[Business Feature Engineering: 12 Domain Levers]
    C --> D[Predictor Matrix X: 100,000 x 110]
    D --> E[Stratified Split 70% / 15% / 15%: SEED=42]
    E --> F[X_train: 70,000 x 110]
    E --> G[X_val: 15,000 x 110]
    E --> H[X_test Held-out: 15,000 x 110]
    
    subgraph Preprocessor Pipeline [Fitted ONLY on X_train]
        I[Numerical Pipeline: 89 features] --> I1[SimpleImputer: Median + MissingIndicator]
        I1 --> I2[StandardScaler: Mean=0, Std=1]
        
        J[Categorical Pipeline: 21 features] --> J1[SimpleImputer: Constant 'Missing']
        J1 --> J2[OneHotEncoder: handle_unknown='ignore']
    end
    
    F --> Preprocessor Pipeline
    Preprocessor Pipeline --> K[X_train_proc: 70,000 x 279]
    G --> Preprocessor Pipeline --> L[X_val_proc: 15,000 x 279]
    H --> Preprocessor Pipeline --> M[X_test_proc: 15,000 x 279 Locked]
```

### Why One-Hot Encoding with `handle_unknown='ignore'`?
1. Nominal variables such as `area` (20 regional areas), `ethnic` (18 categories), and `crclscod` (54 credit sub-classes) have no natural numerical order. Applying ordinal encoding would impose an artificial linear topology (e.g., Area 20 is "greater" than Area 1), distorting linear weights and distance-based splits.
2. Setting `handle_unknown='ignore'` ensures that any unseen category in production or testing does not trigger an execution exception; it is simply encoded as all zeros across the one-hot columns.

### Scaler Strategy
`StandardScaler` is fitted strictly on the imputed numerical features of `X_train`. Scaling is mandatory for linear models (Logistic Regression) to ensure proper gradient descent convergence and fair L2 regularization across variables with drastically different units (e.g., `totmou` in thousands of minutes vs `eqp_over_1yr` as binary flags). For tree-based models in Stage 6 (HistGradientBoosting / XGBoost / Random Forest), the unscaled or scaled features yield invariant split locations.

---

## 6. Dataset Split Verification & Quality Gates

The splitting protocol was verified against rigorous assertion checks:

```python
# Exact split assertions verified in Section 4.3 of telecom_retention_analysis.py
assert len(X_train) == 70000, "Train size mismatch!"
assert len(X_val) == 15000, "Val size mismatch!"
assert len(X_test) == 15000, "Test size mismatch!"
assert abs(y_train.mean() - 0.49562) < 0.001, "Stratification mismatch in train!"
assert abs(y_val.mean() - 0.49562) < 0.001, "Stratification mismatch in val!"
assert abs(y_test.mean() - 0.49562) < 0.001, "Stratification mismatch in test!"
assert not np.isnan(X_train_proc).any(), "NaNs in preprocessed train set!"
assert not np.isnan(X_val_proc).any(), "NaNs in preprocessed validation set!"
assert not np.isnan(X_test_proc).any(), "NaNs in preprocessed test set!"
```

### Final Split Summary Table:

| Split Partition | Sample Count ($n$) | Percentage (%) | Retained Count ($y=0$) | Churned Count ($y=1$) | Churn Rate (%) | Role in Project Lifecycle |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **Training Set (`train`)** | 70,000 | 70.0% | 35,306 | 34,694 | 49.56% | Model fitting, parameter estimation, imputation fitting, scaling. |
| **Validation Set (`val`)** | 15,000 | 15.0% | 7,566 | 7,434 | 49.56% | Model selection, hyperparameter tuning, cutoff threshold ($\tau^*$) calibration. |
| **Held-Out Test Set (`test`)** | 15,000 | 15.0% | 7,566 | 7,434 | 49.56% | **LOCKED**. Single final evaluation pass in Stage 6 / Stage 11. Zero tuning allowed. |
| **Total** | **100,000** | **100.0%** | **50,438** | **49,562** | **49.56%** | Complete dataset verified 1:1 without record loss. |

---

## 7. Status & Transition to Stage 6

With Stage 5 completed and all acceptance criteria satisfied:
- The data preparation pipeline is 100% reproducible and encapsulated in `notebooks/telecom_retention_analysis.py`.
- Transformed matrices `X_train_proc`, `X_val_proc`, and `X_test_proc` are verified with 279 clean, dense features and zero NaNs.
- The pipeline is prepared for **Stage 6: Machine Learning Benchmarks & Multi-Model Evaluation** (`DummyClassifier`, `LogisticRegression`, and gradient boosted decision trees).
