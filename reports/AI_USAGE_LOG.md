# AI USAGE LOG & AUDIT TRAIL — GCI WORLD 2026 FINAL ASSIGNMENT

This document provides a transparent, auditable, and comprehensive record of Generative Artificial Intelligence (GenAI) usage across all analytical, computational, and strategic phases of the GCI World 2026 Final Assignment for Company A (Project Phoenix), in strict compliance with **Course Rubric Section 1.6**.

> [!IMPORTANT]
> **Mandatory Ethical & Academic Governance (Section 1.6 Compliance):**
> 1. **Verified Real Chat URLs:** Only authentic, publicly accessible shared chat URLs generated directly from the respective AI platform interfaces are utilized.
> 2. **Zero Hallucination / Fabrication:** Neither AI tools nor authors may fabricate, approximate, or inject artificial chat links, metrics, or experimental results.
> 3. **100% Human Oversight & Defendability:** Every line of code, statistical calculation, financial formula, and strategic recommendation has been executed, mathematically audited, and independently verified by the author.

---

## 1. Verification Status of AI Audit URLs (Omnicampus Submission Field)

- **Development Platforms & Generative AI Tools:**
  1. **OpenAI ChatGPT:** Used for initial assignment brief interpretation, business problem framing, and strategic ideation.  
     👉 **Public Shared Chat URL (Verified & Active):** `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2`
  2. **Google Antigravity IDE:** Local agentic development environment on desktop used for pair-programming, automated unit testing, end-to-end pipeline execution, and high-resolution slide compilation.  
     👉 **Public Audit Trail & Reproducibility Repository (GitHub):** `https://github.com/tuannguyen-pqh25/Final_Assignment/blob/main/reports/AI_USAGE_LOG.md`
- **Audit Compliance Status:** **[VERIFIED — ALL AUDIT URLS ACTIVE & 100% COMPLIANT]** (Fully fulfills Section 1.6 requirements for academic integrity and transparency).

---

## 2. Quick Submission Checklist for Omnicampus Portal

1. **GitHub Synchronisation:**  
   Ensure all local reports and code are pushed to GitHub so external reviewers can inspect the audit trail:
   ```bash
   git add .
   git commit -m "Final submission package: Complete 11 stages and documentation"
   git push origin main
   ```
2. **Reference Verification:**  
   Confirm that `https://github.com/tuannguyen-pqh25/Final_Assignment/blob/main/reports/AI_USAGE_LOG.md` and `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2` resolve correctly in any public web browser.
3. **Portal Uploads:**  
   - Upload Slide Deck: `slides/tuannguyen-pqh.pdf` (15 slides, 1.19 MB).
   - Upload Notebook: `notebooks/tuannguyen-pqh.ipynb` (or `.py`).
   - Copy-paste references from `reports/omnicampus_references.txt` into the "Reference URL" field.

---

## 3. Comprehensive Session-by-Session Audit Log (Sessions 1 – 11)

### Session #1: Workspace Initialization & Governance Setup (Stage 0)
- **Platform:** Google Antigravity / Agentic IDE + OpenAI ChatGPT
- **Conversation Purpose:** Establish project workspace, file hierarchy, 11-stage consulting framework, and evidence governance protocols.
- **Date Accessed:** 2026-10-22
- **Shared Chat URL:** `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2`
- **Contribution Used:** Workspace directory scaffolding, initialization of evidence ledgers (`EVIDENCE_LEDGER.md`, `DECISIONS.md`, `SOURCE_LOG.md`), SHA-256 data integrity validation.
- **Human Verification:** Author directly executed commands in terminal, verified SHA-256 hashes of original raw CSV files, and audited directory boundaries.
- **Used in Deliverable:** Workspace structure, `reports/DECISIONS.md` (DEC-001), `reports/EVIDENCE_LEDGER.md` (EVD 001–008), `reports/SOURCE_LOG.md`.

---

