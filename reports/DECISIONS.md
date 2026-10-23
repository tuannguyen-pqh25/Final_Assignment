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
| **DEC-016** | 2026-10-23 | 5 | Phân chia tập dữ liệu 70% Train / 15% Val / 15% Test phân tầng và cô lập hoàn toàn tập Test | Đảm bảo tính khách quan (unbiased); tập test (15.000 dòng) được khóa chặt, không dùng để tune/chọn feature/ngưỡng | **ACCEPTED** |
| **DEC-017** | 2026-10-23 | 5 | Áp dụng chiến lược Missing Indicators thay vì loại bỏ biến khuyết thiếu cao | Thực nghiệm ablation chứng minh giữ nguyên 6 biến missing >30% kết hợp MissingIndicator tăng +0,51% ROC-AUC so với drop | **ACCEPTED** |
| **DEC-018** | 2026-10-23 | 5 | Xây dựng 12 đặc trưng nghiệp vụ gắn với 4 giả thuyết EDA (H1–H4) và phân tầng rủi ro | Tính toán thuần túy hàng-ngang (row-wise) tại $T_0$, không rò rỉ tương lai; tăng thêm +0,62% ROC-AUC (+1,13% tổng cộng) | **ACCEPTED** |
| **DEC-019** | 2026-10-23 | 6 | Lựa chọn HistGradientBoostingClassifier làm mô hình quán quân (Champion Model) | Vượt trội hoàn toàn Dummy (0,5000) và LogReg (0,6392) với Val ROC-AUC 0,6903 và Test ROC-AUC 0,6964; Lift Top 20% đạt 1,46x | **ACCEPTED** |
| **DEC-020** | 2026-10-23 | 6 | Tối ưu hóa ngưỡng phân loại tác nghiệp $\tau^* = 0,25$ theo Ma trận Chi phí - Lợi ích | Tăng lợi nhuận ròng giữ chân thêm +$90.977 (+26,2%) trên 15k khách hàng nhờ bù đắp bất đối xứng chi phí $C_{FN} >> C_{FP}$ | **ACCEPTED** |

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

---

### DEC-016: Phân chia tập dữ liệu 70% Train / 15% Val / 15% Test phân tầng và cô lập hoàn toàn tập Test
- **Ngày:** 2026-10-23
- **Giai đoạn:** Giai đoạn 5 (Data Preparation & Controlled Feature Pipeline)
- **Quyết định:**
  1. Phân chia 100.000 bản ghi thành 3 tập dữ liệu độc lập có kích thước nguyên tuyệt đối:
     - **Training Set (`X_train`, `y_train`):** 70.000 khách hàng (70,0%) — dùng để fit imputer, scaler, encoder và huấn luyện mô hình.
     - **Validation Set (`X_val`, `y_val`):** 15.000 khách hàng (15,0%) — dùng để so sánh thuật toán, tinh chỉnh siêu tham số và tối ưu hóa ngưỡng cắt $\tau^*$.
     - **Held-Out Test Set (`X_test`, `y_test`):** 15.000 khách hàng (15,0%) — **KHÓA CHẶT (LOCKED)**. Tuyệt đối không can thiệp, không fit bất kỳ transformer nào, chỉ đánh giá đúng 1 lượt ở Giai đoạn 6 / Giai đoạn 11.
  2. Toàn bộ các bước chia mẫu đều áp dụng `stratify=y` (đảm bảo tỷ lệ churn đạt 49,56% đồng nhất trên cả 3 tập) và cố định `random_state=42` (DEC-002).
