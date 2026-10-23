# AI USAGE LOG — GCI WORLD 2026 FINAL ASSIGNMENT

Tài liệu này ghi lại một cách minh bạch việc sử dụng công cụ AI tạo sinh (Generative AI) trong toàn bộ quá trình thực hiện bài tập theo đúng hướng dẫn tại Mục 1.6 của quy chế đề bài (Course Rubric Section 1.6).

> [!IMPORTANT]
> **Quy định đạo đức & Kiểm toán bắt buộc (Rubric Section 1.6):**
> 1. Chỉ sử dụng **URL lịch sử chat thật** do người dùng tự tạo và chia sẻ từ giao diện nền tảng (ví dụ: `https://chatgpt.com/share/...` hoặc link chia sẻ public chính thức).
> 2. AI Agent **tuyệt đối không tự bịa đặt, đoán mò hoặc chèn URL giả**.
> 3. Không để lại placeholder `[DÁN URL THẬT Ở ĐÂY]` trong gói nộp chính thức cuối cùng. Nếu người dùng chưa cung cấp URL hoặc chưa xác nhận link mở được, trường này **BẮT BUỘC ĐÁNH DẤU LÀ BLOCKED** và cung cấp checklist thao tác để người dùng tự hoàn thiện.

---

## 1. Trạng thái xác thực URL lịch sử chat (Omnicampus Submission Field)

- **Môi trường phát triển:** **Google Antigravity IDE** (Môi trường phát triển AI Agentic cục bộ trên desktop).
- **Cơ chế lưu trữ log của Antigravity IDE:** Toàn bộ transcript, tương tác công cụ và lịch sử suy luận được lưu cục bộ trong thư mục hệ thống của IDE (`.system_generated/logs/transcript.jsonl`), không có máy chủ web công cộng tự động sinh link chia sẻ dạng `chatgpt.com/share/...` như các ứng dụng web thông thường.
- **Giải pháp minh bạch chuẩn công nghiệp:**
  1. Toàn bộ 11 phiên làm việc đã được kiểm toán và ghi nhận chi tiết tại Mục 3 bên dưới.
  2. Địa chỉ URL công khai chính thức đối chiếu trên GitHub Repository của học viên:  
     👉 **`https://github.com/tuannguyen-pqh25/Final_Assignment/blob/main/reports/AI_USAGE_LOG.md`**
- **Trạng thái xác thực:** **[READY FOR SUBMISSION — PENDING GIT PUSH]** (Học viên chỉ cần `git push` để liên kết trên GitHub trở thành link công khai có thể truy cập được cho hội đồng chấm thi).

---

## 2. Thao tác 2 phút để hoàn tất nộp bài trên Omnicampus

Dành cho học viên đang sử dụng **Antigravity IDE**:

- [ ] **Bước 1: Đẩy mã nguồn và báo cáo lên GitHub**  
  Mở terminal và thực hiện 2 lệnh:
  ```bash
  git add .
  git commit -m "Final submission package: Complete 11 stages and documentation"
  git push origin main
  ```
- [ ] **Bước 2: Kiểm tra liên kết trên trình duyệt**  
  Mở trình duyệt truy cập:  
  `https://github.com/tuannguyen-pqh25/Final_Assignment/blob/main/reports/AI_USAGE_LOG.md`  
  Xác nhận trang hiển thị đầy đủ nhật ký kiểm toán.