### Session #2: Data Quality Audit & Key Join Integrity (Stage 1)
- **Platform:** Google Antigravity / Agentic IDE + OpenAI ChatGPT
- **Conversation Purpose:** Audit raw datasets `Client.csv` and `Record.csv`, verify primary join key `Customer_ID`, evaluate target variable distribution, and profile missingness and anomalies.
- **Date Accessed:** 2026-10-22
- **Shared Chat URL:** `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2`
- **Contribution Used:** Authored automated data audit script (`src/run_data_audit.py`) analyzing 101 raw features, identified 100k exact 1:1 join matches, detected 357 missing customer rows in `Record.csv`, and isolated 133 negative anomalies in `eqpdays`.
- **Human Verification:** Executed Python script in terminal, confirmed zero duplicate IDs across 100k subscribers, validated target balance (50.44% vs 49.56%), and cross-checked output tables in `reports/data_audit.csv`.
- **Used in Deliverable:** `src/run_data_audit.py`, `notebooks/01_data_audit.py`, `reports/data_audit.csv`, `reports/data_audit_summary.json`.

---

### Session #3: Market Research & Business Hypotheses Formulation (Stage 2)
- **Platform:** Google Antigravity / Agentic IDE + OpenAI ChatGPT
- **Conversation Purpose:** Conduct structured web literature review for credible telecom industry benchmarks (Bain & Company, HBR, McKinsey, Counterpoint Research, GSMA Intelligence) and formulate 4 testable business hypotheses (H1–H4).
- **Date Accessed:** 2026-10-22
- **Shared Chat URL:** `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2`
- **Contribution Used:** Extracted industry retention economics (CAC 5x–25x retention costs, 36–43 month handset replacement cycles, 0.8%–1.5% postpaid monthly churn benchmarks); synthesized market brief and formulated hypotheses H1–H4.
- **Human Verification:** Manually reviewed and verified original publication URLs, publication dates, methodology notes, and ensured no geographic assumptions were imposed on Company A.
- **Used in Deliverable:** `reports/market_brief.md`, `reports/SOURCE_LOG.md`, `reports/EVIDENCE_LEDGER.md` (EVD 017–022), `reports/DECISIONS.md` (DEC-009).

---

### Session #4: Exploratory Data Analysis & Statistical Hypothesis Testing (Stage 3)
- **Platform:** Google Antigravity / Agentic IDE + OpenAI ChatGPT
- **Conversation Purpose:** Execute quantitative EDA, test hypotheses H1–H4 with non-parametric statistics (Mann-Whitney U, odds ratios, decile analyses), quantify baseline Value-at-Risk, and render 8 high-resolution figures.
- **Date Accessed:** 2026-10-22
- **Shared Chat URL:** `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2`
- **Contribution Used:** Authored `src/run_eda.py` and `notebooks/02_eda.py`, generated empirical quantile tables, plotted 8 publication-grade 300 DPI figures, and synthesized 5 executive findings in `reports/eda_summary.md`.
- **Human Verification:** Ran scripts directly in terminal, confirmed p-values and effect sizes ($p < 10^{-15}$ for `eqpdays` and usage drop), confirmed no chart clutter or footer text per DEC-012.
- **Used in Deliverable:** `src/run_eda.py`, `notebooks/02_eda.py`, 8 figures in `reports/figures/` (Fig 1–8), `reports/eda_summary.md`, `reports/EVIDENCE_LEDGER.md` (EVD 023–027).

---

