# ENVIRONMENT & REPRODUCIBILITY GUIDE — GCI WORLD 2026 FINAL ASSIGNMENT

Tài liệu này xác nhận môi trường tính toán thực tế, cấu hình tái lập (reproducibility) và hướng dẫn thực thi các giai đoạn phân tích.

---

## 1. Môi trường tính toán đã xác nhận

- **Hệ điều hành:** Windows (PowerShell Shell)
- **Phiên bản Python:** `Python 3.13.11`
- **Các gói thư viện chính đã cài đặt và phiên bản ghi nhận:**
  - `pandas`: `2.3.3`
  - `numpy`: `2.4.1`
  - `scikit-learn`: `1.8.0`
  - `scipy`: `1.17.0`
  - `matplotlib`: `3.10.8`
  - `seaborn`: `0.13.2`
  - `openpyxl`: `3.1.5`
  - `pyarrow`: `23.0.1`

---

## 2. Quy chuẩn tái lập (Reproducibility Standards)

1. **Random Seed:**
   - Cố định `SEED = 42` trên mọi phân chia tập dữ liệu (`train_test_split`, `StratifiedKFold`) và khởi tạo thuật toán có yếu tố ngẫu nhiên (`LogisticRegression`, `RandomForestClassifier`, `HistGradientBoostingClassifier`, v.v.).
2. **Quy ước đường dẫn (Path Handling):**
   - Không sử dụng đường dẫn tuyệt đối dạng `D:\Project\...` hay `C:\Users\...` trong code.
   - Luôn sử dụng thư viện `pathlib.Path` để trỏ tương đối từ thư mục gốc dự án:
     ```python
     from pathlib import Path
     BASE_DIR = Path(__file__).resolve().parent.parent if "__file__" in locals() else Path.cwd()
     DATA_DIR = BASE_DIR / "data" / "raw"
     # Dự phòng nếu chạy thẳng trong môi trường chỉ có folder telecom
     if not DATA_DIR.exists():
         DATA_DIR = BASE_DIR / "telecom"
     ```
3. **Phân tách dữ liệu:**
   - Dữ liệu gốc trong `telecom/` và `data/raw/` được bảo vệ ở chế độ Read-Only (không bao giờ ghi đè).
   - Mọi kết quả tiền xử lý sẽ được lưu riêng vào `data/processed/`.

---

## 3. Cấu trúc thư mục chuẩn của dự án

```text
Final_Assignment/
├── ChienLuoc.md                 # Kế hoạch chiến lược 11 giai đoạn và master prompt
├── README.md                    # Tổng quan dự án và hướng dẫn chạy nhanh
├── telecom/                     # Thư mục gốc chứa file thô do BTC cung cấp (Read-only)
│   ├── Client.csv               # 17.937.775 bytes (SHA256: 264A5851...)
│   └── Record.csv               # 30.182.432 bytes (SHA256: 5BD563BB...)
├── data/
│   ├── raw/                     # Bản sao dữ liệu gốc được kiểm tra hash nguyên vẹn
│   │   ├── Client.csv
│   │   └── Record.csv
│   └── processed/               # Dữ liệu sạch sau kiểm toán & pipeline (tạo ở các giai đoạn sau)
├── notebooks/                   # Jupyter Notebook phân tích từng giai đoạn
├── src/                         # Mã nguồn module tái sử dụng (data loaders, metrics, pipeline)
├── reports/                     # Hệ thống quản trị chứng cứ và tài liệu phân tích
│   ├── DECISIONS.md             # Nhật ký quyết định kiến trúc & phương pháp
│   ├── EVIDENCE_LEDGER.md       # Sổ cái theo dõi bằng chứng (số liệu, công thức, nguồn)
│   ├── SOURCE_LOG.md            # Danh mục tài liệu tham khảo & trích dẫn
│   ├── AI_USAGE_LOG.md          # Nhật ký khai báo sử dụng Generative AI & URL chia sẻ
│   ├── ENVIRONMENT.md           # Báo cáo môi trường và hướng dẫn tái lập (file này)
│   └── figures/                 # Biểu đồ và hình ảnh chất lượng cao phục vụ slide
└── slides/                      # Tài liệu storyboard, slide deck và file PDF nộp bài
```

---

## 4. Hướng dẫn chạy và kiểm tra nhanh

Để kiểm tra môi trường và đường dẫn từ terminal:
```powershell
python -c "import pandas, sklearn, numpy, matplotlib, seaborn; print('All core libraries imported successfully!')"
```