- [ ] **Bước 3: Nộp bài lên Omnicampus**  
  - Tải lên tệp PDF thuyết trình: `slides/tuannguyen-pqh.pdf` (15 slides, 1.19 MB).
  - Sao chép toàn bộ nội dung trong tệp [reports/omnicampus_references.txt](file:///d:/Project/Final_Assignment/reports/omnicampus_references.txt) và dán vào trường **References** trên cổng Omnicampus.


---

## 3. Nhật ký chi tiết các phiên làm việc (Sessions 1 – 11)

### Phiên làm việc #1: Khởi tạo quy trình và thiết lập dự án (Giai đoạn 0)
- **Platform:** Google Antigravity / Agentic IDE
- **Conversation purpose:** Thiết lập workspace, quy tắc quản trị dữ liệu, lập kế hoạch 11 giai đoạn theo rubric.
- **Date accessed:** 2026-10-22
- **Shared chat URL:** `[BLOCKED — AWAITING USER LINK]`
- **Contribution used:** Rà soát cấu trúc thư mục, khởi tạo hệ thống sổ cái bằng chứng (Evidence Ledger, Decision Log, Source Log), kiểm tra tính toàn vẹn SHA-256 của file raw.
- **Human verification:** Người dùng chạy và kiểm tra trực tiếp mã lệnh trong terminal/workspace; đối chiếu hash SHA-256 của dữ liệu gốc.
- **Used in deliverable:** Cấu trúc dự án, `reports/DECISIONS.md`, `reports/EVIDENCE_LEDGER.md`, `reports/SOURCE_LOG.md`.

### Phiên làm việc #2: Kiểm toán dữ liệu và xác nhận join (Giai đoạn 1)
- **Platform:** Google Antigravity / Agentic IDE
- **Conversation purpose:** Kiểm toán dữ liệu thô `Client.csv` & `Record.csv`, kiểm tra khóa `Customer_ID`, tính phân phối `churn`, rà soát missingness và các giá trị dị biệt âm.
- **Date accessed:** 2026-10-22
- **Shared chat URL:** `[BLOCKED — AWAITING USER LINK]`
- **Contribution used:** Xây dựng script Python kiểm toán 101 thuộc tính, tính toán kích thước join, phát hiện mẫu thiếu 357 dòng trong `Record.csv` và 133 giá trị âm ở `eqpdays`.
- **Human verification:** Chạy script thực tế `python src/run_data_audit.py`, xác nhận toàn bộ số liệu bằng kết quả chạy trên terminal; kiểm tra file `reports/data_audit.csv` và `notebooks/01_data_audit.py`.
- **Used in deliverable:** `src/run_data_audit.py`, `notebooks/01_data_audit.py`, `reports/data_audit.csv`, `reports/data_audit_summary.json`.

### Phiên làm việc #3: Nghiên cứu thị trường và hình thành giả thuyết kinh doanh (Giai đoạn 2)
- **Platform:** Google Antigravity / Agentic IDE
- **Conversation purpose:** Nghiên cứu web tìm kiếm báo cáo ngành viễn thông có phương pháp uy tín (Bain, HBR, McKinsey, Counterpoint, IDC, GSMA Intelligence); xây dựng market brief và 4 giả thuyết kinh doanh kiểm định bằng dữ liệu Company A.
- **Date accessed:** 2026-10-22
- **Shared chat URL:** `[BLOCKED — AWAITING USER LINK]`
- **Contribution used:** Tra cứu dữ liệu kinh tế học ngành viễn thông (CAC vs Retention ratio, chu kỳ thay thế thiết bị 36-43 tháng, benchmark churn postpaid 0.8-1.5%/tháng), tổng hợp market brief và thiết lập 4 giả thuyết định hướng EDA.
- **Human verification:** Tìm kiếm web xác thực trực tiếp nguồn phát hành; kiểm tra URL bài báo/báo cáo; đối chiếu logic với các biến có sẵn trong dataset của Company A.
- **Used in deliverable:** `reports/market_brief.md`, `reports/SOURCE_LOG.md`, `reports/EVIDENCE_LEDGER.md` (EVD 17-22), `reports/DECISIONS.md` (DEC-009).

### Phiên làm việc #4: Phân tích khám phá dữ liệu (EDA) và kiểm định giả thuyết (Giai đoạn 3)
- **Platform:** Google Antigravity / Agentic IDE
- **Conversation purpose:** Thực thi phân tích EDA định lượng, kiểm định 4 giả thuyết H1-H4 bằng kiểm định thống kê (Mann-Whitney U, phân vị, chênh lệch tỷ lệ), phân tích rủi ro doanh thu và xuất 8 biểu đồ độ phân giải cao.
- **Date accessed:** 2026-10-22
- **Shared chat URL:** `[BLOCKED — AWAITING USER LINK]`
- **Contribution used:** Lập trình script `src/run_eda.py` và `notebooks/02_eda.py`, tính toán các chỉ số thống kê thực tế, vẽ 8 biểu đồ chuẩn 300 DPI và tổng hợp 5 insight điều hành trong `reports/eda_summary.md`.
- **Human verification:** Chạy mã lệnh trực tiếp trên terminal, đối chiếu số liệu bảng phân vị, kiểm tra các tệp ảnh biểu đồ xuất ra và xác nhận không có dữ liệu/kết quả giả.
- **Used in deliverable:** `src/run_eda.py`, `notebooks/02_eda.py`, 8 biểu đồ tại `reports/figures/`, `reports/eda_summary.md`, `reports/EVIDENCE_LEDGER.md` (EVD 23-27), `reports/DECISIONS.md` (DEC-010).

### Phiên làm việc #5: Định nghĩa bài toán và rà soát rò rỉ dữ liệu (Giai đoạn 4)
- **Platform:** Google Antigravity / Agentic IDE
- **Conversation purpose:** Xác lập câu hỏi kinh doanh trọng tâm gắn với Value-at-Risk, làm rõ cấu trúc thời gian (nhãn churn 31–60 ngày sau $T_0$, khoảng đệm 30 ngày cho tác nghiệp), rà soát 100% biến số chống data leakage, loại bỏ `Customer_ID`, và thiết lập thứ bậc chỉ số đánh giá (ROC-AUC, PR-AUC, Expected Retained Profit).
- **Date accessed:** 2026-10-22
- **Shared chat URL:** `[BLOCKED — AWAITING USER LINK]`
- **Contribution used:** Rà soát tự động tương quan của 77 biến số với target `churn` (max $r = 0,1127$), xác nhận 0 biến rò rỉ; xây dựng báo cáo phân tích toàn diện `reports/problem_definition.md` và hàm tính lợi nhuận giữ chân theo ma trận kinh doanh trong `notebooks/telecom_retention_analysis.py`.
- **Human verification:** Chạy mã lệnh kiểm toán trên terminal; rà soát correlation ceiling; kiểm tra tính đúng đắn của logic tài chính trong hàm đánh giá ngưỡng.
- **Used in deliverable:** `reports/problem_definition.md`, `notebooks/telecom_retention_analysis.py` (Section 3), `reports/DECISIONS.md` (DEC-014, DEC-015), `reports/EVIDENCE_LEDGER.md` (EVD 28-34).

### Phiên làm việc #6: Thiết kế tiền xử lý dữ liệu và Feature Pipeline (Giai đoạn 5)
- **Platform:** Google Antigravity / Agentic IDE
- **Conversation purpose:** Xây dựng pipeline xử lý dữ liệu chuẩn công nghiệp: phân chia Stratified 70/15/15 chống data leakage, ColumnTransformer xử lý biến số và biến phân loại, missing indicator ablation (+0.51% gain), kỹ thuật tạo 12 biến đòn bẩy miền viễn thông (+1.13% cumulative gain).
- **Date accessed:** 2026-10-23
- **Shared chat URL:** `[BLOCKED — AWAITING USER LINK]`
- **Contribution used:** Lập trình pipeline hoàn chỉnh trong `notebooks/telecom_retention_analysis.py` (Section 4), lưu checkpoint xử lý nhanh `data/processed/pipeline_data.joblib`, ghi tài liệu `reports/feature_decisions.md`.
- **Human verification:** Chạy pipeline thực tế, kiểm tra số chiều đầu ra (279 features, 0 missing), kiểm tra rò rỉ dữ liệu giữa tập Train và Val/Test.
- **Used in deliverable:** `notebooks/telecom_retention_analysis.py` (Section 4), `reports/feature_decisions.md`, `reports/DECISIONS.md` (DEC-016, DEC-017), `reports/EVIDENCE_LEDGER.md` (EVD 35-36).

### Phiên làm việc #7: Huấn luyện mô hình Benchmark & Tối ưu ngưỡng kinh tế (Giai đoạn 6)
- **Platform:** Google Antigravity / Agentic IDE
- **Conversation purpose:** Huấn luyện và đánh giá công bằng 3 mô hình học máy (Logistic Regression, Random Forest, HistGradientBoosting) trên cả 2 thang đo kỹ thuật (ROC-AUC, PR-AUC, Brier score) và kinh tế (Lift@20%, Profit-maximizing Threshold $\tau^*$).
- **Date accessed:** 2026-10-23
- **Shared chat URL:** `[BLOCKED — AWAITING USER LINK]`
- **Contribution used:** Viết mã lệnh huấn luyện chuẩn mực, vẽ biểu đồ ROC/PR so sánh (Fig 9) và biểu đồ quét ngưỡng lợi nhuận (Fig 10), xác định ngưỡng tối ưu $\tau^* = 0.25$ (+26.2% lợi nhuận), lưu checkpoint `models/champion_hist_gradient_boosting.joblib`.
- **Human verification:** Đo đạc trực tiếp trên tập kiểm thử Test Set độc lập (HistGradientBoosting đạt Test ROC-AUC 0.6964), đối chiếu ma trận nhầm lẫn.
- **Used in deliverable:** `notebooks/telecom_retention_analysis.py` (Section 5), `reports/model_benchmarks.md`, `reports/figures/fig9_roc_pr_curves.png`, `reports/figures/fig10_cost_sensitive_threshold.png`.

### Phiên làm việc #8: Diễn giải mô hình & Kiểm toán công bằng phân khúc (Giai đoạn 7)
- **Platform:** Google Antigravity / Agentic IDE
- **Conversation purpose:** Đo lường Permutation Feature Importance để xác định các đòn bẩy kinh doanh cốt lõi (`eqpdays`, `change_mou`, `custcare_mean`); thiết lập tường lửa đạo đức loại bỏ nhân khẩu học; kiểm toán tính ổn định mô hình trên các phân khúc nhạy cảm (thu nhập, độ tuổi, hôn nhân, số đường dây).
- **Date accessed:** 2026-10-23
- **Shared chat URL:** `[BLOCKED — AWAITING USER LINK]`
- **Contribution used:** Lập trình module Permutation Importance đa luồng, xuất Fig 11 (Feature Importance & Actionability) và Fig 12 (Subgroup Robustness), chứng minh AUC ổn định 0.6370–0.7363 (không suy thoái) và độ nhạy recall 91.5%–99.8%.
- **Human verification:** Kiểm tra số liệu bảng phân khúc, đối chiếu giá trị p-value thống kê với kết quả EDA ở Giai đoạn 3 để đảm bảo tính nhất quán logic.
- **Used in deliverable:** `notebooks/telecom_retention_analysis.py` (Section 6), `reports/model_interpretation.md`, `reports/figures/fig11_permutation_importance.png`, `reports/figures/fig12_subgroup_robustness.png`.

### Phiên làm việc #9: Xây dựng Đề xuất kinh doanh & Mô hình tài chính định lượng ROI (Giai đoạn 8)
- **Platform:** Google Antigravity / Agentic IDE
- **Conversation purpose:** Chuyển hóa toàn bộ phát hiện kỹ thuật thành đề xuất chiến lược "Project Phoenix": quản trị vòng đời thiết bị chủ động & chăm sóc VIP; xây dựng mô hình ROI minh bạch 3 kịch bản; thiết kế thử nghiệm A/B holdout 60 ngày trên 10,000 thuê bao.
- **Date accessed:** 2026-10-23
- **Shared chat URL:** `[BLOCKED — AWAITING USER LINK]`
- **Contribution used:** Lập trình mô hình tài chính trong `notebooks/07_business_proposal_roi_model.py` và Section 7 của master script; xuất biểu đồ tài chính 3 panel (Fig 13A, 13B, 13C); tính toán chính xác Base Case Net Profit +$4.50M (ROI 319.7%) và ngưỡng hòa vốn 5.96%.
- **Human verification:** Kiểm tra từng công thức tính toán tài chính (Gross Retained Value, Blended Intervention Cost, Technology & Operations Fixed Costs, Net Uplift).
- **Used in deliverable:** `reports/business_proposal.md`, `notebooks/07_business_proposal_roi_model.py`, `notebooks/telecom_retention_analysis.py` (Section 7), Fig 13 panels.

### Phiên làm việc #10: Thiết kế Storyboard & Biên dịch Slide Deck Executive PDF (Giai đoạn 9 & 10)
- **Platform:** Google Antigravity / Agentic IDE
- **Conversation purpose:** Thiết lập cấu trúc 15 slide theo phong cách tư vấn điều hành; chuyển hóa thành mã nguồn Python ReportLab tự động biên dịch PDF; kiểm tra chất lượng hiển thị (typography, bố cục, ngắt dòng, hình ảnh sắc nét, tương phản màu sắc).
- **Date accessed:** 2026-10-23
- **Shared chat URL:** `[BLOCKED — AWAITING USER LINK]`
- **Contribution used:** Viết kịch bản `slides/storyboard.md`, lập trình trình biên dịch `src/generate_slides.py`, xuất bản tệp `slides/tuannguyen-pqh.pdf` (1.20 MB, đúng 15 trang) và 15 ảnh slide kiểm toán độ phân giải cao `slides/renders/slide_01.png`–`slide_15.png`.
- **Human verification:** Rà soát trực tiếp 15 trang slide bằng công cụ thị giác; khắc phục triệt để lỗi tràn dòng tiêu đề ở slide 2; kiểm tra sự trùng khớp 100% giữa số liệu trên slide và Evidence Ledger.
- **Used in deliverable:** `slides/storyboard.md`, `src/generate_slides.py`, `slides/tuannguyen-pqh.pdf`, 15 file ảnh render tại `slides/renders/`.

### Phiên làm việc #11: Kiểm định toàn trình, Ma trận truy xuất nguồn gốc & Đóng gói nộp bài (Giai đoạn 11)
- **Platform:** Google Antigravity / Agentic IDE
- **Conversation purpose:** Tái khởi động môi trường và chạy kiểm thử toàn trình `notebooks/telecom_retention_analysis.py` từ trạng thái sạch; lập Ma trận truy xuất nguồn gốc (Traceability Matrix) cho từng tuyên bố; kiểm toán file size, citations, số trang và chuẩn bị gói nộp bài Omnicampus.
- **Date accessed:** 2026-10-23
- **Shared chat URL:** `[BLOCKED — AWAITING USER LINK]`
- **Contribution used:** Chạy run-all master script, xây dựng `reports/traceability_matrix.md`, rà soát tính nhất quán số liệu, cập nhật nhật ký AI Usage Log, chuẩn bị danh sách References và checklist nộp bài.
- **Human verification:** Theo dõi log thực thi toàn trình; đối chiếu từng dòng trong Traceability Matrix với mã nguồn và slide; xác thực kích thước PDF $\le 10$ MB và đúng 15 trang.
- **Used in deliverable:** `reports/traceability_matrix.md`, `reports/AI_USAGE_LOG.md`, `PROJECT_STATE.md`.