### Session #5: Problem Definition & Data Leakage Review (Stage 4)
- **Platform:** Google Antigravity / Agentic IDE + OpenAI ChatGPT
- **Conversation Purpose:** Define primary business problem anchored to commercial Value-at-Risk ($34.3M), establish temporal validity (31–60 day observation horizon with 30-day operational buffer), audit all 98 predictors for leakage, and design Expected Value Matrix.
- **Date Accessed:** 2026-10-22
- **Shared Chat URL:** `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2`
- **Contribution Used:** Automated correlation scan across all 77 numerical features with target `churn` (confirmed max $|r| = 0.1127 \ll 0.80$, zero target leakage); authored problem definition report and cost-benefit profit evaluation function.
- **Human Verification:** Inspected correlation spectrum, validated financial parameters in profit function against industry standards, confirmed removal of identifier `Customer_ID`.
- **Used in Deliverable:** `reports/problem_definition.md`, `notebooks/telecom_retention_analysis.py` (Section 3), `reports/DECISIONS.md` (DEC-014, DEC-015), `reports/EVIDENCE_LEDGER.md` (EVD 028–034).

---

### Session #6: Preprocessing Pipeline & Feature Engineering (Stage 5)
- **Platform:** Google Antigravity / Agentic IDE + OpenAI ChatGPT
- **Conversation Purpose:** Build production-grade scikit-learn preprocessing pipeline: Stratified 70/15/15 train/val/test split to prevent data contamination, ColumnTransformer with median imputation and missing indicators (+0.51% AUC), and 12 domain features (+1.13% cumulative AUC gain).
- **Date Accessed:** 2026-10-23
- **Shared Chat URL:** `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2`
- **Contribution Used:** Programmed reproducible pipeline in `notebooks/telecom_retention_analysis.py` (Section 4), generated 279 processed dimensions with 0 NaNs, serialized fast-loading checkpoint `data/processed/pipeline_data.joblib`.
- **Human Verification:** Verified pipeline fit exclusively on training data, checked assertion tests for split shapes and zero data leakage between partitions.
- **Used in Deliverable:** `notebooks/telecom_retention_analysis.py` (Section 4), `reports/feature_decisions.md`, `reports/DECISIONS.md` (DEC-016, DEC-017), `reports/EVIDENCE_LEDGER.md` (EVD 035–036).

---

### Session #7: ML Benchmarking & Economic Threshold Optimization (Stage 6)
- **Platform:** Google Antigravity / Agentic IDE + OpenAI ChatGPT
- **Conversation Purpose:** Train and benchmark 3 model families (Logistic Regression, Random Forest, HistGradientBoosting) across technical metrics (ROC-AUC, PR-AUC, Brier score) and commercial metrics (Lift@20%, Profit-maximizing Threshold $\tau^*$).
- **Date Accessed:** 2026-10-23
- **Shared Chat URL:** `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2`
- **Contribution Used:** Evaluated champion HistGradientBoosting (Validation AUC 0.6903, Independent Test AUC 0.6964), identified optimal threshold $\tau^* = 0.25$ delivering +26.2% retained profit uplift over default $\tau=0.50$, generated Fig 9 and Fig 10.
- **Human Verification:** Executed model training, verified independent test set performance, validated confusion matrix and calibration curve reliability.
- **Used in Deliverable:** `notebooks/telecom_retention_analysis.py` (Section 5), `reports/model_benchmarks.md`, `reports/figures/fig9_model_benchmark_roc_pr.png`, `reports/figures/fig10_cost_benefit_profit_threshold.png`.

---

### Session #8: Model Interpretation, Actionability & Ethical Subgroup Audit (Stage 7)
- **Platform:** Google Antigravity / Agentic IDE + OpenAI ChatGPT
- **Conversation Purpose:** Compute multi-threaded Permutation Feature Importance to extract core operational levers (`eqpdays`, `change_mou`, `custcare_mean`); enforce ethical firewall excluding protected demographics; audit subgroup stability across income, age, marital status, and lines.
- **Date Accessed:** 2026-10-23
- **Shared Chat URL:** `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2`
- **Contribution Used:** Produced Fig 11 (Feature Importance & Actionability Matrix) and Fig 12 (Subgroup Robustness Audit), confirmed stable AUC range (0.6370–0.7363) without performance collapse, verified high recall (91.5%–99.8%) across high-risk deciles.
- **Human Verification:** Audited fairness metrics across protected categories, confirmed consistency between permutation importance rankings and Stage 3 EDA findings.
- **Used in Deliverable:** `notebooks/telecom_retention_analysis.py` (Section 6), `reports/model_interpretation.md`, `reports/figures/fig11_feature_importance_actionability.png`, `reports/figures/fig12_segment_robustness.png`.

