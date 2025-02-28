import pandas as pd

# Đọc dữ liệu thô
print("Đang làm sạch dữ liệu...")
data = pd.read_csv("marketing_campaign_raw_data.csv")

# Kiểm tra danh sách cột để đảm bảo đúng
print("Danh sách các cột trong dataset:")
print(data.columns.tolist())

# Làm sạch và chuẩn hóa dữ liệu
# Xóa giá trị null ở các cột quan trọng
data = data.dropna(subset=["age", "job", "marital", "y", "poutcome", "campaign", "duration"])  # Sử dụng "y" thay vì "response"

# Chuẩn hóa cột "job", "marital", "poutcome", "education" thành chữ thường
data["job"] = data["job"].str.lower()
data["marital"] = data["marital"].str.lower()
data["poutcome"] = data["poutcome"].str.lower()
if "education" in data.columns:
    data["education"] = data["education"].str.lower()

# Không có cột "income" trong dataset, nên bỏ qua bước điền giá trị trung bình cho thu nhập

# Chuẩn hóa cột "y" (response) thành 1/0 (1: chấp nhận, 0: từ chối)
data["response"] = data["y"].map({"yes": 1, "no": 0})

# Thêm cột "age_group" (nhóm tuổi)
def categorize_age(age):
    if age < 30:
        return "Young"
    elif 30 <= age < 50:
        return "Middle-aged"
    else:
        return "Senior"
data["age_group"] = data["age"].apply(categorize_age)

# Thêm cột "engagement_score" (điểm tương tác) dựa trên số lần liên hệ và thời lượng cuộc gọi
data["engagement_score"] = data["campaign"] * 0.3 + (data["duration"] / 60) * 0.7  # Giả định trọng số

# Chuẩn hóa cột "poutcome" để phân tích cảm xúc/hành vi
data["poutcome"] = data["poutcome"].map({"success": "positive", "failure": "negative", "other": "neutral", "nonexistent": "neutral"})

# Lưu file sạch
data.to_csv("marketing_campaign_cleaned_data.csv", index=False)
print("Đã làm sạch và lưu vào marketing_campaign_cleaned_data.csv")
print(data.head())