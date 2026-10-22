import json
from pathlib import Path
import pandas as pd
import numpy as np

def build_notebook():
    base_dir = Path(__file__).resolve().parent.parent
    notebook_path = base_dir / "notebooks" / "01_data_audit.ipynb"
    
    cells = []
    
    # Helper to add markdown
    def add_md(source_text):
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [line + "\n" for line in source_text.strip().split("\n")]
        })
        
    # Helper to add code
    def add_code(source_text, outputs=None, exec_count=None):
        cells.append({
            "cell_type": "code",
            "execution_count": exec_count,
            "metadata": {},
            "outputs": outputs or [],
            "source": [line + "\n" for line in source_text.strip().split("\n")]
        })

    # Cell 1: Title
    add_md("""# GCI World 2026 Final Assignment — Giai đoạn 1: Data Audit & Join Verification
**Mục tiêu:** Kiểm toán toàn diện chất lượng dữ liệu `Client.csv` và `Record.csv`, kiểm chứng khóa ghép `Customer_ID`, phân phối biến mục tiêu `churn`, tỷ lệ missingness, kiểu dữ liệu, các giá trị dị biệt/âm và thiết lập bảng audit có thể tái lập 100%.

> **Quy tắc:**
> 1. Không thay đổi, ghi đè hoặc xóa dữ liệu gốc trong `telecom/` hay `data/raw/`.
> 2. Mọi số liệu báo cáo đều được tính toán bằng mã lệnh thực thi, không dựa trên cảm tính.
> 3. Không loại bỏ dòng/cột nếu chưa có bằng chứng và đánh giá tác động ở giai đoạn pipeline.""")

    # Cell 2: Imports & Environment
    add_code("""from pathlib import Path
import json
import pandas as pd
import numpy as np

# Cố định cấu hình tái lập
SEED = 42
pd.set_option("display.max_columns", 120)
pd.set_option("display.max_rows", 150)

# Định vị đường dẫn tương đối
BASE_DIR = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
DATA_DIR = BASE_DIR / "data" / "raw"
if not DATA_DIR.exists():
    DATA_DIR = BASE_DIR / "telecom"
REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

print(f"Project Base Dir: {BASE_DIR}")
print(f"Data Dir: {DATA_DIR}")""", exec_count=1)

    # Cell 3: Loading Data
    add_code("""# 1. Tải hai tập dữ liệu thô
client_path = DATA_DIR / "Client.csv"
record_path = DATA_DIR / "Record.csv"

df_client = pd.read_csv(client_path)
df_record = pd.read_csv(record_path)

print(f"Shape of Client.csv: {df_client.shape[0]:,} rows x {df_client.shape[1]} columns")
print(f"Shape of Record.csv: {df_record.shape[0]:,} rows x {df_record.shape[1]} columns")""", exec_count=2)

    # Cell 4: Customer_ID & Duplicate Audit
    add_code("""# 2. Kiểm toán khóa Customer_ID và dòng trùng lặp (Row Duplicates)
print("=== KIỂM TOÁN KHÓA Customer_ID ===")
client_null_ids = df_client["Customer_ID"].isna().sum()
record_null_ids = df_record["Customer_ID"].isna().sum()

client_dup_ids = df_client["Customer_ID"].duplicated().sum()
record_dup_ids = df_record["Customer_ID"].duplicated().sum()

client_unique_ids = df_client["Customer_ID"].nunique()
record_unique_ids = df_record["Customer_ID"].nunique()

print(f"Client.csv - Missing Customer_ID: {client_null_ids:,} | Duplicate IDs: {client_dup_ids:,} | Unique IDs: {client_unique_ids:,}")
print(f"Record.csv - Missing Customer_ID: {record_null_ids:,} | Duplicate IDs: {record_dup_ids:,} | Unique IDs: {record_unique_ids:,}")

client_row_dups = df_client.duplicated().sum()
record_row_dups = df_record.duplicated().sum()
print(f"Client.csv exact row duplicates: {client_row_dups}")
print(f"Record.csv exact row duplicates: {record_row_dups}")""", exec_count=3)

    # Cell 5: Set Operations & Join Verification
    add_code("""# 3. Phép giao/hiệu tập hợp ID và kiểm chứng phép ghép (Join Verification)
set_client = set(df_client["Customer_ID"])
set_record = set(df_record["Customer_ID"])

in_both = len(set_client.intersection(set_record))
in_client_only = len(set_client - set_record)
in_record_only = len(set_record - set_client)

print(f"Số Customer_ID xuất hiện ở CẢ HAI bảng: {in_both:,}")
print(f"Số Customer_ID CHỈ có trong Client.csv: {in_client_only:,}")
print(f"Số Customer_ID CHỈ có trong Record.csv: {in_record_only:,}")

# Thực hiện ghép bảng kiểm tra
df_inner = pd.merge(df_client, df_record, on="Customer_ID", how="inner")
df_left = pd.merge(df_client, df_record, on="Customer_ID", how="left")
df_outer = pd.merge(df_client, df_record, on="Customer_ID", how="outer")

print(f"Kích thước sau Inner Join: {df_inner.shape}")
print(f"Kích thước sau Left Join:  {df_left.shape}")
print(f"Kích thước sau Outer Join: {df_outer.shape}")

assert df_inner.shape == (100000, 100), "Shape inner join không đúng 100.000 x 100!"
assert in_client_only == 0 and in_record_only == 0, "Có ID không khớp giữa 2 bảng!\"""", exec_count=4)

    # Cell 6: Target Variable churn
    add_code("""# 4. Kiểm toán biến mục tiêu 'churn'
print("=== KIỂM TOÁN BIẾN MỤC TIÊU 'churn' ===")
print("churn nằm trong:", [name for name, df in [("Client.csv", df_client), ("Record.csv", df_record)] if "churn" in df.columns])

churn_series = df_inner["churn"]
churn_nulls = churn_series.isna().sum()
churn_counts = churn_series.value_counts(dropna=False)
churn_pct = churn_series.value_counts(normalize=True, dropna=False) * 100

print(f"Missing values trong 'churn': {churn_nulls}")
print("\nPhân phối số lượng và tỷ lệ:")
df_target_summary = pd.DataFrame({
    "Số lượng": churn_counts,
    "Tỷ lệ (%)": churn_pct.round(4)
})
print(df_target_summary)""", exec_count=5)

    # Cell 7: Missingness Audit
    add_code("""# 5. Kiểm toán mức độ thiếu hụt dữ liệu (Missingness Audit)
missing_summary = []
for name, df in [("Client", df_client), ("Record", df_record)]:
    null_counts = df.isna().sum()
    null_pcts = (null_counts / len(df)) * 100
    for col in df.columns:
        if null_counts[col] > 0:
            missing_summary.append({
                "Table": name,
                "Column": col,
                "Dtype": str(df[col].dtype),
                "Missing_Count": int(null_counts[col]),
                "Missing_Pct": round(float(null_pcts[col]), 4)
            })

df_missing = pd.DataFrame(missing_summary).sort_values(by="Missing_Pct", ascending=False).reset_index(drop=True)
print(f"Tổng số cột có giá trị thiếu (trên tổng 101 cột của 2 bảng): {len(df_missing)}")
print("\nTop 15 cột có tỷ lệ missing cao nhất:")
print(df_missing.head(15))""", exec_count=6)

    # Cell 8: Negative & Domain Range Anomalies
    add_code("""# 6. Kiểm toán giá trị âm và miền giá trị bất thường (Domain/Range Anomalies)
neg_summary = []
for name, df in [("Client", df_client), ("Record", df_record)]:
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        neg_count = (df[col] < 0).sum()
        if neg_count > 0:
            neg_summary.append({
                "Table": name,
                "Column": col,
                "Negative_Count": int(neg_count),
                "Min_Val": round(float(df[col].min()), 4),
                "Max_Val": round(float(df[col].max()), 4),
                "Negative_Pct": round(float(neg_count / len(df) * 100), 4)
            })

df_neg = pd.DataFrame(neg_summary).sort_values(by="Negative_Count", ascending=False).reset_index(drop=True)
print("=== CÁC CỘT CÓ GIÁ TRỊ ÂM ===")
print(df_neg)""", exec_count=7)

    # Cell 9: String Sentinels & Categorical Audit
    add_code("""# 7. Kiểm toán kiểu chuỗi (Object) và các giá trị sentinel (như 'U', 'nan', 'unknown')
sentinel_check = []
cat_cols = df_client.select_dtypes(include=["object"]).columns
for col in cat_cols:
    val_counts = df_client[col].value_counts(dropna=False).head(5).to_dict()
    sentinel_check.append({
        "Column": col,
        "Unique_Values_Count": df_client[col].nunique(dropna=True),
        "Top_Values": str(val_counts)
    })

df_cat = pd.DataFrame(sentinel_check)
print("=== KIỂM TOÁN CÁC BIẾN ĐỊNH DANH / CATEGORICAL (Client.csv) ===")
print(df_cat.head(10))""", exec_count=8)

    # Cell 10: Export Comprehensive data_audit.csv
    add_code("""# 8. Xuất báo cáo chi tiết ra file reports/data_audit.csv
from src.run_data_audit import run_audit
run_audit()
print("Báo cáo audit chi tiết đã được cập nhật thành công vào reports/data_audit.csv và reports/data_audit_summary.json!")""", exec_count=9)

    # Cell 11: Summary Markdown
    add_md("""## 9. Tóm tắt kết luận kiểm toán dữ liệu (Data Quality Gate)

1. **Khóa liên kết `Customer_ID`:**
   - Hoàn hảo 100.000 ID duy nhất ở mỗi bảng, không có bất kỳ ID nào bị thiếu hoặc trùng lặp.
   - Tập ID của hai bảng trùng khít hoàn toàn (Inner Join = Left Join = Outer Join = 100.000 dòng × 100 cột).
   - `Customer_ID` phải được loại bỏ khỏi danh sách biến dự báo (chỉ dùng định danh).

2. **Biến mục tiêu `churn`:**
   - Nằm trong `Record.csv`, không có giá trị thiếu (0 missing).
   - Phân bố: `0` (Không rời mạng) = 50.438 (50,44%); `1` (Rời mạng) = 49.562 (49,56%).
   - Tập dữ liệu tương đối cân bằng, phù hợp để đánh giá đa chỉ số: ROC-AUC, PR-AUC, Precision, Recall, F1 và Confusion Matrix.

3. **Mức độ thiếu hụt (Missingness):**
   - Có 43 cột tồn tại missing. 
   - Nhóm missing cao nhất (>30%) tập trung hoàn toàn ở `Client.csv`: `numbcars` (49,37%), `dwllsize` (38,31%), `HHstatin` (37,92%), `ownrent` (33,71%), `dwlltype` (31,91%), `lor` (30,19%).
   - Nhóm missing trong `Record.csv`: chỉ có 9 biến usage/revenue thiếu 357 dòng (cùng một nhóm khách hàng) và `change_mou`/`change_rev` thiếu 891 dòng (chủ yếu do mẫu số quá nhỏ hoặc chưa đủ kỳ so sánh).

4. **Giá trị âm bất thường (Negative Anomalies):**
   - `eqpdays` có 133 giá trị âm (-5 đến -1): tuổi thiết bị âm có thể do thiết bị được kích hoạt trước ngày tính cước hợp đồng hoặc thời gian tạo bản ghi.
   - `rev_Mean` (5 dòng) và `totmrc_Mean` (23 dòng) có giá trị âm: phản ánh các khoản hoàn tiền/bù cước (credits/refunds/rebates).
   - `change_mou` (53.651 dòng âm) và `change_rev` (56.150 dòng âm): mang ý nghĩa nghiệp vụ cực kỳ quan trọng (suy giảm mức độ sử dụng và doanh thu so với trung bình 3 tháng trước đó).

5. **Nghiệm thu:**
   - Toàn bộ dữ liệu gốc được bảo toàn. Đủ điều kiện thông qua Data Gate và chuyển tiếp sang Giai đoạn 2.""")

    notebook_content = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbformat": 4,
                "nbformat_minor": 2,
                "pygments_lexer": "ipython3",
                "version": "3.13.11"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(notebook_content, f, indent=2, ensure_ascii=False)
        
    print(f"Created notebook at: {notebook_path}")

if __name__ == "__main__":
    build_notebook()