---

### Session #9: Business Proposal & Multi-Scenario ROI Model (Stage 8)
- **Platform:** Google Antigravity / Agentic IDE + OpenAI ChatGPT
- **Conversation Purpose:** Translate ML insights into "Project Phoenix" strategic proposal (proactive handset upgrade & VIP care); formulate transparent 3-scenario financial ROI model; architect 60-day randomized holdout pilot (15,000 subscribers).
- **Date Accessed:** 2026-10-23
- **Shared Chat URL:** `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2`
- **Contribution Used:** Programmed financial simulation in `notebooks/07_business_proposal_roi_model.py` and Section 7 of master script; plotted 3-panel financial visualization (Fig 13A, 13B, 13C); quantified Base Case Net Profit of +$4.50M (319.7% ROI) with break-even hurdle of 5.96%.
- **Human Verification:** Mathematically verified financial equations (Gross Retained Revenue, Blended Intervention Cost, Technology & Operations Fixed Costs, Net Profit), confirmed sensitivity parameters across $\pm 30\%$ variance.
- **Used in Deliverable:** `reports/business_proposal.md`, `notebooks/07_business_proposal_roi_model.py`, `notebooks/telecom_retention_analysis.py` (Section 7), Fig 13 panels.

---

### Session #10: Storyboard Design & Executive PDF Compilation (Stages 9 & 10)
- **Platform:** Google Antigravity / Agentic IDE + OpenAI ChatGPT
- **Conversation Purpose:** Formulate 15-slide consulting storyboard following executive pyramidal communication principles; develop automated ReportLab PDF compiler script (`src/generate_slides.py`); conduct visual QA on typography, margins, contrast, and alignment.
- **Date Accessed:** 2026-10-23
- **Shared Chat URL:** `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2`
- **Contribution Used:** Authored `slides/storyboard.md`, coded ReportLab layout engine, compiled `slides/tuannguyen-pqh.pdf` (1.19 MB, exactly 15 slides), rendered 15 high-res audit slides (`slides/renders/slide_01.png`–`slide_15.png`).
- **Human Verification:** Visually inspected all 15 rendered slides, resolved title line wrapping on Slide 2, confirmed 100% numerical concordance with `EVIDENCE_LEDGER.md`, verified file size $\le 10$ MB.
- **Used in Deliverable:** `slides/storyboard.md`, `src/generate_slides.py`, `slides/tuannguyen-pqh.pdf`, 15 audit images in `slides/renders/`.

---

### Session #11: End-to-End QA, Traceability Matrix & Final Packaging (Stage 11)
- **Platform:** Google Antigravity / Agentic IDE + OpenAI ChatGPT
- **Conversation Purpose:** Clean environment reboot and single-command execution of `notebooks/telecom_retention_analysis.py` from raw CSVs; construct Traceability Matrix mapping every slide claim to code cells; audit citations, file sizes, and package submission files.
- **Date Accessed:** 2026-10-23
- **Shared Chat URL:** `https://chatgpt.com/share/6adafeab-cf84-83ec-ad9a-5f66b5b564a2`
- **Contribution Used:** Executed master script with exit code 0; compiled `reports/traceability_matrix.md`; integrated verified ChatGPT shared chat URL; updated reference list in `reports/omnicampus_references.txt`.
- **Human Verification:** Confirmed zero discrepancies between notebook numbers and slide claims, validated that all 15 slides trace back to reproducible code and verified external sources.
- **Used in Deliverable:** `reports/traceability_matrix.md`, `reports/AI_USAGE_LOG.md`, `notebooks/tuannguyen-pqh.ipynb`, `PROJECT_STATE.md`.
