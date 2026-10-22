# AI USAGE LOG — GCI WORLD 2026 FINAL ASSIGNMENT

Tài liệu này ghi lại một cách minh bạch việc sử dụng công cụ AI tạo sinh (Generative AI) trong quá trình thực hiện bài tập theo đúng hướng dẫn tại Mục 1.6 của [ChienLuoc.md](file:///d:/Project/Final_Assignment/ChienLuoc.md).

> [!IMPORTANT]
> **Quy định bắt buộc:**
> 1. Chỉ sử dụng **URL lịch sử chat thật** do người dùng tạo và cung cấp từ tính năng chia sẻ của nền tảng (ví dụ: `https://chatgpt.com/share/...`).
> 2. AI Agent **tuyệt đối không tự bịa đặt, đoán mò hoặc chèn URL giả**.
> 3. Không để lại placeholder `[DÁN URL THẬT Ở ĐÂY]` trong gói nộp chính thức cuối cùng.

---

## Nhật ký các phiên làm việc

### Phiên làm việc #1: Khởi tạo quy trình và thiết lập dự án (Giai đoạn 0)
- **Platform:** Google Antigravity / Claude / ChatGPT (theo môi trường người dùng kết nối)
- **Conversation purpose:** Thiết lập workspace, quy tắc quản trị dữ liệu, lập kế hoạch 11 giai đoạn theo rubric.
- **Date accessed:** 2026-10-22
- **Shared chat URL:** `[CHỜ NGƯỜI DÙNG CUNG CẤP URL CHIA SẺ THẬT - XEM HƯỚNG DẪN BÊN DƯỚI]`
- **Contribution used:** Rà soát cấu trúc thư mục, khởi tạo hệ thống sổ cái bằng chứng (Evidence Ledger, Decision Log, Source Log), kiểm tra tính toàn vẹn SHA-256 của file raw.
- **Human verification:** Người dùng chạy và kiểm tra trực tiếp mã lệnh trong terminal/workspace; đối chiếu hash SHA-256 của dữ liệu gốc.
- **Used in deliverable:** Cấu trúc dự án, `reports/DECISIONS.md`, `reports/EVIDENCE_LEDGER.md`, `reports/SOURCE_LOG.md`.
- **Status:** **PENDING_USER_URL** (Chờ người dùng nhấn Share và dán liên kết thật vào đây trước khi nộp).

### Phiên làm việc #2: Kiểm toán dữ liệu và xác nhận join (Giai đoạn 1)
- **Platform:** Google Antigravity / Claude / ChatGPT (theo môi trường người dùng kết nối)
- **Conversation purpose:** Kiểm toán dữ liệu thô `Client.csv` & `Record.csv`, kiểm tra khóa `Customer_ID`, tính phân phối `churn`, rà soát missingness và các giá trị dị biệt âm.
- **Date accessed:** 2026-10-22
- **Shared chat URL:** `[CHỜ NGƯỜI DÙNG CUNG CẤP URL CHIA SẺ THẬT - XEM HƯỚNG DẪN BÊN DƯỚI]`
- **Contribution used:** Xây dựng script Python kiểm toán 101 thuộc tính, tính toán kích thước join, phát hiện mẫu thiếu 357 dòng trong `Record.csv` và 133 giá trị âm ở `eqpdays`.
- **Human verification:** Chạy script thực tế `python src/run_data_audit.py`, xác nhận toàn bộ số liệu bằng kết quả chạy trên terminal; kiểm tra file `reports/data_audit.csv` và `notebooks/01_data_audit.py`.
- **Used in deliverable:** `src/run_data_audit.py`, `notebooks/01_data_audit.py`, `reports/data_audit.csv`, `reports/data_audit_summary.json`.
- **Status:** **PENDING_USER_URL** (Chờ người dùng cập nhật URL thật trước khi nộp).

### Phiên làm việc #3: Nghiên cứu thị trường và hình thành giả thuyết kinh doanh (Giai đoạn 2)
- **Platform:** Google Antigravity / Claude / ChatGPT (theo môi trường người dùng kết nối)
- **Conversation purpose:** Nghiên cứu web tìm kiếm báo cáo ngành viễn thông có phương pháp uy tín (Bain, HBR, McKinsey, Counterpoint, IDC, GSMA Intelligence); xây dựng market brief và 4 giả thuyết kinh doanh kiểm định bằng dữ liệu Company A.
- **Date accessed:** 2026-10-22
- **Shared chat URL:** `[CHỜ NGƯỜI DÙNG CUNG CẤP URL CHIA SẺ THẬT - XEM HƯỚNG DẪN BÊN DƯỚI]`
- **Contribution used:** Tra cứu dữ liệu kinh tế học ngành viễn thông (CAC vs Retention ratio, chu kỳ thay thế thiết bị 36-43 tháng, benchmark churn postpaid 0.8-1.5%/tháng), tổng hợp market brief và thiết lập 4 giả thuyết định hướng EDA.
- **Human verification:** Tìm kiếm web xác thực trực tiếp nguồn phát hành; kiểm tra URL bài báo/báo cáo; đối chiếu logic với các biến có sẵn trong dataset của Company A.
- **Used in deliverable:** `reports/market_brief.md`, `reports/SOURCE_LOG.md`, `reports/EVIDENCE_LEDGER.md` (EVD 17-22), `reports/DECISIONS.md` (DEC-009).
- **Status:** **PENDING_USER_URL** (Chờ người dùng cập nhật URL thật trước khi nộp).

### Phiên làm việc #4: Phân tích khám phá dữ liệu (EDA) và kiểm định giả thuyết (Giai đoạn 3)
- **Platform:** Google Antigravity / Claude / ChatGPT (theo môi trường người dùng kết nối)
- **Conversation purpose:** Thực thi phân tích EDA định lượng, kiểm định 4 giả thuyết H1-H4 bằng kiểm định thống kê (Mann-Whitney U, phân vị, chênh lệch tỷ lệ), phân tích rủi ro doanh thu và xuất 8 biểu đồ độ phân giải cao.
- **Date accessed:** 2026-10-22
- **Shared chat URL:** `[CHỜ NGƯỜI DÙNG CUNG CẤP URL CHIA SẺ THẬT - XEM HƯỚNG DẪN BÊN DƯỚI]`
- **Contribution used:** Lập trình script `src/run_eda.py` và `notebooks/02_eda.py`, tính toán các chỉ số thống kê thực tế, vẽ 8 biểu đồ chuẩn 300 DPI và tổng hợp 5 insight điều hành trong `reports/eda_summary.md`.
- **Human verification:** Chạy mã lệnh trực tiếp trên terminal, đối chiếu số liệu bảng phân vị, kiểm tra các tệp ảnh biểu đồ xuất ra và xác nhận không có dữ liệu/kết quả giả.
- **Used in deliverable:** `src/run_eda.py`, `notebooks/02_eda.py`, 8 biểu đồ tại `reports/figures/`, `reports/eda_summary.md`, `reports/EVIDENCE_LEDGER.md` (EVD 23-27), `reports/DECISIONS.md` (DEC-010).
- **Status:** **PENDING_USER_URL** (Chờ người dùng cập nhật URL thật trước khi nộp).

### Phiên làm việc #5: Định nghĩa bài toán và rà soát rò rỉ dữ liệu (Giai đoạn 4)
- **Platform:** Google Antigravity / Claude / ChatGPT (theo môi trường người dùng kết nối)
- **Conversation purpose:** Xác lập câu hỏi kinh doanh trọng tâm gắn với Value-at-Risk, làm rõ cấu trúc thời gian (nhãn churn 31–60 ngày sau $T_0$, khoảng đệm 30 ngày cho tác nghiệp), rà soát 100% biến số chống data leakage, loại bỏ `Customer_ID`, và thiết lập thứ bậc chỉ số đánh giá (ROC-AUC, PR-AUC, Expected Retained Profit).
- **Date accessed:** 2026-10-22
- **Shared chat URL:** `[CHỜ NGƯỜI DÙNG CUNG CẤP URL CHIA SẺ THẬT - XEM HƯỚNG DẪN BÊN DƯỚI]`
- **Contribution used:** Rà soát tự động tương quan của 77 biến số với target `churn` (max $r = 0,1127$), xác nhận 0 biến rò rỉ; xây dựng báo cáo phân tích toàn diện `reports/problem_definition.md` và hàm tính lợi nhuận giữ chân theo ma trận kinh doanh trong `notebooks/telecom_retention_analysis.py`.
- **Human verification:** Chạy mã lệnh kiểm toán trên terminal; rà soát correlation ceiling; kiểm tra tính đúng đắn của logic tài chính trong hàm đánh giá ngưỡng.
- **Used in deliverable:** `reports/problem_definition.md`, `notebooks/telecom_retention_analysis.py` (Section 3), `reports/DECISIONS.md` (DEC-014, DEC-015), `reports/EVIDENCE_LEDGER.md` (EVD 28-34).
- **Status:** **PENDING_USER_URL** (Chờ người dùng cập nhật URL thật trước khi nộp).

---



## Hướng dẫn người dùng tạo URL chia sẻ hợp lệ:
1. Mở cuộc trò chuyện trên giao diện web của công cụ AI.
2. Nhấn nút **Share** (Chia sẻ cuộc trò chuyện).
3. Kiểm tra nội dung hiển thị để đảm bảo không lộ thông tin bảo mật/nhạy cảm cá nhân.
4. Chọn **Create link** hoặc **Copy link**.
5. Dán liên kết đó thay thế vào mục `Shared chat URL` ở trên và thêm vào trường References trên Omnicampus khi nộp bài.
