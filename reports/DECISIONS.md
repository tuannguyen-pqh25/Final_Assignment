# DECISIONS LOG — GCI WORLD 2026 FINAL ASSIGNMENT

Nhật ký ghi lại các quyết định kỹ thuật, nghiệp vụ, thiết kế mô hình và giả định quan trọng theo thời gian thực. Mỗi quyết định bao gồm bối cảnh, phương án thay thế, bằng chứng, lý do và trạng thái.

---

## Danh mục quyết định

| ID | Ngày | Giai đoạn | Quyết định | Bằng chứng / Cơ sở | Trạng thái |
|:---|:---|:---|:---|:---|:---|
| **DEC-001** | 2026-10-22 | 0 | Thiết lập cấu trúc workspace chuẩn và bảo toàn dữ liệu gốc | [ChienLuoc.md](file:///d:/Project/Final_Assignment/ChienLuoc.md) mục 138-161; dữ liệu gốc trong `telecom/` được giữ nguyên vẹn | **ACCEPTED** |
| **DEC-002** | 2026-10-22 | 0 | Cố định Random Seed = 42 xuyên suốt dự án | Đảm bảo tính tái lập (reproducibility) cho phân chia tập dữ liệu, mô hình baseline và benchmark | **ACCEPTED** |
| **DEC-003** | 2026-10-22 | 0 | Quy ước đường dẫn tương đối (Relative Path) | Cho phép chạy linh hoạt cả local, Colab hoặc Kaggle mà không phụ thuộc ổ đĩa cụ thể | **ACCEPTED** |
| **DEC-004** | 2026-10-22 | 1 | Sử dụng phép ghép Inner Join trên khóa `Customer_ID` | Kiểm toán chứng minh tập ID trùng khít 100% giữa `Client` và `Record` (100.000 ID, 0 orphan); Inner = Left = Outer | **ACCEPTED** |
| **DEC-005** | 2026-10-22 | 1 | Loại bỏ hoàn toàn `Customer_ID` khỏi không gian biến dự báo | `Customer_ID` là khóa định danh ngẫu nhiên, không có giá trị tổng quát hóa và có thể gây rò rỉ nếu dùng trong model | **ACCEPTED** |
| **DEC-006** | 2026-10-22 | 1 | Bảo lưu các biến có missingness cao (>30%) để đánh giá ablation | 6 cột nhân khẩu học (`numbcars`, `dwllsize`, `HHstatin`, `ownrent`, `dwlltype`, `lor`) có missing cao nhưng mang tín hiệu hộ gia đình; không drop vội vã | **ACCEPTED** |
| **DEC-007** | 2026-10-22 | 1 | Giữ nguyên các giá trị âm mang bản chất nghiệp vụ | `change_mou` và `change_rev` âm thể hiện sự suy giảm tiêu dùng; `eqpdays` âm do ngày kích hoạt trước chu kỳ; không drop dòng | **ACCEPTED** |
| **DEC-008** | 2026-10-22 | 1 | Sử dụng định dạng script Python `.py` (với cú pháp cell `# %%`) song song / thay thế `.ipynb` | Người dùng yêu cầu tạo file `.py` để dễ đọc, dễ diff và tiện copy/paste vào Google Colab; phù hợp mục 1.2 README | **ACCEPTED** |
| **DEC-009** | 2026-10-22 | 2 | Xác lập thị trường viễn thông không dây trưởng thành làm bối cảnh tham chiếu & 4 giả thuyết kinh doanh | Đảm bảo tính khách quan (không tự gán quốc gia cụ thể cho Company A ẩn danh); định hướng kiểm định EDA bằng 4 giả thuyết có nguồn | **ACCEPTED** |
| **DEC-010** | 2026-10-22 | 3 | Xác nhận 5 insight EDA và ưu tiên đòn bẩy vòng đời thiết bị kết hợp suy giảm tiêu dùng | Dữ liệu chứng minh `eqpdays` là yếu tố tương quan mạnh nhất (r=+0,11), H1 & H2 được xác nhận, nhóm ARPU cao gánh 41,8% rủi ro | **ACCEPTED** |
| **DEC-011** | 2026-10-22 | 3 | Chuẩn hóa toàn bộ sản phẩm nộp, biểu đồ, báo cáo và code sang tiếng Anh (English Deliverables Standard) | Yêu cầu chương trình học quốc tế; đảm bảo mọi biểu đồ, slides, notebook comments và báo cáo nộp bằng tiếng Anh chuẩn | **ACCEPTED** |
| **DEC-012** | 2026-10-22 | 3 | Tinh giản biểu đồ trực quan hóa (Bỏ dòng chú thích footer nhỏ in cứng trên hình) | Tránh lỗi cắt viền chữ, tránh rối mắt; thông điệp insight thuộc về tiêu đề slide và nội dung báo cáo | **ACCEPTED** |
| **DEC-013** | 2026-10-22 | 3 | Hợp nhất quy trình phân tích vào MỘT file kịch bản duy nhất `telecom_retention_analysis.py` | Tuân thủ chính xác yêu cầu nộp 1 notebook/script của Omnicampus; tiện copy/paste và chạy liên tục trên Google Colab | **ACCEPTED** |
| **DEC-014** | 2026-10-22 | 4 | Xác lập kiến trúc khung thời gian dự báo (Horizon) và Khoảng đệm tác nghiệp (Lead Time) | Churn 31–60 ngày sau ngày quan sát $T_0$; ngày 1–30 là lead time thực thi chiến dịch giữ chân; loại trừ `Customer_ID`, 98 predictor là thông tin tiền $T_0$ | **ACCEPTED** |
| **DEC-015** | 2026-10-22 | 4 | Thiết lập thứ bậc chỉ số đánh giá gắn với ma trận giá trị kỳ vọng ròng (Expected Value Matrix) | Không dùng duy nhất Accuracy; ROC-AUC (xếp hạng toàn cục), PR-AUC/Lift@20% (hiệu quả chiến dịch), Net Profit (tối ưu ngưỡng $\tau^*$) | **ACCEPTED** |

---

## Chi tiết các quyết định

### DEC-001: Thiết lập cấu trúc workspace chuẩn và bảo toàn dữ liệu gốc
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 0 (Thiết lập workspace & quy tắc dự án)
- **Quyết định:** Tạo cấu trúc thư mục phân tách rõ ràng (`data/raw/`, `data/processed/`, `notebooks/`, `src/`, `reports/`, `slides/`).
- **Bằng chứng / Cơ sở:** Khớp với mục 1.3 và 1.4 của [ChienLuoc.md](file:///d:/Project/Final_Assignment/ChienLuoc.md). Bản gốc trong `telecom/` được giữ nguyên 100% (hash SHA-256 khớp tuyệt đối).
- **Trạng thái:** **ACCEPTED**.

---

### DEC-002: Cố định Random Seed = 42
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 0
- **Quyết định:** Sử dụng `SEED = 42` làm giá trị hạt giống mặc định cho toàn bộ các bước sampling, train_test_split, cross-validation và khởi tạo mô hình.
- **Bằng chứng / Cơ sở:** Tiêu chuẩn tái lập trong khoa học dữ liệu.
- **Trạng thái:** **ACCEPTED**.

---

### DEC-003: Quy ước đường dẫn tương đối (Relative Path)
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 0
- **Quyết định:** Mọi script và notebook phải sử dụng đường dẫn tương đối so với thư mục gốc dự án hoặc tự động dò tìm project root thông qua `pathlib.Path`.
- **Bằng chứng / Cơ sở:** Mục 152 & 156 của [ChienLuoc.md](file:///d:/Project/Final_Assignment/ChienLuoc.md).
- **Trạng thái:** **ACCEPTED**.

---

### DEC-004: Sử dụng phép ghép Inner Join trên khóa `Customer_ID`
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 1 (Kiểm toán dữ liệu và xác nhận join)
- **Quyết định:** Ghép 2 bảng bằng `pd.merge(df_client, df_record, on='Customer_ID', how='inner')`. Kết quả tạo ra bảng 100.000 dòng × 100 cột (khóa chung `Customer_ID` giữ 1 lần).
- **Phương án thay thế:** Dùng Left Join hoặc Outer Join. Không cần thiết vì kết quả cả 3 phép ghép cho số dòng và tập ID hoàn toàn trùng khớp (0 dòng dư, 0 dòng mồ côi).
- **Bằng chứng / Cơ sở:** [notebooks/01_data_audit.ipynb](file:///d:/Project/Final_Assignment/notebooks/01_data_audit.ipynb) Cell 4 và EVD-011 trong [reports/EVIDENCE_LEDGER.md](file:///d:/Project/Final_Assignment/reports/EVIDENCE_LEDGER.md).
- **Trạng thái:** **ACCEPTED**.

---

### DEC-005: Loại bỏ hoàn toàn `Customer_ID` khỏi không gian biến dự báo
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 1
- **Quyết định:** `Customer_ID` chỉ được giữ trong tập dữ liệu phục vụ join, truy vết khách hàng (QA) hoặc phân bổ treatment/control sau này; tuyệt đối không đưa vào ma trận đặc trưng $X$ của mô hình machine learning.
- **Phương án thay thế:** Giữ lại ID làm biến số hoặc thứ tự. Bị loại vì vi phạm nghiêm trọng quy chuẩn phòng chống data leakage và overfitting.
- **Bằng chứng / Cơ sở:** Mục 130 và 233 của [ChienLuoc.md](file:///d:/Project/Final_Assignment/ChienLuoc.md); EVD-009 trong [reports/EVIDENCE_LEDGER.md](file:///d:/Project/Final_Assignment/reports/EVIDENCE_LEDGER.md).
- **Trạng thái:** **ACCEPTED**.

---

### DEC-006: Bảo lưu các biến có missingness cao (>30%) để đánh giá ablation
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 1
- **Quyết định:** Không vội vã loại bỏ 6 cột nhân khẩu học có missing >30% (`numbcars`, `dwllsize`, `HHstatin`, `ownrent`, `dwlltype`, `lor`) ở bước kiểm toán. Ở Giai đoạn 5 (Data Preparation), sẽ thiết kế thử nghiệm ablation (so sánh giữa việc xóa bỏ hoàn toàn vs impute kèm chỉ báo thiếu `_is_missing`).
- **Phương án thay thế:** Tự động drop tất cả các biến có missing >30%. Bị bác bỏ vì việc thiếu dữ liệu nhân khẩu học thường có cấu trúc (MNAR/MAR) và việc khách hàng không cung cấp thông tin cũng có thể là một tín hiệu dự báo.
- **Bằng chứng / Cơ sở:** Mục 252 của [ChienLuoc.md](file:///d:/Project/Final_Assignment/ChienLuoc.md); EVD-014 trong [reports/EVIDENCE_LEDGER.md](file:///d:/Project/Final_Assignment/reports/EVIDENCE_LEDGER.md).
- **Trạng thái:** **ACCEPTED**.

---

### DEC-007: Giữ nguyên các giá trị âm mang bản chất nghiệp vụ
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 1
- **Quyết định:** Giữ nguyên các giá trị âm ở `change_mou` (53.651 dòng), `change_rev` (56.150 dòng) vì đây là các biến phần trăm thay đổi thể hiện sự sụt giảm sử dụng/doanh thu. Với `eqpdays` âm (133 dòng, từ -5 đến -1), sẽ xử lý ở bước tiền xử lý (clip về 0 hoặc coi là thiết bị đăng ký trước ngày kích hoạt). Không xóa dòng dữ liệu khách hàng.
- **Phương án thay thế:** Coi giá trị âm là lỗi nhập liệu và drop 50.000+ dòng. Bị loại vì làm mất hơn một nửa tập dữ liệu và phá hủy tín hiệu hành vi then chốt.
- **Bằng chứng / Cơ sở:** [reports/data_audit.csv](file:///d:/Project/Final_Assignment/reports/data_audit.csv); EVD-016 trong [reports/EVIDENCE_LEDGER.md](file:///d:/Project/Final_Assignment/reports/EVIDENCE_LEDGER.md).
- **Trạng thái:** **ACCEPTED**.

---

### DEC-008: Sử dụng định dạng script Python `.py` với cú pháp cell `# %%`
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 1 (và áp dụng cho tất cả các giai đoạn sau)
- **Quyết định:** Cung cấp mã nguồn dưới dạng file Python `.py` sạch, chia các cell logic bằng cú pháp tiêu chuẩn `# %%` (hỗ trợ interactive window trong VS Code/IDE và dễ dàng copy từng cell hoặc toàn bộ vào Google Colab).
- **Phương án thay thế:** Chỉ tạo file `.ipynb` (JSON thô). Bị thay thế theo yêu cầu người dùng vì file JSON `.ipynb` khó đọc trực tiếp, nặng nề và khó chỉnh sửa nhanh.
- **Bằng chứng / Cơ sở:** Yêu cầu người dùng; Mục 1.2 của [ChienLuoc.md](file:///d:/Project/Final_Assignment/ChienLuoc.md) và README cho phép nộp file `.py` hoặc đóng gói `.zip`.
- **Trạng thái:** **ACCEPTED**.

---

### DEC-009: Xác lập thị trường tham chiếu và 4 giả thuyết kinh doanh phục vụ EDA
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 2 (Nghiên cứu thị trường và hình thành giả thuyết kinh doanh)
- **Quyết định:**
  1. Xác lập bối cảnh thị trường là **Thị trường viễn thông không dây trưởng thành (Mature Wireless Market)** làm thị trường tham chiếu; không tự gán Company A là Việt Nam hay quốc gia cụ thể nào khi chưa có bằng chứng nguồn.
  2. Xác lập 4 giả thuyết kinh doanh có thể kiểm định được bằng dữ liệu thực tế tại Giai đoạn 3 (EDA):
     - **H1 (Consumption Drop):** Khách hàng giảm `change_mou` và `change_rev` có nguy cơ churn cao hơn.
     - **H2 (Equipment Lifecycle):** Khách hàng có `eqpdays` > 365–730 ngày (hết hạn cam kết máy) có rủi ro churn tăng vọt.
     - **H3 (Service Friction):** Khách hàng có nhiều cuộc gọi `custcare_Mean` và rớt mạng `drop_blk_Mean` có tỷ lệ rời mạng cao hơn.
     - **H4 (Household Stickiness):** Khách hàng sở hữu gói đa thuê bao (`actvsubs > 1`) có độ gắn kết cao và tỷ lệ churn thấp hơn.
- **Phương án thay thế:** Tự ý gán Company A là mạng viễn thông tại một quốc gia cụ thể hoặc bắt đầu EDA không có giả thuyết định hướng. Bị loại vì vi phạm nguyên tắc bảo mật của Company A và thiếu định hướng kinh doanh.
- **Bằng chứng / Cơ sở:** [reports/market_brief.md](file:///d:/Project/Final_Assignment/reports/market_brief.md), [reports/SOURCE_LOG.md](file:///d:/Project/Final_Assignment/reports/SOURCE_LOG.md) (SRC-002 đến SRC-005), [reports/EVIDENCE_LEDGER.md](file:///d:/Project/Final_Assignment/reports/EVIDENCE_LEDGER.md) (EVD-017 đến EVD-022).
- **Trạng thái:** **ACCEPTED**.

---

### DEC-010: Xác nhận 5 Insight EDA và lựa chọn đòn bẩy vòng đời thiết bị kết hợp suy giảm tiêu dùng
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 3 (Phân tích khám phá dữ liệu — EDA)
- **Quyết định:**
  1. Xác nhận H1 (Suy giảm tiêu dùng) và H2 (Vòng đời thiết bị) được dữ liệu ủng hộ mạnh mẽ. Trong đó, `eqpdays` là biến đơn lẻ có tương quan và effect size lớn nhất (+16,2 điểm % churn giữa máy cũ và máy mới).
  2. Ghi nhận nghịch lý "Silent Churners" (H3): Khách hàng không gọi tổng đài có tỷ lệ churn cao hơn (51,8%) so với khách hàng gọi nhiều (44,7%). Định hướng đề xuất là giữ chân chủ động trước khi khách hàng ngắt kết nối trong im lặng.
  3. Định vị giải pháp kinh doanh vào phân khúc giá trị cao (ARPU quintile Q5) gánh 41,8% tổng doanh thu rủi ro.
- **Phương án thay thế:** Tập trung can thiệp vào các biến nhân khẩu học nhạy cảm (như thu nhập, chủng tộc, tình trạng hôn nhân). Bị loại bỏ vì rủi ro định kiến/đạo đức và không phải là đòn bẩy có thể hành động được (non-actionable levers).
- **Bằng chứng / Cơ sở:** [reports/eda_summary.md](file:///d:/Project/Final_Assignment/reports/eda_summary.md), 8 biểu đồ trong `reports/figures/`, EVD-023 đến EVD-027 trong [reports/EVIDENCE_LEDGER.md](file:///d:/Project/Final_Assignment/reports/EVIDENCE_LEDGER.md).
- **Trạng thái:** **ACCEPTED**.

---

### DEC-011: Chuẩn hóa toàn bộ sản phẩm nộp, biểu đồ, báo cáo và code sang tiếng Anh
- **Ngày:** 2026-10-22
- **Giai đoạn:** Áp dụng xuyên suốt toàn bộ dự án
- **Quyết định:**
  1. Toàn bộ các sản phẩm dùng để nộp bài và chấm điểm (submission deliverables): Slides, file PDF, mã nguồn Python scripts (`.py`), chú thích code, bảng biểu, tài liệu phân tích (`reports/market_brief.md`, `reports/eda_summary.md`), và 8 biểu đồ trong `reports/figures/` đều được chuẩn hóa 100% bằng tiếng Anh học thuật và kinh doanh chuyên nghiệp.
  2. Ngôn ngữ trao đổi tương tác với người dùng (Chat conversation) được giữ bằng tiếng Việt theo yêu cầu để người dùng nắm bắt và phản biện thuận tiện nhất.
- **Phương án thay thế:** Để lẫn lộn tiếng Việt trên biểu đồ hoặc slides nộp bài. Bị loại vì đây là khóa học và chương trình quốc tế chấm bằng tiếng Anh.
- **Bằng chứng / Cơ sở:** Yêu cầu người dùng và thể lệ cuộc thi GCI World 2026.
- **Trạng thái:** **ACCEPTED**.

---

### DEC-012: Tinh giản biểu đồ trực quan hóa (Loại bỏ footer chú thích in cứng trên ảnh)
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 3 (và áp dụng cho toàn bộ các biểu đồ tiếp theo)
- **Quyết định:** Loại bỏ hoàn toàn các dòng ghi chú `ax.text()` nhỏ li ti ở đáy ảnh của 8 biểu đồ. Đảm bảo ảnh xuất ra tập trung 100% vào dữ liệu (bars, lines, boxes, labels, titles rõ ràng), không bị lỗi cắt viền chữ khi xem hoặc nhúng vào slide. Thông điệp kết luận (takeaways) sẽ được trình bày trực tiếp trong văn bản slide hoặc báo cáo.
- **Phương án thay thế:** Giữ nguyên chú thích nhỏ dưới đáy biểu đồ. Bị loại bỏ vì gây rối mắt, chiếm diện tích và dễ bị crop mép ảnh.
- **Bằng chứng / Cơ sở:** Phản hồi của người dùng và tiêu chuẩn thiết kế slide consulting chuyên nghiệp.
- **Trạng thái:** **ACCEPTED**.

---

### DEC-013: Hợp nhất quy trình phân tích vào MỘT file kịch bản duy nhất `telecom_retention_analysis.py`
- **Ngày:** 2026-10-22
- **Giai đoạn:** Áp dụng xuyên suốt từ Giai đoạn 3 đến Giai đoạn 11
- **Quyết định:** Duy trì và cập nhật liên tục một file mã nguồn duy nhất: `notebooks/telecom_retention_analysis.py`. Mỗi giai đoạn mới (Stage 4, 5, 6, 7...) sẽ nối tiếp vào file này dưới dạng các Section rõ ràng (`# %% [markdown]`, `# %%`).
- **Phương án thay thế:** Chia nhỏ thành nhiều file rời rạc (`01_...`, `02_...`, `03_...`). Bị loại bỏ vì vi phạm thể lệ chấm điểm nộp bài của Omnicampus (chỉ cho phép nộp 1 file notebook/script) và gây phiền phức khi copy sang Google Colab.
- **Bằng chứng / Cơ sở:** Yêu cầu người dùng và quy chế nộp bài tại Mục 1.2 của [ChienLuoc.md](file:///d:/Project/Final_Assignment/ChienLuoc.md).
- **Trạng thái:** **ACCEPTED**.

---

### DEC-014: Xác lập kiến trúc khung thời gian dự báo (Horizon) và Khoảng đệm tác nghiệp (Lead Time)
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 4 (Định nghĩa bài toán và rà soát rò rỉ dữ liệu)
- **Quyết định:**
  1. Xác lập biến mục tiêu `churn` là biến nhị phân đo lường việc khách hàng rời mạng trong khoảng thời gian từ **31 đến 60 ngày sau ngày quan sát $T_0$**.
  2. Xác lập khoảng đệm thời gian từ **ngày 1 đến ngày 30 sau $T_0$** là **Cửa sổ can thiệp tác nghiệp (Operational Intervention Window)**: Đây là khoảng thời gian sống còn để hệ thống CRM chấm điểm rủi ro, phân loại thuê bao và triển khai các chiến dịch giữ chân chủ động (tặng voucher đổi máy, tái cấu trúc gói cước) trước khi khách hàng bước vào cửa sổ rời mạng.
  3. Kiểm toán feature-by-feature xác nhận toàn bộ 98 biến dự báo đều là dữ liệu lịch sử hoặc trạng thái phát sinh trước hoặc tại $T_0$. Loại bỏ hoàn toàn `Customer_ID`. Mức tương quan tuyệt đối tối đa giữa các biến số với `churn` là $r = 0,1127$ (`eqpdays`), không có bất kỳ biến nào rò rỉ thông tin tương lai ($r > 0,20$).
- **Phương án thay thế:** Coi ngày dự báo trùng với ngày rời mạng. Bị bác bỏ vì trong viễn thông, khi khách hàng đã quyết định rời mạng tại ngày $T$ thì đã quá muộn để can thiệp giữ chân; thiết kế khoảng đệm 30 ngày là chuẩn mực công nghiệp để hành động có tính khả thi.
- **Bằng chứng / Cơ sở:** [ENG_Company _A_ Dataset Overview.md](file:///d:/Project/Final_Assignment/ENG_Company%20_A_%20Dataset%20Overview.md) dòng 77; [reports/problem_definition.md](file:///d:/Project/Final_Assignment/reports/problem_definition.md) Mục 2 & 3; EVD-028 đến EVD-031.
- **Trạng thái:** **ACCEPTED**.

---

### DEC-015: Thiết lập thứ bậc chỉ số đánh giá gắn với ma trận giá trị kỳ vọng ròng (Expected Value Matrix)
- **Ngày:** 2026-10-22
- **Giai đoạn:** Giai đoạn 4 (Định nghĩa bài toán và rà soát rò rỉ dữ liệu)
- **Quyết định:**
  1. Thiết lập thứ bậc chỉ số đánh giá mô hình phân tầng theo mục tiêu kinh doanh:
     - **Chỉ số xếp hạng toàn cục (Primary Ranking Metric):** **ROC-AUC** — đo lường năng lực phân biệt khách hàng rời mạng độc lập với việc chọn ngưỡng và không bị ảnh hưởng bởi tỷ lệ cơ sở (base rate).
     - **Chỉ số hiệu quả chiến dịch (Operational Metric):** **PR-AUC (Average Precision)** và **Precision / Lift @ Top 20% (Decile 1 & 2)** — đo lường mức độ tập trung khách hàng churn thực tế trong ngân sách tiếp cận hữu hạn của đội ngũ CSKH.
     - **Chỉ số tối ưu hóa lợi nhuận (Financial ROI Metric):** **Net Expected Retained Profit** dựa trên ma trận chi phí - lợi ích:
       $$\text{Net Profit}(\tau) = \text{TP} \times (V_{\text{retained}} \times S - C_{\text{retention}}) - \text{FP} \times C_{\text{subsidy}} - N_{\text{targeted}} \times C_{\text{outreach}}$$
       Ngưỡng phân loại tối ưu $\tau^*$ sẽ được chọn để tối đa hóa số tiền giữ chân ròng thay vì ngưỡng mặc định 0,5.
     - **Chỉ số chẩn đoán (Diagnostic Metrics):** Báo cáo Accuracy, Recall, F1-Score tại ngưỡng tối ưu $\tau^*$ và ngưỡng chuẩn 0,5.
  2. Ghi nhận đặc điểm mẫu quan sát cân bằng 50/50 (49,56% churn): Phản ánh quy trình lấy mẫu case-control có chủ đích của Company A (so với mức tự nhiên 1–1,5%/tháng). Mô hình học tốt trật tự rủi ro tương đối, nhưng khi tính toán lợi nhuận toàn mạng cần hiệu chỉnh xác suất theo định lý Bayes.
- **Phương án thay thế:** Chỉ sử dụng duy nhất Accuracy để đánh giá mô hình. Bị loại bỏ vì Accuracy coi chi phí bỏ sót một khách hàng churn (False Negative, mất hàng trăm USD CLV) ngang bằng với việc tặng thừa một ưu đãi cho khách hàng trung thành (False Positive, tốn vài chục USD chiết khấu).
- **Bằng chứng / Cơ sở:** Mục 233 của [ChienLuoc.md](file:///d:/Project/Final_Assignment/ChienLuoc.md); [reports/problem_definition.md](file:///d:/Project/Final_Assignment/reports/problem_definition.md) Mục 5; EVD-032 đến EVD-034.
- **Trạng thái:** **ACCEPTED**.