- **Phương án thay thế:** Chia 80/20 train/test thông thường rồi tune trên test. Bị loại vì vi phạm nguyên tắc chống rò rỉ dữ liệu (overfitting vào test set).
- **Bằng chứng / Cơ sở:** [reports/feature_decisions.md](file:///d:/Project/Final_Assignment/reports/feature_decisions.md) Mục 6; [notebooks/telecom_retention_analysis.py](file:///d:/Project/Final_Assignment/notebooks/telecom_retention_analysis.py) Cell 4.3; EVD-035.
- **Trạng thái:** **ACCEPTED**.

---

### DEC-017: Áp dụng chiến lược Missing Indicators thay vì loại bỏ biến khuyết thiếu cao
- **Ngày:** 2026-10-23
- **Giai đoạn:** Giai đoạn 5 (Data Preparation & Controlled Feature Pipeline)
- **Quyết định:**
  1. Không xóa bỏ 6 biến nhân khẩu học có missing >30% (`numbcars`, `dwllsize`, `HHstatin`, `ownrent`, `dwlltype`, `lor`).
  2. Triển khai kiến trúc xử lý khuyết thiếu kép thông qua `sklearn.compose.ColumnTransformer`:
     - Biến số (Numerical): `SimpleImputer(strategy='median', add_indicator=True)` kết hợp `StandardScaler()`. Việc thêm cờ `MissingIndicator` giúp mô hình nhận biết được thuê bao nào không khai báo thông tin tài sản.
     - Biến phân loại (Categorical): `SimpleImputer(strategy='constant', fill_value='Missing')` kết hợp `OneHotEncoder(handle_unknown='ignore', sparse_output=False)`.
  3. Mọi imputer/scaler chỉ được `fit()` trên `X_train` và `transform()` trên `X_val`/`X_test`.
- **Phương án thay thế:** Tự động loại bỏ toàn bộ các cột có missing >30%. Bị bác bỏ vì thực nghiệm đối sánh (ablation test) cho thấy phương án loại bỏ chỉ đạt ROC-AUC **0,6278**, trong khi phương án giữ lại kèm Missing Indicator đạt ROC-AUC **0,6329** (+0,0051 điểm % ROC-AUC).
- **Bằng chứng / Cơ sở:** [reports/feature_decisions.md](file:///d:/Project/Final_Assignment/reports/feature_decisions.md) Mục 3; [notebooks/telecom_retention_analysis.py](file:///d:/Project/Final_Assignment/notebooks/telecom_retention_analysis.py) Cell 4.4 - 4.6; EVD-036.
- **Trạng thái:** **ACCEPTED**.

---

### DEC-018: Xây dựng 12 đặc trưng nghiệp vụ gắn với 4 giả thuyết EDA (H1–H4) và phân tầng rủi ro
- **Ngày:** 2026-10-23
- **Giai đoạn:** Giai đoạn 5 (Data Preparation & Controlled Feature Pipeline)
- **Quyết định:** Xây dựng hàm tiền xử lý `engineer_telecom_features(df)` tạo ra 12 biến đặc trưng mang tính giải thích và hành động cao:
  - Nhóm Vòng đời thiết bị (H2): `eqpdays_years`, `eqp_over_1yr`, `eqp_over_2yr`, `eqp_to_tenure_ratio`.
  - Nhóm Suy giảm tiêu dùng (H1): `severe_mou_drop`, `severe_rev_drop`.
  - Nhóm Ma sát giá & Sốc cước: `rev_per_mou`, `overage_rev_ratio`.
  - Nhóm Tương tác CSKH & Silent Churners (H3): `silent_churner_flag`, `drop_per_call`.
  - Nhóm Cấu trúc tài khoản & Doanh thu rủi ro (H4 & Value-at-Risk): `multi_line_flag`, `high_arpu_tier`.
  Tất cả các biến đều được tính toán thuần túy trên từng hàng (row-wise) tại thời điểm $T_0$, không sử dụng thống kê tổng hợp chéo giữa các hàng, triệt tiêu hoàn toàn rò rỉ dữ liệu.
- **Phương án thay thế:** Chỉ sử dụng 98 biến thô nguyên bản. Bị loại vì thực nghiệm chứng minh 12 biến nghiệp vụ giúp nâng ROC-AUC của Logistic Regression từ 0,6329 lên **0,6391** (+0,0062 điểm %; tích lũy +0,0113 so với baseline).
- **Bằng chứng / Cơ sở:** [reports/feature_decisions.md](file:///d:/Project/Final_Assignment/reports/feature_decisions.md) Mục 4; [notebooks/telecom_retention_analysis.py](file:///d:/Project/Final_Assignment/notebooks/telecom_retention_analysis.py) Cell 4.1 & 4.6; EVD-037.
- **Trạng thái:** **ACCEPTED**.

---

### DEC-019: Lựa chọn HistGradientBoostingClassifier làm mô hình quán quân (Champion Model)
- **Ngày:** 2026-10-23
- **Giai đoạn:** Giai đoạn 6 (Benchmark và chọn mô hình Machine Learning)
- **Quyết định:**
  1. Thiết lập bộ benchmark 4 họ thuật toán: `DummyClassifier` (mốc tối thiểu), `LogisticRegression` (mốc tuyến tính giải thích), `RandomForestClassifier` (bagging ensemble), và `HistGradientBoostingClassifier` (boosting gradient cây quyết định dạng histogram).
  2. Lựa chọn `HistGradientBoostingClassifier(max_iter=150, max_depth=6, min_samples_leaf=30, l2_regularization=1.0)` làm mô hình quán quân (Champion Model) để triển khai thực tế.
  3. Mô hình đạt ROC-AUC **0,6903** và PR-AUC **0,6772** trên tập Validation (15.000 mẫu); vượt qua bài kiểm toán tổng quát hóa độc lập trên tập Held-out Test (15.000 mẫu) với ROC-AUC **0,6964** và PR-AUC **0,6865** (chênh lệch < 0,0061, hoàn toàn không suy giảm/overfitting).
  4. Năng lực phân loại theo phân vị (Decile Lift): Nhóm 20% rủi ro cao nhất (Decile 1 & 2) đạt mật độ churn **72,53%** (so với tỷ lệ cơ sở 49,56%), mang lại hệ số **Lift = 1,46x**.
- **Bằng chứng / Cơ sở:** [reports/model_benchmarks.md](file:///d:/Project/Final_Assignment/reports/model_benchmarks.md) Mục 2; [notebooks/telecom_retention_analysis.py](file:///d:/Project/Final_Assignment/notebooks/telecom_retention_analysis.py) Section 5; EVD-039 đến EVD-042; Fig 9.
- **Trạng thái:** **ACCEPTED**.

---

### DEC-020: Tối ưu hóa ngưỡng phân loại tác nghiệp $\tau^* = 0,25$ theo Ma trận Chi phí - Lợi ích
- **Ngày:** 2026-10-23
- **Giai đoạn:** Giai đoạn 6 (Benchmark và chọn mô hình Machine Learning)
- **Quyết định:**
  1. Bác bỏ việc áp dụng ngưỡng phân loại mặc định $\tau = 0,50$ cho chiến dịch giữ chân khách hàng.
  2. Xác lập ngưỡng phân loại tác nghiệp tối ưu $\tau^* = 0,25$ dựa trên hàm mục tiêu tối đa hóa Lợi nhuận Giữ chân Ròng Kỳ vọng (Expected Net Retained Profit):
     - Chi phí bỏ sót 1 khách hàng churn ($C_{\text{FN}} \approx \$126 - \$504$ giá trị CLV biên mất đi) lớn hơn rất nhiều chi phí tặng nhầm ưu đãi cho 1 khách hàng không churn ($C_{\text{FP}} \approx \$35$ voucher chiết khấu + $\$3$ phí liên hệ).
     - Việc hạ ngưỡng cắt về $\tau^* = 0,25$ giúp mở rộng tỷ lệ bao phủ khách hàng churn từ 64,6% lên **97,24%** (bắt trúng 7.229 / 7.434 khách hàng rời mạng trên tập validation).
  3. Giá trị kinh tế gia tăng: Lợi nhuận giữ chân ròng tăng từ **$346.585,14** (ở $\tau = 0,50$) lên **$437.562,36** (ở $\tau^* = 0,25$), mang lại khoản thặng dư ròng **+$90.977,22 (+26,2%)** trên mỗi 15.000 thuê bao tiếp cận.
- **Phương án thay thế:** Giữ nguyên ngưỡng cắt 0,50 để tối đa hóa Accuracy. Bị bác bỏ vì tối ưu Accuracy bỏ lọt hơn 35% khách hàng rời mạng, gây thất thoát tài chính nghiêm trọng cho nhà mạng.
- **Bằng chứng / Cơ sở:** [reports/model_benchmarks.md](file:///d:/Project/Final_Assignment/reports/model_benchmarks.md) Mục 5; [notebooks/telecom_retention_analysis.py](file:///d:/Project/Final_Assignment/notebooks/telecom_retention_analysis.py) Cell 5.4 - 5.5; EVD-043 đến EVD-045; Fig 10.
- **Trạng thái:** **ACCEPTED**.

---


### DEC-021: Thiết lập Khung phân loại Tính khả thi Hành động (Actionability Framework) và Phân định Nhân quả
- **Ngày:** 2026-10-23
- **Giai đoạn:** Giai đoạn 7 (Model Interpretation, Robustness & Actionability Audit)
- **Quyết định:**
  1. Tuyệt đối không đồng nhất Permutation Feature Importance với quan hệ nhân quả (Causality). Tầm quan trọng của feature chỉ phản ánh mức độ phụ thuộc dự báo thống kê của mô hình trên dữ liệu quan sát lịch sử, không chứng minh việc thay đổi giá trị biến sẽ trực tiếp làm giảm churn.
  2. Thiết lập ranh giới phân loại 3 nhóm biến trong không gian đặc trưng:
     - **Đòn bẩy chiến lược can thiệp được (Actionable Levers):** Các yếu tố nhà mạng có thể chủ động tác động qua chính sách giá, ưu đãi thiết bị, hoặc tối ưu kỹ thuật: `eqpdays` (trợ giá nâng cấp máy), `change_mou` (tối ưu gói cước rightsizing), `rev_per_mou` / `overage_rev_ratio` (xóa bỏ sốc cước/chuyển đổi gói không giới hạn), `drop_vce_Mean` / `drop_per_call` (xử lý điểm lõm sóng và bù cước dịch vụ).
     - **Tín hiệu bối cảnh quan sát (Observational Signals):** Các cột mốc vòng đời tự nhiên không thể can thiệp trực tiếp: `months` (thời gian thuê bao gắn bó chỉ dùng để kích hoạt thời điểm tái ký hợp đồng tháng thứ 11/23), `totmrc_Mean` (mức cước cam kết dùng để định mức ngân sách ưu đãi), `avgmou`, `avgqty`, `mou_Mean`.
     - **Thuộc tính nhạy cảm đạo đức (Sensitive / Demographic):** `ethnic`, `income`, `marital`, `lor`, `ownrent` — được cô lập và cấm sử dụng trong tác nghiệp marketing.
  3. Mọi giải pháp giữ chân ở Giai đoạn 8 bắt buộc phải đi kèm thiết kế thử nghiệm A/B có nhóm đối chứng ngẫu nhiên (Holdout Control Group) để đo lường độ nâng gia tăng thực tế (incremental uplift).
- **Phương án thay thế:** Tuyên bố mô hình tìm ra nguyên nhân gốc rễ và đề xuất can thiệp vào mọi biến có importance cao (kể cả tenure và nhân khẩu). Bị bác bỏ vì ngụy biện nhân quả sẽ dẫn đến thất bại chiến dịch trong thực tế.
- **Bằng chứng / Cơ sở:** [reports/model_interpretation.md](file:///d:/Project/Final_Assignment/reports/model_interpretation.md) Mục 2 & 3; [notebooks/telecom_retention_analysis.py](file:///d:/Project/Final_Assignment/notebooks/telecom_retention_analysis.py) Section 6.1 - 6.2; EVD-046, EVD-047; Fig 11.
- **Trạng thái:** **ACCEPTED**.

---

### DEC-022: Thiết lập Tường lửa Đạo đức (Ethical Firewall) và Tiêu chuẩn Ổn định Phân khúc (Subgroup Robustness)
- **Ngày:** 2026-10-23
- **Giai đoạn:** Giai đoạn 7 (Model Interpretation, Robustness & Actionability Audit)
- **Quyết định:**
  1. **Tường lửa đạo đức (Ethical & Anti-discrimination Firewall):** Nghiêm cấm tuyệt đối việc sử dụng các biến nhân khẩu học nhạy cảm (`ethnic` chủng tộc, `income` thu nhập ước tính, `marital` tình trạng hôn nhân, `ownrent` sở hữu nhà) làm tiêu chí chọn mẫu, lọc danh sách tiếp cận hoặc định giá ưu đãi trong các chiến dịch giữ chân.
  2. Chiến dịch giữ chân chỉ được phép nhắm mục tiêu dựa trên 3 trụ cột kỹ thuật khách quan:
     - **Mức độ rủi ro (Risk Tier):** Xác suất churn dự báo $\ge \tau^* = 0,25$.
     - **Triệu chứng hành vi cần can thiệp (Actionable Trigger):** Máy cũ $>365$ ngày, sụt giảm tiêu dùng $<-100$ phút, tỷ lệ cước phạt phát sinh $>20\%$.
     - **Giá trị kinh tế (ARPU / CLV Tier):** Đảm bảo chi phí ưu đãi không vượt quá 70% giá trị biên đóng góp hàng tháng.
  3. **Tiêu chuẩn ổn định phân khúc (Subgroup Robustness):** Nghiệm thu chất lượng mô hình trên 15.000 mẫu validation:
     - ROC-AUC ổn định từ **0,6370** đến **0,7363** trên mọi nhóm thiết bị, phân vị doanh thu, số dòng thuê bao và thời gian gắn bó, vượt qua cổng chất lượng tối thiểu $\ge 0,6000$ (không xảy ra hiện tượng sụp đổ thuật toán ở bất kỳ phân khúc nào).
     - Tính bất biến theo quy mô tài khoản: Thuê bao đơn (Single-line, AUC = 0,6910) và Đa thuê bao (Multi-line, AUC = 0,6890) có năng lực phân loại tương đương (chênh lệch $< 0,0020$).
     - Độ phủ tiếp cận toàn diện: Tại ngưỡng $\tau^* = 0,25$, mô hình bắt trúng từ **91,51% đến 99,82%** khách hàng rời mạng trên tất cả các phân khúc tác nghiệp.
- **Phương án thay thế:** Không kiểm toán phân khúc và sử dụng mọi thuộc tính cá nhân để tối đa hóa AUC. Bị bác bỏ vì vi phạm chuẩn mực đạo đức AI, rủi ro pháp lý chống phân biệt đối xử và nguy cơ thiên lệch mô hình.
- **Bằng chứng / Cơ sở:** [reports/model_interpretation.md](file:///d:/Project/Final_Assignment/reports/model_interpretation.md) Mục 4; [notebooks/telecom_retention_analysis.py](file:///d:/Project/Final_Assignment/notebooks/telecom_retention_analysis.py) Section 6.3; EVD-048 đến EVD-050; Fig 12.
- **Trạng thái:** **ACCEPTED**.

---

### DEC-023: Lựa chọn Ưu tiên Chiến lược Cốt lõi (Project Phoenix) và Khung Tác nghiệp Giữ chân Đa tầng (Value-Tier Routing)
- **Ngày:** 2026-10-23
- **Giai đoạn:** Giai đoạn 8 (Thiết kế Business Proposal và Định lượng Tác động Tài chính)
- **Quyết định:**
  1. **Hội tụ vào MỘT ưu tiên chiến lược duy nhất:** Khởi động *"Project Phoenix: Chương trình Trợ giá Nâng cấp Thiết bị Chủ động & Tối ưu Gói cước"* (Proactive Handset Upgrade & Tariff Rightsizing Retention Program).
     - Bác bỏ phương án dàn trải ngân sách vào nhiều thử nghiệm marketing phân mảnh; tập trung nguồn lực giải quyết điểm nghẽn nghiêm trọng nhất đã được xác thực qua EDA và Model: Vực thẳm churn khi thiết bị cũ quá 1 năm (`eqpdays` > 365 ngày, churn 53,8%–57,9%, EVD-023; feature rank 2, EVD-046) và sụt giảm tiêu dùng đột ngột (`change_mou` < -100 phút, churn 53,6%, EVD-024; feature rank 3, EVD-046).
  2. **Quy trình tác nghiệp phân tầng theo Giá trị Thuê bao (Value-Tier Routing):**
     - Áp dụng Tường lửa đạo đức (DEC-022): Tuyệt đối không dùng biến nhân khẩu học (`ethnic`, `income`, `marital`) để chọn mẫu hay định giá ưu đãi.
     - Phân bổ kênh tiếp cận và chi phí ưu đãi theo mức đóng góp biên thực tế:
       * **Phân tầng Giá trị Cao (ARPU > $75, chiếm 41,8% rủi ro):** Điều phối sang Bàn Concierge Chăm sóc Đặc biệt (Outbound Phone Concierge), ưu đãi voucher $50 nâng cấp máy 5G kèm cam kết tái ký hợp đồng 12 tháng.
       * **Phân tầng Trung bình (ARPU $40–$75, chiếm 45,2% rủi ro):** Kênh số tự động qua MyCompanyA Mobile App và Email cá nhân hóa, voucher $35 đổi máy + tối ưu gói cước rightsizing không cước phạt phát sinh.
       * **Phân tầng Tăng trưởng / Cơ bản (ARPU < $40, chiếm 13,0% rủi ro):** SMS tương tác tự động và cổng web tự phục vụ, voucher $25 phụ kiện/thiết bị + gói cước trọn gói (flat-rate).
  3. **Chủ thể chịu trách nhiệm (Program Ownership):** Trực tiếp thuộc quyền điều hành của Phó Tổng Giám đốc Thương mại (CCO) / Trưởng bộ phận Giữ chân Khách hàng (Head of Retention), phối hợp liên phòng ban với Data Science (chấm điểm định kỳ hàng tuần), Marketing (thiết kế ưu đãi), và Chuỗi cung ứng (phân bổ máy 5G từ đối tác OEM).
- **Phương án thay thế:** Triển khai đại trà ưu đãi giảm giá cước chung cho toàn bộ thuê bao hoặc chỉ can thiệp bị động khi khách gọi lên tổng đài. Bị bác bỏ vì EDA chứng minh 51,8% khách rời mạng trong im lặng (EVD-025), và giảm cước đại trà gây thất thoát biên lợi nhuận nghiêm trọng (deadweight loss).
- **Bằng chứng / Cơ sở:** [reports/business_proposal.md](file:///d:/Project/Final_Assignment/reports/business_proposal.md) Mục 1, 2, 3; EVD-023, EVD-024, EVD-025, EVD-027, EVD-046; Fig 11.
- **Trạng thái:** **ACCEPTED**.

---

### DEC-024: Khung Quản trị Tài chính Đa Kịch bản (Multi-Scenario ROI Governance) và Thử nghiệm Đối chứng Ngẫu nhiên (Randomized Holdout Pilot)
- **Ngày:** 2026-10-23
- **Giai đoạn:** Giai đoạn 8 (Thiết kế Business Proposal và Định lượng Tác động Tài chính)
- **Quyết định:**
  1. **Tuyệt đối chống ngụy biện quy kết (Zero Attribution Fallacy):** Nghiêm cấm quy đổi trực tiếp các chỉ số kỹ thuật của mô hình (ROC-AUC 0,6964 hay Accuracy 64,1%) thành tỷ lệ khách hàng được giữ chân hay doanh thu gia tăng. Doanh thu giữ chân chỉ phát sinh khi có hành động can thiệp kinh doanh thực tế tác động làm thay đổi hành vi của khách hàng.
  2. **Mô hình tài chính 3 kịch bản minh bạch (3-Scenario Economic Model):**
     - Xây dựng bảng dự phóng tài chính với công thức đại số tường minh trên 2 quy mô: Thử nghiệm Pilot (15.000 thuê bao) và Vận hành Toàn niên (100.000 thuê bao):
       * **Kịch bản Thận trọng (Conservative):** Retention Uplift = 15%, Take-up = 25%, ARPU = $55, Margin = 65%, $C_{\text{voucher}} = \$40$, $C_{\text{outreach}} = \$4$. Pilot mang lại **+$256.635,90** lợi nhuận ròng (ROI 122,9%); Quy mô năm mang lại **+$1.810.769,00** lợi nhuận ròng (ROI 140,1%).
       * **Kịch bản Cơ sở (Base Case):** Retention Uplift = 25%, Take-up = 35%, ARPU = $58,35, Margin = 70%, $C_{\text{voucher}} = \$35$, $C_{\text{outreach}} = \$3$. Pilot mang lại **+$660.236,19** lợi nhuận ròng (ROI 291,9%); Quy mô năm mang lại **+$4.501.233,28** lợi nhuận ròng (ROI 319,7%). Chi phí giữ chân một khách hàng (CPRS) là **$116,77** (rẻ hơn 3x–5x so với CAC $350–$600).
       * **Kịch bản Lạc quan (Optimistic):** Retention Uplift = 35%, Take-up = 45%, ARPU = $62, Margin = 75%, $C_{\text{voucher}} = \$30$, $C_{\text{outreach}} = \$2,50$. Pilot mang lại **+$1.176.232,20** lợi nhuận ròng (ROI 497,2%); Quy mô năm mang lại **+$7.940.946,00** lợi nhuận ròng (ROI 537,6%).
  3. **Biên an toàn vượt trội (Break-even Frontier):** Điểm hòa vốn chương trình chỉ yêu cầu tỷ lệ giữ chân gia tăng đạt từ **5,49% đến 6,73%**. So với chuẩn ngành viễn thông đạt từ 20% đến 35%, dự án có biên an toàn (margin of safety) lớn hơn **3,0x**, đảm bảo khả năng sinh lời ngay cả trong điều kiện biên lợi nhuận bị ép xuống 55%.
  4. **Kiến trúc Thử nghiệm Đối chứng Ngẫu nhiên (Randomized Controlled Holdout Trial):**
     - Bắt buộc triển khai Pilot trên 15.000 thuê bao nguy cơ cao ($\hat{p} \ge 0,25$): Chia ngẫu nhiên **90% Nhóm can thiệp (Treatment Group, $N=13.500$)** nhận ưu đãi Project Phoenix và **10% Nhóm đối chứng giữ nguyên (Holdout Control Group, $N=1.500$)** hoàn toàn không can thiệp (business-as-usual).
     - Đo lường độ nâng gia tăng thực tế thuần túy (Pure Incremental Uplift) = Churn Nhóm Đối chứng − Churn Nhóm Can thiệp. Đảm bảo lực thống kê $>80\%$ để phát hiện hiệu quả $\ge 4,5\%$ ở mức ý nghĩa $\alpha = 0,05$. Chỉ khi Pilot đạt ý nghĩa thống kê và lợi nhuận ròng $> \$250.000$ mới được mở rộng quy mô toàn mạng.
- **Phương án thay thế:** Giả định toàn bộ khách hàng churn được mô hình nhận diện đều sẽ ở lại mạng và tính ROI hàng chục triệu USD không cần thử nghiệm. Bị bác bỏ vì vi phạm chuẩn mực quản trị tài chính doanh nghiệp, che giấu rủi ro kinh doanh và không kiểm chứng được thực tế.
- **Bằng chứng / Cơ sở:** [reports/business_proposal.md](file:///d:/Project/Final_Assignment/reports/business_proposal.md) Mục 4, 5, 6; [notebooks/telecom_retention_analysis.py](file:///d:/Project/Final_Assignment/notebooks/telecom_retention_analysis.py) Section 7; [notebooks/07_business_proposal_roi_model.py](file:///d:/Project/Final_Assignment/notebooks/07_business_proposal_roi_model.py); Fig 13; EVD-051 đến EVD-056.
- **Trạng thái:** **ACCEPTED**.

