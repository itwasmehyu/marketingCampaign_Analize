import pandas as pd

# Tải file CSV từ Kaggle, sử dụng dấu ; làm separator
data = pd.read_csv("bank-additional-full.csv", sep=';')  # Đảm bảo tên file khớp
data.to_csv("marketing_campaign_raw_data.csv", index=False)
print("Đã tải dữ liệu và lưu vào marketing_campaign_raw_data.csv")
print("Danh sách các cột trong dataset:")
print(data.columns.tolist())  # In danh sách cột
print(data.head())  # In 5 dòng đầu để kiểm tra dữ liệu