# CHIẾN LƯỢC HOÀN THÀNH GCI WORLD 2026 FINAL ASSIGNMENT

> **Mục đích:** Hoàn thành bài Final Assignment theo hướng tư vấn kinh doanh dựa trên dữ liệu, có EDA thực chất, mô hình ML phù hợp, tác động kinh doanh định lượng, slide dành cho lãnh đạo và notebook có thể tái lập. Làm theo từng giai đoạn; không yêu cầu AI Agent giải quyết toàn bộ trong một lượt.
>
> **Nguyên tắc:** Dữ liệu trước, kết luận sau. Không bịa kết quả, nguồn, điểm mô hình, chi phí, ROI hoặc insight. Mọi con số đưa lên slide phải truy ngược được về notebook, nguồn công khai hoặc giả định được ghi rõ.

---

## 1. Mục tiêu, phạm vi và điều kiện nộp

### 1.1 Bối cảnh assignment

Theo README và Dataset Overview được cung cấp, vai trò là associate tại một công ty tư vấn IT. Company A là nhà cung cấp dịch vụ viễn thông ẩn danh, có dữ liệu khách hàng nhưng năng lực ML nội bộ hạn chế. Bài làm không chỉ báo cáo kỹ thuật; cần xác định vấn đề kinh doanh từ EDA và phân tích thị trường, xây ít nhất một mô hình ML/thống kê, rồi đề xuất giải pháp có tác động định lượng.

### 1.2 Các sản phẩm bắt buộc

1. **Slide deck PDF:** tối đa **15 slide tổng cộng**, tính cả trang tiêu đề, mục lục, trang phân cách và references. Khuyến nghị dùng đủ 15 slide chỉ khi mỗi slide đóng góp rõ ràng.
2. **Notebook tái lập:** `.ipynb` hoặc `.py`; nếu có nhiều file có thể đóng gói `.zip`. Phải chứa quy trình phân tích có thể chạy lại, không chỉ ảnh chụp kết quả.
3. **References:** nhập danh sách URL/trích dẫn vào trường References trên Omnicampus; mỗi nguồn một dòng. Danh sách này phải khớp với citations trên slide.
4. **AI conversation URL:** nếu dùng AI tạo sinh, README yêu cầu đưa URL lịch sử chat vào References. Hãy lấy URL thật từ giao diện của người dùng; Agent không được tự bịa URL.

**Tên file nộp:**
- `[OmnicampusAccountName].pdf`
- `[OmnicampusAccountName].ipynb` hoặc `[OmnicampusAccountName].py` hoặc `[OmnicampusAccountName].zip`

Thay `OmnicampusAccountName` bằng đúng account name trên Omnicampus trước khi nộp. PDF tối đa 10 MB.

### 1.3 Lịch triển khai nội bộ gợi ý

| Khoảng thời gian | Giai đoạn | Mốc nghiệm thu |
|---|---|---|
| 22–24/10/2026 | 0–1 | Workspace, data audit, xác nhận join/target |
| 25–28/10/2026 | 2 | Market brief, nguồn đã xác minh, giả thuyết |
| 29/10–03/11/2026 | 3 | EDA và evidence ledger đủ mạnh |
| 04–06/11/2026 | 4–5 | Problem definition, leakage review, preprocessing pipeline |
| 07–12/11/2026 | 6 | Benchmark model, metric và score tái lập |
| 13–15/11/2026 | 7 | Interpretation, robustness, actionable segments |
| 16–18/11/2026 | 8 | Proposal, impact model, assumptions và pilot plan |
| 19–21/11/2026 | 9 | Storyboard được duyệt, tối đa 15 slide |
| 22–24/11/2026 | 10 | Slide deck và PDF đã render/kiểm tra |
| 25–26/11/2026 | 11 | Notebook run-all, traceability, References, submission pack |
| 27/11/2026 | Buffer | Sửa lỗi cuối; không thêm phân tích rủi ro cao nếu không cần thiết |

Lịch này là kế hoạch nội bộ chứ không phải hạn chính thức. Ưu tiên hoàn tất toàn bộ đầu ra trước hạn ít nhất 24–48 giờ để còn thời gian sửa lỗi và nộp lại nếu cần.

### 1.4 Hạn nộp

README ghi hạn **28/11/2026 lúc 11:30 UTC**, tương đương **28/11/2026 lúc 18:30 giờ Việt Nam (UTC+7)**. Không chờ đến hạn mới kiểm tra; đặt mốc hoàn tất nội bộ sớm hơn ít nhất 24–48 giờ.

### 1.5 Rubric phải được đáp ứng rõ ràng

- Đề xuất kinh doanh cụ thể, không dừng ở technical report.
- Insight dựa trên EDA thật của dữ liệu Company A.
- Ít nhất một mô hình phù hợp; trên slide ghi **tên mô hình + metric + score** bằng chữ rõ ràng.
- Giải thích vì sao chọn mô hình, cách xây dựng, cách đánh giá và insight định lượng phục vụ quyết định.
- Market analysis dùng nguồn ngoài có thể kiểm chứng, trích dẫn trên slide và trong References.
- Nhiều biểu đồ có mục đích, không chỉ trình bày số liệu thô.
- Mạch lập luận nhất quán: thị trường → EDA → vấn đề → mô hình → đề xuất → tác động → kế hoạch kiểm chứng.
- Ngôn ngữ dành cho executive không có nền tảng ML; giải thích thuật ngữ kỹ thuật bằng ngôn ngữ kinh doanh.

### 1.6. Khai báo việc sử dụng Generative AI và đính kèm URL lịch sử chat

README cho phép sử dụng generative AI, nhưng yêu cầu **đưa URL lịch sử chat vào trường References trên Omnicampus**. Không được bỏ qua bước này nếu có dùng ChatGPT hoặc công cụ AI tạo sinh khác. URL phải là liên kết thật do người dùng tạo trên nền tảng; AI Agent không thể tự đoán, tự sinh hay tuyên bố đã tạo liên kết thay người dùng.

#### Cách tạo URL lịch sử ChatGPT trên máy tính

1. Mở cuộc trò chuyện ChatGPT thực sự đã hỗ trợ bài assignment (ví dụ: cuộc trò chuyện dùng để lập kế hoạch, viết/sửa code, giải thích mô hình hoặc phản biện proposal).
2. Nhấn **Share** ở phía trên cuộc trò chuyện; nếu giao diện hiện lựa chọn chia sẻ khác, chọn thao tác chia sẻ cuộc trò chuyện chứ không chỉ chia sẻ riêng một câu trả lời.
3. Xem trước nội dung sắp chia sẻ, kiểm tra tiêu đề, phần hội thoại và mọi dữ liệu/ảnh/file có thể hiển thị.
4. Chọn **Create link** hoặc **Copy link** (tùy trạng thái/giao diện). Mở hoặc dán liên kết vào một cửa sổ riêng để kiểm tra nó truy cập được.
5. Sao chép URL có dạng `https://chatgpt.com/share/...` vào `reports/AI_USAGE_LOG.md` và danh sách References. Không tự thay phần `...` bằng ID phỏng đoán.
6. Nếu tiếp tục bổ sung nội dung sau khi tạo link, mở lại **Share** và dùng **Update link** nếu muốn liên kết phản ánh phiên bản mới nhất; xác minh lại trước khi nộp.

Tài liệu hướng dẫn chính thức: [Sharing conversations and scheduled tasks in ChatGPT — OpenAI Help Center](https://help.openai.com/en/articles/7925741-sharing-conversations-and-scheduled-tasks-in-chatgpt).

#### Cần tạo link cho những cuộc trò chuyện nào?

- Ghi lại các cuộc hội thoại AI **đã có ảnh hưởng thực chất** đến phân tích, code, lựa chọn mô hình, business proposal, thiết kế slide hoặc nội dung cuối.
- Khuyến nghị tạo một mục cho mỗi cuộc hội thoại quan trọng; đừng tạo hàng loạt link không liên quan chỉ để tăng số lượng.
- Nếu dùng nhiều nền tảng AI, lưu URL lịch sử/conversation permalink của từng nền tảng nếu công cụ đó hỗ trợ. Nếu không hỗ trợ link lịch sử, ghi nền tảng và cách truy cập/tài liệu thay thế, nhưng không bịa một URL.
- Tham khảo FAQ, yêu cầu của giảng viên và giao diện Omnicampus khi nhập References. Nếu có giới hạn trường nhập, ưu tiên các hội thoại có đóng góp trực tiếp và rõ ràng; không được xóa các nguồn dữ liệu/phương pháp bên ngoài để nhường chỗ cho link AI.

#### Mẫu ghi vào `reports/AI_USAGE_LOG.md`

```text
Platform: ChatGPT
Conversation purpose: Lập kế hoạch / EDA / model evaluation / business proposal / slide review (chọn và mô tả đúng)
Date accessed: YYYY-MM-DD
Shared chat URL: [DÁN URL THẬT Ở ĐÂY]
Contribution used: [Mô tả ngắn phần ý tưởng/code/biên tập đã tham khảo]
Human verification: [Cách bạn tự kiểm tra bằng dữ liệu, chạy code hoặc đối chiếu nguồn]
Used in deliverable: [Notebook cell/section, report, slide number]
```

Thay toàn bộ phần trong ngoặc vuông bằng thông tin thật trước khi nộp. Không để placeholder như `[DÁN URL THẬT Ở ĐÂY]` trong submission cuối.

#### Quyền riêng tư và tính trung thực

- Với link chia sẻ từ tài khoản cá nhân, **bất kỳ ai có link đều có thể xem nội dung được chia sẻ**. Hãy kiểm tra trước khi chia sẻ và không để lộ thông tin cá nhân nhạy cảm, mật khẩu, thông tin tài khoản hoặc nội dung không cần thiết.
- Link chia sẻ là snapshot tại thời điểm tạo/cập nhật; nội dung mới thường không tự thêm vào link snapshot đã tạo.
- URL chat chứng minh việc tham khảo AI, không thay thế citation cho số liệu thị trường, phương pháp, bài báo hoặc tài liệu ngoài. Mọi nguồn bên ngoài vẫn phải được trích dẫn riêng trên slide và trong References.
- Bạn phải hiểu, kiểm tra và chịu trách nhiệm với phần nội dung sử dụng. Không trình bày văn bản hoặc code AI đề xuất như kết quả thực nghiệm nếu chưa chạy và xác minh.

---

## 2. Hiện trạng dữ liệu đã kiểm tra

Các thông tin dưới đây là **kết quả kiểm tra sơ bộ thực tế** từ các CSV được cung cấp, không phải kết luận phân tích cuối cùng:

| Thành phần | Kết quả sơ bộ |
|---|---:|
| `Client.csv` | 100.000 dòng × 50 cột |
| `Record.csv` | 100.000 dòng × 51 cột |
| `Customer_ID` | 100.000 ID duy nhất trong mỗi bảng; không thấy ID thiếu hoặc trùng |
| Giao nhau giữa hai bảng | 100.000 ID; chưa thấy bản ghi chỉ tồn tại ở một bảng |
| Số cột sau inner join | Dự kiến 100 cột (khóa chung chỉ giữ một lần) |
| `churn = 1` | 49.562 khách hàng, khoảng 49,56% |
| `churn = 0` | 50.438 khách hàng, khoảng 50,44% |
| Missing nổi bật trong `Client.csv` | `numbcars` 49.366; `dwllsize` 38.308; `HHstatin` 37.923; `ownrent` 33.706; `dwlltype` 31.909 |
| Missing nổi bật trong `Record.csv` | `change_mou`/`change_rev`: 891 mỗi cột; nhiều biến usage/revenue: 357 mỗi cột |

Tỷ lệ churn tương đối cân bằng khiến accuracy có thể hữu ích, nhưng **không được chỉ dùng accuracy**. Phải so sánh với baseline và xem ROC-AUC, precision, recall, F1, confusion matrix; cân nhắc PR-AUC, calibration và chi phí sai lầm tùy quyết định kinh doanh.

### Những điểm cần kiểm tra, không được mặc định

- README/Dataset Overview mô tả `churn` là churn xảy ra trong khoảng **31–60 ngày sau ngày quan sát**. Agent phải xác định phạm vi thời gian của các feature và rà soát khả năng leakage trước khi mô hình hóa.
- `eqpdays` (tuổi thiết bị), các biến doanh thu, mức sử dụng và liên hệ chăm sóc khách hàng là các **ứng viên để kiểm tra**, không phải insight đã được xác nhận hoặc quan hệ nhân quả.
- Một số biến nhân khẩu học/tài chính và trường có missing rất cao có thể kém ổn định hoặc nhạy cảm. Không giữ chúng chỉ vì tăng điểm; phải giải thích giá trị, rủi ro và tính phù hợp trong quyết định kinh doanh.
- Dataset Overview nói Company A là doanh nghiệp ẩn danh; tài liệu được cung cấp không xác nhận thị trường địa lý. **Không được tự khẳng định đây là dữ liệu của Việt Nam hoặc quốc gia cụ thể** nếu không có nguồn xác minh. Nếu chọn một thị trường làm bối cảnh đề xuất, phải nêu rõ đó là thị trường tham chiếu/giả định.
- `Customer_ID` chỉ dùng để ghép/kiểm soát chất lượng; loại khỏi feature model.

---

## 3. Chiến lược làm việc theo giai đoạn

**Quy tắc điều hành:** Mỗi lần chỉ yêu cầu Agent thực hiện **một giai đoạn**. Agent phải tạo đủ các deliverable của giai đoạn, chạy kiểm tra nghiệm thu, ghi quyết định và dừng. Chỉ chuyển giai đoạn khi người dùng đã xem kết quả hoặc chủ động yêu cầu tiếp tục. Không viết toàn bộ notebook và slide một cách hấp tấp trong một lượt.

### Giai đoạn 0 — Thiết lập workspace và quy tắc dự án

**Mục tiêu:** Tạo nền tảng để các bước sau có tổ chức, dễ theo dõi và không làm mất file gốc.

**Việc cần làm:**
- Kiểm tra cấu trúc thư mục, file hiện có và môi trường chạy (local/Colab/Kaggle); không di chuyển hoặc sửa file gốc nếu chưa cần.
- Tạo cấu trúc tối thiểu phù hợp, ví dụ:
  - `data/raw/` — dữ liệu gốc, giữ nguyên.
  - `notebooks/` — notebook phân tích chính.
  - `src/` — hàm xử lý tái sử dụng nếu thực sự cần.
  - `reports/figures/` — biểu đồ xuất ra.
  - `reports/` — nhật ký phát hiện, giả định, model results, nguồn.
  - `slides/` — nguồn slide và PDF xuất.
- Tạo `reports/DECISIONS.md`, `reports/EVIDENCE_LEDGER.md`, `reports/SOURCE_LOG.md`.
- Thiết lập seed, package/version notes, đường dẫn tương đối và cách chạy lại.

**Deliverables:** cấu trúc thư mục; `reports/DECISIONS.md`; checklist môi trường; hướng dẫn chạy.

**Nghiệm thu:** file gốc còn nguyên; đường dẫn không phụ thuộc đường dẫn tuyệt đối của một máy; có thể xác định rõ file nào là nguồn, notebook chính và đầu ra.

**Prompt Agent:**
```text
Thực hiện GIAI ĐOẠN 0 của ChienLuoc.md, chỉ làm giai đoạn này. Trước tiên hãy kiểm kê workspace và file có sẵn; không ghi đè/xóa/di chuyển dữ liệu gốc. Tạo cấu trúc thư mục tối thiểu, DECISIONS.md, EVIDENCE_LEDGER.md, SOURCE_LOG.md và hướng dẫn chạy phù hợp môi trường hiện tại. Đừng tạo phân tích giả hoặc placeholder trông như kết quả thật. Cuối cùng báo cáo file đã tạo, đường dẫn, lệnh chạy, giả định và checklist nghiệm thu. DỪNG, không chuyển giai đoạn tiếp theo.
```

### Giai đoạn 1 — Kiểm toán dữ liệu và xác nhận join

**Mục tiêu:** Chứng minh dữ liệu đủ tin cậy trước khi vẽ biểu đồ hay train model.

**Việc cần làm:**
- Load hai CSV với encoding và dtype phù hợp; kiểm tra shape, tên cột, dtype, khóa, ID trùng/thiếu, duplicate row, tập ID giao nhau và kết quả join.
- Kiểm tra domain/range, số âm bất thường, giá trị sentinel, kiểu categorical, tỷ lệ missing; phân biệt NaN thật với chuỗi có nội dung giống `nan`.
- Xác nhận `churn` chỉ có các lớp hợp lệ và target không thiếu.
- Lưu kết quả audit thành bảng tái lập; không xóa hàng/cột dựa trên cảm tính.

**Deliverables:** phần notebook “Data audit”; `reports/data_audit.csv` hoặc bảng tương đương; ghi chú quality issues và hướng xử lý được đề xuất.

**Nghiệm thu:** số dòng/cột, khóa join và target distribution được tính từ code; mọi biến bị loại/đổi dtype có lý do; không thay đổi dữ liệu gốc.

**Prompt Agent:**
```text
Thực hiện GIAI ĐOẠN 1 theo ChienLuoc.md. Chỉ kiểm toán dữ liệu và kiểm chứng join của Client.csv/Record.csv; chưa làm EDA sâu, chưa train model, chưa tạo slide. Tất cả kết quả định lượng phải được tính bằng code và lưu lại trong notebook/artefact. Kiểm tra khóa Customer_ID, duplicate, missingness, dtype, phạm vi giá trị, target churn và kết quả inner/left join. Nêu rõ mọi bất thường, cách phát hiện và phương án xử lý đề xuất; không tự ý làm sạch không có bằng chứng. Chạy lại cell từ đầu để xác minh. Cập nhật EVIDENCE_LEDGER.md và DECISIONS.md. DỪNG sau báo cáo nghiệm thu.
```

### Giai đoạn 2 — Nghiên cứu thị trường và hình thành giả thuyết kinh doanh

**Mục tiêu:** Đặt bài toán dữ liệu vào bối cảnh ngành phù hợp mà không gán nhầm địa lý cho dataset.

**Việc cần làm:**
- Đọc kỹ assignment/tutor, xác định câu hỏi kinh doanh cần được giải quyết cho nhà điều hành viễn thông.
- Tìm nguồn đáng tin cậy và hiện hành: cơ quan quản lý, ITU/GSMA, báo cáo ngành có phương pháp rõ ràng, báo cáo thường niên hoặc nghiên cứu học thuật. Chỉ lấy dữ kiện liên quan trực tiếp đến retention/churn, chi phí thu hút khách, doanh thu thuê bao, chăm sóc khách hàng, thiết bị hoặc bối cảnh đã chọn.
- Với mỗi nguồn, lưu URL, tên tổ chức/tác giả, ngày xuất bản, ngày truy cập, luận điểm được sử dụng và slide dự kiến trích dẫn.
- Soạn 2–4 giả thuyết có thể kiểm định bằng dữ liệu, ví dụ: thay đổi usage/revenue, tuổi thiết bị, tín hiệu customer care hoặc thời gian sử dụng có liên quan đến churn/giá trị khách hàng không. Đây là giả thuyết, không phải kết luận.
- Vì danh tính/thị trường của Company A chưa được xác nhận, không chuyển số liệu thị trường tham chiếu thành số liệu riêng của Company A.

**Deliverables:** market brief 1–2 trang; bảng nguồn có chất lượng; 2–4 giả thuyết và phép kiểm định tương ứng.

**Nghiệm thu:** các luận điểm thị trường quan trọng đều có nguồn; nguồn trùng khớp nội dung được trích; đã đánh dấu dữ kiện, suy luận và giả định riêng biệt.

**Prompt Agent:**
```text
Thực hiện GIAI ĐOẠN 2 theo ChienLuoc.md. Hãy nghiên cứu web để tạo market brief ngắn, có nguồn mới và đáng tin cậy, nhằm hỗ trợ đề xuất cho một doanh nghiệp viễn thông ẩn danh. Trước hết kiểm tra xem tài liệu có xác định quốc gia/thị trường không; nếu không, tuyệt đối không khẳng định dữ liệu thuộc Việt Nam hay quốc gia nào. Có thể dùng thị trường tham chiếu nhưng phải ghi rõ đây là bối cảnh/giả định, không phải thông tin nội bộ Company A. Ưu tiên nguồn chính thức/học thuật/báo cáo ngành có ngày phát hành và phương pháp; lưu URL, ngày, số liệu chính xác, giới hạn áp dụng và cách trích dẫn. Không bịa nguồn hoặc số liệu. Đưa ra 2–4 giả thuyết có thể kiểm tra bằng dataset, chưa kết luận trước EDA. Cập nhật SOURCE_LOG.md và EVIDENCE_LEDGER.md. Chỉ làm giai đoạn này rồi DỪNG.
```

### Giai đoạn 3 — EDA để tìm insight có ý nghĩa kinh doanh

**Mục tiêu:** Khám phá dữ liệu có hệ thống và tìm ra các khoảng cách/hành vi đáng kiểm chứng.

**Việc cần làm:**
- Tổng quan target, missingness, phân phối, outliers, cardinality, correlation/collinearity và các nhóm khách hàng.
- Tạo biểu đồ có mục tiêu: churn balance; missingness; so sánh feature trọng yếu theo churn; phân nhóm/decile; biến động doanh thu/usage; thiết bị; customer care; heatmap/correlation khi hữu ích.
- Dùng thống kê phù hợp để hỗ trợ biểu đồ; báo cáo cả kích thước mẫu và độ lớn khác biệt, không chỉ p-value.
- Xem xét phân phối lệch, log scale hoặc cap/winsorization chỉ khi có lý do và ghi rõ ảnh hưởng.
- Kiểm tra các phân đoạn có cơ hội hành động được, tránh suy luận nhân quả từ tương quan.
- Không dùng pairplot trên toàn bộ 100.000 bản ghi; lấy mẫu có seed khi biểu đồ quá nặng.

**Deliverables:** notebook EDA; ít nhất 5–8 biểu đồ có chất lượng nếu chúng trả lời câu hỏi khác nhau; bảng tóm tắt 5 insight tiềm năng với số liệu và caveat.

**Nghiệm thu:** mỗi hình có tiêu đề dạng thông điệp, tên biến/đơn vị/legend rõ; các insight được tính từ dữ liệu và có thể tái tạo; phân biệt rõ quan sát với diễn giải.

**Prompt Agent:**
```text
Thực hiện GIAI ĐOẠN 3 theo ChienLuoc.md, dùng kết quả audit đã nghiệm thu. Chỉ làm EDA, chưa chốt chiến lược kinh doanh, chưa train model và chưa làm slide cuối. Mỗi biểu đồ phải trả lời một câu hỏi cụ thể và có đơn vị/legend/n, không tạo chart để trang trí. Tìm quan hệ với churn cùng các biến kinh doanh tiềm năng; kiểm tra outliers, missingness, tương quan và khác biệt theo phân đoạn. Với insight ứng viên, ghi số liệu thực, effect size hoặc chênh lệch hữu ích, số lượng quan sát và caveat. Không gọi tương quan là quan hệ nhân quả; không dùng demographic làm khuyến nghị targeting nếu chưa xem rủi ro. Xuất hình độ phân giải cao và cập nhật EVIDENCE_LEDGER.md. Chạy notebook từ đầu đến cuối phần EDA và DỪNG.
```

### Giai đoạn 4 — Chốt business problem, target, và kiểm soát data leakage

**Mục tiêu:** Chọn câu hỏi hẹp, quan trọng và có thể hành động; mọi bước ML phải phục vụ câu hỏi đó.

**Mặc định ưu tiên để kiểm định:** dự đoán `churn` để giúp nhóm retention ưu tiên khách hàng có nguy cơ cao trong khoảng dự báo được mô tả trong dữ liệu. Chỉ giữ hướng này sau khi EDA và kiểm tra thời điểm feature xác nhận tính hợp lý. Nếu kết quả chỉ ra vấn đề khác phù hợp hơn, Agent phải trình bày bằng chứng và lý do trước khi đổi bài toán.

**Việc cần làm:**
- Viết một câu business question bằng ngôn ngữ executive.
- Xác định target, observation window, prediction horizon, đối tượng sử dụng output và hành động cụ thể sau prediction.
- Xem xét từng cột: có biết được vào thời điểm ra quyết định không? Có thể chứa thông tin sau sự kiện hoặc proxy gần như trực tiếp của target không?
- Loại `Customer_ID` khỏi feature; không dùng dữ liệu phát sinh sau thời điểm dự đoán. Rà soát các biến tổng hợp có thể chứa thông tin thời gian chồng lấn với churn.
- Chọn metric dựa trên cân bằng target và chi phí false positive/false negative.

**Deliverables:** 1 trang problem definition; bảng target/feature timing/leakage decisions; tiêu chí đánh giá mô hình gắn với quyết định.

**Nghiệm thu:** giải thích được mô hình sẽ giúp ai làm gì; target/horizon rõ; quyết định loại feature có bằng chứng; không rò rỉ test set hoặc tương lai vào train.

**Prompt Agent:**
```text
Thực hiện GIAI ĐOẠN 4 theo ChienLuoc.md. Dựa trên EDA thật để chốt business question, target, prediction horizon, người sử dụng và action. Churn là giả thuyết ưu tiên chứ không phải điều bắt buộc nếu dữ liệu phản bác nó. Rà soát feature-by-feature về thời điểm có sẵn và khả năng leakage theo mô tả churn 31–60 ngày sau observation date; không suy đoán thời điểm thiếu bằng chứng. Loại Customer_ID khỏi modeling features. Đề xuất metric theo trade-off kinh doanh; vì target gần cân bằng nên accuracy có thể báo cáo nhưng không được là metric duy nhất. Ghi rõ những điểm còn bất định, cập nhật DECISIONS.md và EVIDENCE_LEDGER.md. Không train model ở giai đoạn này. DỪNG.
```

### Giai đoạn 5 — Data preparation và feature engineering có kiểm soát

**Mục tiêu:** Xây pipeline sạch, tránh leakage, chịu được dữ liệu mới và có thể tái lập.

**Việc cần làm:**
- Phân biệt numeric, categorical, binary, identifier và cột quá thiếu/khó giải thích.
- Xây preprocessing bằng pipeline: imputation fit trên train; encoding phù hợp; scaling nếu mô hình cần; xử lý unseen category; tránh fit preprocessing trên toàn bộ dataset trước split.
- So sánh việc loại biến missing cao với imputing có indicator; không tự động drop chỉ vì missing cao.
- Cân nhắc feature engineering mang ý nghĩa nghiệp vụ (delta, ratio, tenure/usage trend) chỉ khi tính được tại thời điểm dự đoán, hợp lý và không nhân đôi/leak target.
- Xây train/validation/test tách biệt và stratify theo target. Chỉ test một lần ở vòng đánh giá cuối; không dùng test để chọn feature/threshold/hyperparameter.

**Deliverables:** pipeline preprocessing; bảng feature giữ/bỏ và lý do; notebook cells chạy được từ raw data.

**Nghiệm thu:** không có leakage do preprocessing; xử lý được NaN và category lạ; random seed cố định; test set được giữ riêng; không hard-code kết quả đã nhìn thấy.

**Prompt Agent:**
```text
Thực hiện GIAI ĐOẠN 5 theo ChienLuoc.md. Tạo preprocessing pipeline reproducible từ raw data đã audit: phân loại cột, xử lý missing, categorical encoding, loại ID/leakage và feature engineering có luận cứ. Mọi imputer/encoder/scaler phải fit chỉ trên training data (ví dụ qua sklearn Pipeline/ColumnTransformer). So sánh có giải thích các cách xử lý missing cao; không drop biến tùy tiện. Chia train/validation/test hoặc thiết kế CV hợp lý, stratify nếu classification và giữ test set độc lập. Tạo bảng quyết định feature. Viết kiểm tra assertion cho shape, target và không có Customer_ID trong X. Chạy toàn bộ bước preparation. Chưa tối ưu mô hình hoặc làm slide. DỪNG.
```

### Giai đoạn 6 — Benchmark và chọn mô hình ML

**Mục tiêu:** Chứng minh model có giá trị dự đoán so với baseline và chọn mô hình phù hợp với use case.

**Bộ so sánh đề xuất cho classification:**
1. `DummyClassifier` làm baseline tối thiểu.
2. Logistic Regression làm mốc dễ giải thích.
3. Một mô hình phi tuyến phù hợp dữ liệu bảng như XGBoost/HistGradientBoosting/Random Forest/CatBoost, tùy package sẵn có và chất lượng pipeline. Không cần cố cài tất cả; chọn mô hình có căn cứ và chạy ổn định.

**Việc cần làm:**
- Báo cáo tên model, preprocessing, split, seed, metric và score.
- Tối ưu hyperparameter chỉ trên train/validation hoặc cross-validation.
- Báo cáo tối thiểu ROC-AUC, precision, recall, F1, accuracy và confusion matrix; thêm PR-AUC/Brier/calibration nếu liên quan.
- So sánh sai lầm false positive/false negative theo đề xuất retention.
- Xem xét threshold theo chi phí/nguồn lực thay vì mặc định 0.5; ghi rõ threshold được chọn từ validation, không tối ưu trên test.
- Ghi thời gian chạy, giới hạn tính toán và khả năng triển khai.

**Deliverables:** bảng model comparison; confusion matrix; metric plot; model artifact nếu thực sự cần; code để rerun experiments.

**Nghiệm thu:** có baseline; metric được tính trên split đúng; score không bị dùng để tune test; slide sau này sẽ ghi rõ model + metric + score; số liệu chạy lại gần như giống nhau.

**Prompt Agent:**
```text
Thực hiện GIAI ĐOẠN 6 theo ChienLuoc.md. Chỉ benchmark mô hình bằng pipeline và split đã nghiệm thu. Với classification, bắt buộc có DummyClassifier, Logistic Regression và tối thiểu một mô hình phi tuyến phù hợp với dữ liệu bảng (chọn theo package/compute và giải thích). Báo cáo metric đã được tính thật: ROC-AUC, precision, recall, F1, accuracy, confusion matrix; bổ sung PR-AUC/calibration nếu hữu ích. Tune chỉ trên train/validation hoặc CV, không chọn threshold dựa trên test. Báo cáo cả score và trade-off kinh doanh, không kết luận model tốt chỉ vì accuracy. Ghi seed, phiên bản thư viện, thời gian chạy, thông số chính và đường dẫn kết quả. Không bịa output khi code chưa chạy. Cập nhật EVIDENCE_LEDGER.md. DỪNG sau nghiệm thu.
```

### Giai đoạn 7 — Model interpretation, robustness và actionability

**Mục tiêu:** Biến model thành bằng chứng hữu ích; xác định tín hiệu có thể tác động, không diễn giải feature importance thành quan hệ nhân quả.

**Việc cần làm:**
- Dùng permutation importance/SHAP hoặc feature importance phù hợp; kiểm tra ổn định trên nhiều lần chạy/fold hoặc khi loại feature thống trị.
- Kiểm tra metric theo các nhóm nghiệp vụ hợp lý (ví dụ tenure, usage/revenue band, thiết bị) nếu sample đủ; xem precision/recall theo phân đoạn để biết mô hình có thể hữu ích ở đâu.
- Không diễn giải mã categorical như số liên tục nếu encoder tạo thứ tự giả.
- Xem xét bias/privacy và tránh đưa quyết định nhạy cảm chỉ dựa trên ethnic, income, marital hoặc proxy không phù hợp.
- Tách biệt **predictive signal** (dự đoán được) với **actionable lever** (doanh nghiệp có thể can thiệp). Kiểm tra thêm insight EDA trước khi đề xuất hành động.

**Deliverables:** top features với ý nghĩa kinh doanh và caveat; bảng hiệu quả theo phân đoạn; danh sách yếu tố có thể hành động/không hành động; robustness note.

**Nghiệm thu:** không tuyên bố nhân quả; không dựa vào một feature importance duy nhất để chốt chiến lược; khuyến nghị dựa trên tín hiệu có thể can thiệp và kiểm chứng.

**Prompt Agent:**
```text
Thực hiện GIAI ĐOẠN 7 theo ChienLuoc.md. Giải thích model bằng permutation importance/SHAP hoặc phương pháp thích hợp; kiểm tra độ ổn định và chất lượng theo các segment đủ mẫu. Với mỗi feature quan trọng, nói rõ: bằng chứng đo được, cách diễn giải hợp lý, liệu doanh nghiệp có thể tác động hay không, nguy cơ proxy/bias và caveat. Không gọi importance là causality. Không xây chiến dịch targeting dựa riêng vào ethnicity/income/marital hoặc biến nhạy cảm. So sánh các phát hiện model với EDA; nếu mâu thuẫn thì ghi nhận. Cập nhật EVIDENCE_LEDGER.md, xuất biểu đồ có thể dùng trên slide. Chưa tạo deck cuối; DỪNG.
```

### Giai đoạn 8 — Thiết kế business proposal và định lượng tác động

**Mục tiêu:** Đề xuất hành động cụ thể, có đối tượng, thời điểm, quy trình, KPI, rủi ro và economic case.

**Cấu trúc khuyến nghị:**
- Mục tiêu kinh doanh và nhóm chịu trách nhiệm.
- Hành động theo risk tier/segment mà EDA và model hỗ trợ; action phải khả thi, phù hợp những feature có thể tác động (ví dụ thử nghiệm ưu đãi/upgrade/chăm sóc chủ động chỉ nếu kết quả dữ liệu và market research hỗ trợ).
- Quy trình sử dụng score: cập nhật dữ liệu → tính risk → chọn danh sách theo năng lực vận hành → liên hệ/offer → đo kết quả.
- Pilot có nhóm thử nghiệm và nhóm holdout ngẫu nhiên để ước lượng retention uplift gia tăng. Không tuyên bố model tự gây ra tăng doanh thu.
- Định nghĩa KPI: churn rate ở treatment/control, incremental retention, revenue/contribution retained, cost per contact, offer redemption, net benefit, ROI và guardrail chỉ số khách hàng.

**Khung tính tác động (dùng công thức, không điền số bịa):**
- `N_targeted` = số khách đủ điều kiện được nhắm đến.
- `p_churn` = churn risk/baseline churn probability thích hợp cho nhóm triển khai.
- `uplift` = phần tăng thêm xác suất giữ chân nhờ can thiệp; phải ước lượng bằng thử nghiệm hoặc nêu là giả định kịch bản.
- `N_saved_incremental = N_targeted × p_churn × uplift` (nếu uplift được định nghĩa là tỷ lệ churn giảm tương đối trong nhóm có nguy cơ; nếu định nghĩa theo điểm phần trăm thì phải đổi công thức tương ứng và ghi rõ).
- `Contribution_per_saved_customer` = contribution margin tháng × số tháng giữ chân kỳ vọng; nếu chỉ có revenue proxy, không gọi là profit.
- `Gross_benefit = N_saved_incremental × Contribution_per_saved_customer`.
- `Net_benefit = Gross_benefit − campaign_cost − incentive_cost − implementation_cost`.
- `ROI = Net_benefit / Total_cost`; ghi rõ nếu ROI không xác định khi total cost bằng 0.

Xây kịch bản conservative/base/upside và sensitivity theo uplift, margin, cost, horizon. Nếu dữ liệu không có chi phí, margin, hoặc intervention uplift, ghi rõ đó là giả định cần xác minh trong pilot, không trình bày như dữ kiện Company A. Nên xác định break-even uplift để lãnh đạo hiểu điều kiện thành công.

**Deliverables:** bản business proposal; bảng giả định/công thức; kịch bản impact; KPI và design pilot.

**Nghiệm thu:** mỗi con số có nguồn hoặc nhãn assumption; model metric không bị chuyển thẳng thành ROI; có cách kiểm chứng thực tế; đề xuất có owner, hành động, timeline, KPI và rủi ro.

**Prompt Agent:**
```text
Thực hiện GIAI ĐOẠN 8 theo ChienLuoc.md. Chuyển insight EDA/model đã nghiệm thu thành một đề xuất business cụ thể, tập trung vào một ưu tiên chính. Phải mô tả ai làm gì với đầu ra model, đối tượng mục tiêu, quy trình, chi phí/nguồn lực, KPI, rủi ro và pilot. Tính business impact bằng công thức minh bạch và ít nhất ba kịch bản conservative/base/upside; nêu từng giả định, đơn vị, horizon và nguồn. Nếu không có margin/cost/uplift thực của Company A thì không được giả vờ biết; hãy dùng giả định rõ ràng, làm sensitivity và nêu cần xác thực bằng A/B test/holdout. Không dùng accuracy/AUC như thể đó là tỷ lệ churn được ngăn chặn hoặc doanh thu tăng. Tạo bảng impact có thể kiểm tra từng ô và cập nhật EVIDENCE_LEDGER.md. DỪNG.
```

### Giai đoạn 9 — Xây storyline và storyboard tối đa 15 slide

**Mục tiêu:** Chuyển báo cáo nghiên cứu thành một câu chuyện thuyết phục lãnh đạo.

**Storyboard khởi điểm (15 slide tối đa):**
1. **Title + recommendation headline:** tên đề xuất và quyết định mong muốn.
2. **Executive summary:** vấn đề, giải pháp, model evidence, impact range và điều kiện/giả định quan trọng.
3. **Market context:** 2–3 dữ kiện thị trường hỗ trợ nhu cầu; citations ngay trên slide.
4. **Company A & data opportunity:** nguồn dữ liệu, quy mô, giới hạn, câu hỏi quyết định.
5. **EDA — churn/business baseline:** quy mô target và vấn đề có ý nghĩa với kinh doanh.
6. **EDA — key discovery:** insight phân đoạn hoặc hành vi nổi bật có số liệu thực.
7. **Problem framing & proposed decision workflow:** target, prediction horizon và model output được sử dụng ra sao.
8. **Model approach:** lý do chọn model, split, preprocessing, metric và chống leakage.
9. **Model results:** bảng benchmark; tên model + metric + score; confusion matrix/ROC hoặc hình phù hợp.
10. **Drivers & actionable segments:** 3–5 tín hiệu chính và khả năng hành động/caveat.
11. **Recommended intervention:** chiến lược hành động chính và vận hành.
12. **Quantified business case:** conservative/base/upside, assumptions, break-even/sensitivity.
13. **Pilot & implementation roadmap:** giai đoạn 30/60/90 ngày hoặc khung phù hợp, owner, KPI, holdout.
14. **Risks, governance & decision requested:** data privacy, model drift, fairness, cost, dependency, điều kiện go/no-go.
15. **References:** các nguồn đã trích dẫn trên deck và nguồn bổ sung cần thiết.

Không bắt buộc dùng đúng 15 slide. Nếu storyline cần gọn hơn, rút số slide nhưng không bỏ requirement. Tránh slide mục lục/phân cách nếu không thêm giá trị.

**Deliverables:** `slides/storyboard.md` với headline kết luận cho từng slide, luận điểm chính, hình/metric cần dùng, nguồn và speaker notes ngắn.

**Nghiệm thu:** mọi yêu cầu README ánh xạ được đến slide; câu chuyện không có khoảng nhảy logic; không đưa số chưa nghiệm thu vào storyboard.

**Prompt Agent:**
```text
Thực hiện GIAI ĐOẠN 9 theo ChienLuoc.md. Chỉ tạo storyboard, chưa thiết kế/ xuất PDF cuối. Tối đa 15 slide tính cả title và references. Viết headline kiểu kết luận cho từng slide, luận điểm, số liệu/biểu đồ chính, nguồn chân trang, lời giải thích cho executive và cách chuyển tiếp sang slide kế. Đảm bảo mọi requirement của README được ánh xạ vào storyboard, đặc biệt phải có tên model + metric + score viết rõ. Chỉ dùng số liệu đã có trong EVIDENCE_LEDGER.md và assumptions đã duyệt trong business case; nếu thiếu dữ liệu hãy đánh dấu TODO thay vì bịa. Hãy kiểm tra giới hạn độ dài chữ và loại slide không đóng góp. Cập nhật checklist rubric. DỪNG sau storyboard.
```

### Giai đoạn 10 — Thiết kế, hoàn thiện slide và xuất PDF

**Mục tiêu:** Tạo slide có vẻ ngoài như proposal của consulting firm, dễ đọc trong vài giây và có trích dẫn đầy đủ.

**Nguyên tắc thiết kế:**
- Mỗi slide có một thông điệp chính; title phải truyền đạt kết luận, không chỉ ghi tên chủ đề.
- Sử dụng nền sáng hoặc palette nhất quán, tối đa 1–2 font, phân cấp chữ rõ, khoảng trắng tốt và màu sắc có nghĩa.
- Dùng chart gốc từ dữ liệu, có đơn vị/legend/ghi chú; làm nổi bật insight thay vì nhồi nhiều hình.
- Cỡ chữ phải dễ đọc khi trình chiếu; không dùng ảnh chụp notebook thay cho kết quả; tránh chart 3D và trục gây hiểu nhầm.
- Citation ngắn ngay trên từng slide có claim/dữ kiện ngoài; đầy đủ danh mục ở slide cuối và Omnicampus.
- Giữ claims, metric, bảng ROI nhất quán với notebook và Evidence Ledger.
- Xuất PDF rồi render/kiểm tra toàn bộ các trang để phát hiện chữ tràn, cắt, sai ký tự, citation nhỏ hoặc hình mờ.

**Deliverables:** source slide (nếu công cụ hỗ trợ), `slides/[OmnicampusAccountName].pdf`, ảnh render kiểm tra và bảng rubric coverage.

**Nghiệm thu:** tổng slide ≤15; PDF ≤10 MB; có references; chart rõ; không tràn/cắt; mọi con số match notebook; PDF mở được.

**Prompt Agent:**
```text
Thực hiện GIAI ĐOẠN 10 theo ChienLuoc.md dựa trên storyboard đã nghiệm thu. Tạo slide deck executive-ready, tối đa 15 trang tính title/references, phong cách tư vấn chuyên nghiệp và nhất quán. Không chèn số liệu mới nếu chưa có nguồn. Đảm bảo title là thông điệp, biểu đồ đọc được, citation đặt sát claim và References cuối deck khớp SOURCE_LOG.md. Slide kết quả mô hình phải ghi đầy đủ tên model, metric và score bằng text; slide impact phải hiển thị rõ giả định. Export PDF, kiểm tra số trang/kích thước file, render tất cả trang để xem lỗi tràn/cắt/chữ nhỏ/chữ lỗi/hình mờ. Nếu phát hiện lỗi, sửa rồi render kiểm tra lại. Lưu source file nếu có. Không thay đổi kết luận phân tích chỉ để làm slide đẹp. DỪNG sau QA.
```

### Giai đoạn 11 — Notebook final, kiểm toán chéo và đóng gói submission

**Mục tiêu:** Đảm bảo người chấm có thể tái tạo phân tích và mọi claim trên slide có bằng chứng.

**Việc cần làm:**
- Restart kernel/runtime và run-all từ trên xuống dưới trong môi trường được hướng dẫn; loại bỏ state ẩn, cell lỗi, output cũ gây hiểu lầm và đường dẫn tuyệt đối không cần thiết.
- Kiểm tra data paths, package imports, random seeds, runtime, version notes và hướng dẫn tái lập.
- Kiểm tra tất cả số liệu/caption/table trên slide với kết quả notebook; tạo traceability matrix `slide → claim → notebook cell/table/figure hoặc nguồn/assumption`.
- Xác minh citations: tất cả nguồn slide nằm trong References; không có nguồn ngoài nào thiếu citation. Nếu có dùng generative AI, hoàn thiện `reports/AI_USAGE_LOG.md`, tạo/xác minh URL lịch sử chat thật theo Mục 1.6 và thêm URL vào trường References trên Omnicampus. Không đánh dấu PASS khi link còn placeholder, lỗi hoặc chưa được người dùng xác nhận.
- Đổi tên file chính xác theo Omnicampus account name, không bỏ sót file khi resubmission.
- Thực hiện checklist submission sớm trước deadline.

**Deliverables:** notebook/zip final; PDF final; `reports/traceability_matrix.md`; danh sách References để copy lên Omnicampus; checklist cuối.

**Nghiệm thu:** notebook run-all thành công trong môi trường ghi rõ; ≤15 slide và ≤10 MB; model name/metrics chính xác; link và nguồn thật; tất cả tên file đúng; không có số mâu thuẫn.

**Prompt Agent:**
```text
Thực hiện GIAI ĐOẠN 11 theo ChienLuoc.md. Đây là final QA, không tự tái viết toàn bộ analysis hoặc thay kết quả để trông đẹp hơn. Restart runtime và chạy notebook từ đầu đến cuối; sửa lỗi import/path/state ẩn/seed/output stale. Xây traceability matrix cho từng claim và con số quan trọng trên slide: trỏ tới cell/bảng/hình notebook, URL nguồn hoặc dòng giả định. So sánh slide với kết quả đã chạy và tìm mọi mâu thuẫn. Kiểm tra tối đa 15 slides, PDF <=10 MB, model name + metric + score, citations trên slide, References list trên Omnicampus, `reports/AI_USAGE_LOG.md` và AI-chat URL thật theo Mục 1.6. Nếu tôi chưa cung cấp URL hoặc chưa xác nhận link đã mở được, hãy đánh dấu BLOCKED và đưa checklist thao tác để tôi tự tạo/cung cấp; tuyệt đối không bịa link hoặc tuyên bố đã chia sẻ thay tôi. Tạo final checklist cùng các điểm còn chưa thể xác minh. Không nói rằng notebook đã tái lập nếu chưa thật sự run-all. Sau báo cáo cuối thì DỪNG.
```

---

## 4. Master prompt dùng để khởi tạo AI Agent

Sao chép prompt này vào Agent trước khi chạy prompt của Giai đoạn 0:

```text
Bạn là senior data scientist, telecom business consultant và presentation reviewer. Nhiệm vụ là hỗ trợ tôi hoàn thành GCI World 2026 Final Assignment dựa trên README, Dataset Overview, tutorial.ipynb, Client.csv và Record.csv được cung cấp.

MỤC TIÊU CUỐI:
1) PDF proposal tối đa 15 slides, dưới 10 MB.
2) Notebook/Script có thể tái lập.
3) Danh sách References trùng với citations trên slides; nếu dùng generative AI, có `reports/AI_USAGE_LOG.md` và URL lịch sử chat thật được nhập vào trường References trên Omnicampus theo Mục 1.6 của ChienLuoc.md.
4) Một đề xuất kinh doanh có owner/action/target group/KPI, căn cứ từ EDA + model + market research và tác động định lượng kèm giả định minh bạch.

QUY TẮC BẮT BUỘC:
- Đọc ChienLuoc.md và tất cả tài liệu assignment trước khi làm. Giữ nguyên thuật ngữ và tiêu chí của nguồn.
- Làm đúng MỘT giai đoạn mỗi lượt. Nếu tôi chưa yêu cầu giai đoạn tiếp theo, dừng sau deliverables và nghiệm thu của giai đoạn đang làm.
- Đừng chỉ giải thích hoặc đưa pseudocode: khi được yêu cầu thực thi một giai đoạn, hãy tạo/sửa file và chạy code thực tế trong workspace khi công cụ cho phép.
- Không bịa số liệu, metrics, citations, URL, model result, cost, market fact hoặc ROI. Nếu chưa chạy được, ghi rõ chưa chạy được và vì sao.
- Phân biệt FACT (quan sát từ dataset/nguồn), INFERENCE (diễn giải), ASSUMPTION (giả định), và TODO/UNVERIFIED.
- Dataset Overview chỉ xác nhận Company A là nhà cung cấp viễn thông ẩn danh; không tự gán quốc gia/thị trường nếu nguồn không chứng minh.
- Dùng Customer_ID chỉ cho join/QA, không dùng làm predictor. Rà soát leakage, thời điểm dữ liệu, missingness, split và data preprocessing cẩn thận.
- Không fit imputation/encoding/scaling trên test; không dùng test để tuning/threshold selection; không đưa target hoặc hậu quả sau thời điểm dự đoán vào X.
- `churn` là hướng mặc định để kiểm định, không phải kết luận phải giữ bằng mọi giá. Nếu đổi bài toán, hãy trình bày bằng chứng EDA và lý do.
- Model performance không đồng nghĩa causal effect hoặc ROI. Economic case phải dùng công thức minh bạch, assumption labels, sensitivity và pilot/holdout để xác minh incremental uplift.
- Ưu tiên originality và synthesis; không copy nguyên đoạn từ nguồn/AI. Citation tất cả thông tin, phương pháp và hình bên ngoài.
- Slides hướng tới executive không có nền tảng ML; vẫn phải ghi rõ tên model, metric và score; nhiều biểu đồ có mục tiêu; tối đa 15 slides tính cả title/references.
- Mỗi lần kết thúc giai đoạn phải cập nhật DECISIONS.md, EVIDENCE_LEDGER.md, SOURCE_LOG.md và AI_USAGE_LOG.md khi có thay đổi phù hợp; liệt kê file tạo/sửa, kiểm tra đã chạy, kết quả, rủi ro và câu hỏi còn mở. Với link chat AI, chỉ ghi URL do người dùng cung cấp/tạo và không được tự bịa URL.
- Không sửa dữ liệu nguồn hoặc xóa file cũ nếu chưa có lý do rõ ràng; ưu tiên thao tác có thể đảo ngược.

QUY TRÌNH PHẢN HỒI CUỐI MỖI GIAI ĐOẠN:
A. Mục tiêu đã hoàn thành.
B. File tạo/sửa và đường dẫn.
C. Code/QA đã chạy và kết quả thực tế.
D. Các quyết định có bằng chứng và link đến dòng/biểu đồ/bảng tương ứng.
E. Giả định, hạn chế, rủi ro và mục chưa xác minh.
F. Checklist nghiệm thu: PASS / FAIL / BLOCKED.
G. Dừng; không làm giai đoạn kế tiếp cho đến khi tôi yêu cầu.

Bắt đầu bằng việc xác nhận đã đọc ChienLuoc.md và report ngắn cấu trúc workspace, nhưng chưa bắt tay làm các giai đoạn sau. Chờ tôi chỉ định prompt giai đoạn cần chạy.
```

---

## 5. Các file quản trị bằng chứng nên duy trì xuyên suốt

### `reports/DECISIONS.md`
Mỗi quyết định ghi: ngày, quyết định, lựa chọn thay thế, bằng chứng, lý do, hệ quả và trạng thái (proposed/accepted/rejected).

### `reports/EVIDENCE_LEDGER.md`
Bảng nên có các cột: `Claim/Insight`, `Evidence type (DATA/SOURCE/ASSUMPTION)`, `Value`, `How calculated`, `Notebook cell/table/figure`, `Source URL`, `Limitations`, `Slide planned`, `Status`.

### `reports/SOURCE_LOG.md`
Mỗi nguồn: `Organization/Author`, `Title`, `URL`, `Publication date`, `Access date`, `Exact fact used`, `Slide`, `Citation text`, `Reliability/limitations`.

### `reports/AI_USAGE_LOG.md`
Lưu nhật ký minh bạch cho từng cuộc hội thoại AI có đóng góp đáng kể: nền tảng, ngày truy cập, mục đích, URL chia sẻ thật, phần đóng góp được sử dụng, deliverable chịu ảnh hưởng và cách người dùng kiểm chứng. Tạo file từ mẫu tại Mục 1.6. AI Agent có thể chuẩn bị các dòng nhật ký và nhắc người dùng hoàn tất, nhưng không được tự tạo link chia sẻ hoặc đánh dấu PASS khi người dùng chưa cung cấp/xác minh URL.

### `reports/traceability_matrix.md`
Sau khi có slide, ánh xạ từng claim quan trọng trên slide tới notebook cell/table/figure, URL nguồn hoặc assumption. Claim nào không có bằng chứng phải được sửa/xóa.

---

## 6. Quality gates — không được chuyển tiếp nếu chưa đạt

### Data gate
- [ ] Join và khóa đã được xác nhận.
- [ ] Target hợp lệ, phân phối đã báo cáo.
- [ ] Missingness, dtype, outliers và cột bất thường đã được audit.
- [ ] File gốc không bị chỉnh sửa.

### EDA/problem gate
- [ ] Có nhiều insight định lượng; không dừng ở mô tả shape/missingness.
- [ ] Business question có ý nghĩa và dẫn đến quyết định hành động.
- [ ] Target/horizon đúng; feature timing và leakage được xem xét.
- [ ] Không kết luận nhân quả từ correlation.

### Model gate
- [ ] Có baseline và benchmark hợp lý.
- [ ] Split/seed/preprocessing tái lập, không leakage.
- [ ] Có tên model, metric và score; đánh giá không chỉ bằng accuracy.
- [ ] Threshold/metric phục vụ trade-off thật.
- [ ] Kết quả trên test không được dùng để tune.

### Business case gate
- [ ] Đề xuất mô tả rõ ai làm gì, với ai, bằng cách nào.
- [ ] Tác động định lượng có công thức, units, assumptions và sensitivity.
- [ ] Có pilot/holdout để đo incremental uplift.
- [ ] Rủi ro, giới hạn và điều kiện go/no-go được ghi.

### Presentation/submission gate
- [ ] Tối đa 15 slides, có title và references.
- [ ] Tất cả claims/data ngoài có citations trên slide.
- [ ] Slide có model name + metric + score bằng chữ.
- [ ] Nhiều biểu đồ rõ, không gây hiểu lầm.
- [ ] Slide deck logic từ vấn đề tới impact, dễ hiểu với executive.
- [ ] Notebook run-all đã kiểm chứng.
- [ ] PDF ≤10 MB; tên file theo Omnicampus account name.
- [ ] Nếu có dùng generative AI: `reports/AI_USAGE_LOG.md` đã hoàn thiện; URL lịch sử chat thật đã được kiểm tra và nhập vào References trên Omnicampus; chưa để placeholder.
- [ ] Người dùng đã rà soát nội dung chia sẻ để tránh công khai thông tin nhạy cảm; link được mở kiểm tra thành công.

---

## 7. Quy tắc ra quyết định khi thời gian hoặc compute hạn chế

1. Ưu tiên câu hỏi business + EDA đúng + model baseline/benchmark hợp lệ + impact logic, trước khi thử model phức tạp.
2. Không chạy grid search quá rộng nếu không đổi quyết định kinh doanh; bắt đầu với baseline, rồi mô hình diễn giải được và một mô hình phi tuyến mạnh.
3. Nếu SHAP hoặc package khác không hoạt động, chuyển sang permutation importance/feature importance phù hợp và ghi hạn chế; không để một công cụ optional chặn toàn bộ assignment.
4. Nếu một biến có missingness cao, đánh giá bằng phân tích và thử nghiệm ablation thay vì mặc định xóa hoặc giữ.
5. Nếu không đủ dữ liệu để xác định market/cost/margin/impact, công khai giới hạn và dùng sensitivity analysis; không bù lỗ hổng bằng những con số giả định nhưng không gắn nhãn.
6. Thiết kế đẹp không bù được bằng chứng yếu; score model cao cũng không tự động chứng minh đề xuất tạo lợi nhuận.
7. Lưu bản cuối sau mỗi giai đoạn nghiệm thu; giữ ít nhất một bản backup riêng trước các sửa đổi lớn.

---

## 8. Lệnh khởi động mỗi giai đoạn

Sau khi Agent nạp Master Prompt, gửi riêng prompt của giai đoạn tương ứng. Ví dụ:

```text
Bắt đầu GIAI ĐOẠN 0. Tuân thủ toàn bộ ChienLuoc.md và Master Prompt. Chỉ làm Giai đoạn 0, tạo deliverables thực tế, chạy kiểm tra nghiệm thu và dừng.
```

Tiếp tục lần lượt từ Giai đoạn 1 đến 11. Nếu một gate FAIL/BLOCKED, sửa gate đó trước, không xây các giai đoạn sau dựa trên kết quả chưa đáng tin cậy.

---

## 9. Tiêu chuẩn cuối cùng

Một bài làm mạnh không phải là bài có notebook dài nhất, thuật toán mới nhất hay đủ đúng 15 slide. Bài làm mạnh là bài mà người điều hành có thể trả lời rõ ràng 5 câu hỏi:

1. Vấn đề kinh doanh nào được dữ liệu chỉ ra?
2. Bằng chứng nào cho thấy vấn đề này đáng giải quyết?
3. Model hỗ trợ quyết định ra sao và đáng tin đến mức nào?
4. Đề xuất tạo giá trị thế nào, trong điều kiện giả định nào?
5. Pilot sẽ kiểm chứng thành công/thất bại bằng KPI nào trước khi mở rộng?

Nếu một slide, feature, model hoặc phân tích không giúp trả lời các câu hỏi trên hoặc đáp ứng trực tiếp rubric, hãy cân nhắc bỏ nó để dành chỗ cho bằng chứng và quyết định quan trọng hơn.
