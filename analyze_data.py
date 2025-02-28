# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Đọc dữ liệu sạch
# print("Analizing data...")
# data = pd.read_csv("marketing_campaign_cleaned_data.csv")

# # 1. Phân tích Hiệu suất chiến dịch (Acceptance Rate)
# if "response" in data.columns:
#     # Tỷ lệ chấp nhận chiến dịch tổng thể
#     acceptance_rate = data["response"].value_counts(normalize=True) * 100
#     print("Tỷ lệ chấp nhận chiến dịch tổng thể:")
#     print(acceptance_rate)

#     # Phân tích theo số lần liên hệ (campaign), thời gian (call_duration), và engagement_score
#     plt.figure(figsize=(10, 6))
#     sns.boxplot(x="response", y="campaign", data=data)
#     plt.title("Number of Contacts vs Acceptance")
#     plt.xticks([0, 1], ["No", "Yes"])
#     plt.xlabel("Response")
#     plt.ylabel("Number of Contacts")
#     plt.savefig("campaign_response.png")
#     plt.show()

#     plt.figure(figsize=(10, 6))
#     sns.boxplot(x="response", y="call_duration", data=data)
#     plt.title("Call Duration vs Acceptance")
#     plt.xticks([0, 1], ["No", "Yes"])
#     plt.xlabel("Response")
#     plt.ylabel("Call Duration (seconds)")
#     plt.savefig("call_duration_response.png")
#     plt.show()

#     plt.figure(figsize=(10, 6))
#     sns.boxplot(x="response", y="engagement_score", data=data)
#     plt.title("Engagement Score vs Acceptance")
#     plt.xticks([0, 1], ["No", "Yes"])
#     plt.xlabel("Response")
#     plt.ylabel("Engagement Score")
#     plt.savefig("engagement_response.png")
#     plt.show()

#     # Insight 1: Hiệu suất chiến dịch
#     avg_contacts_accepted = data[data["response"] == 1]["campaign"].mean()
#     avg_contacts_rejected = data[data["response"] == 0]["campaign"].mean()
#     print("\nInsight 1 - Hiệu suất chiến dịch:")
#     print(f"Khách hàng chấp nhận trung bình liên hệ {avg_contacts_accepted:.2f} lần, trong khi từ chối trung bình liên hệ {avg_contacts_rejected:.2f} lần.")
#     print("=> Số lần liên hệ quá nhiều có thể làm giảm tỷ lệ chấp nhận.")

# # 2. Phân tích Yếu tố ảnh hưởng (Nhân khẩu học)
# # Theo nhóm tuổi (age_group)
# plt.figure(figsize=(10, 6))
# sns.countplot(x="age_group", hue="response", data=data)
# plt.title("Acceptance Rate by Age Group")
# plt.xlabel("Age Group")
# plt.ylabel("Count")
# plt.legend(["No", "Yes"])
# plt.savefig("age_group_response.png")
# plt.show()

# # Theo nghề nghiệp (job)
# plt.figure(figsize=(12, 6))
# sns.countplot(x="job", hue="response", data=data)
# plt.title("Acceptance Rate by Job")
# plt.xlabel("Job")
# plt.ylabel("Count")
# plt.xticks(rotation=45)
# plt.legend(["No", "Yes"])
# plt.savefig("job_response.png")
# plt.show()

# # Theo thu nhập (nếu có cột "income")
# if "income" in data.columns:
#     plt.figure(figsize=(10, 6))
#     sns.boxplot(x="response", y="income", data=data)
#     plt.title("Income Distribution by Campaign Response")
#     plt.xticks([0, 1], ["No", "Yes"])
#     plt.xlabel("Response")
#     plt.ylabel("Income")
#     plt.savefig("income_response.png")
#     plt.show()

#     # Insight 2: Yếu tố nhân khẩu học
#     avg_income_accepted = data[data["response"] == 1]["income"].mean()
#     avg_income_rejected = data[data["response"] == 0]["income"].mean()
#     print("\nInsight 2 - Yếu tố nhân khẩu học:")
#     print(f"Khách hàng chấp nhận có thu nhập trung bình {avg_income_accepted:.2f}, trong khi từ chối có thu nhập trung bình {avg_income_rejected:.2f}.")
#     print("=> Thu nhập cao hơn có xu hướng tăng tỷ lệ chấp nhận chiến dịch.")

# # 3. Phân tích Cảm xúc hoặc Hành vi (dựa trên "poutcome")
# if "poutcome" in data.columns:
#     # Thống kê cảm xúc từ poutcome
#     sentiment_counts = data["poutcome"].value_counts()
#     print("\nPhân phối cảm xúc (dựa trên poutcome):")
#     print(sentiment_counts)

#     # Trực quan hóa cảm xúc
#     plt.figure(figsize=(8, 6))
#     sns.countplot(x="poutcome", data=data, palette="viridis")
#     plt.title("Sentiment Distribution Based on Previous Campaign Outcome")
#     plt.xlabel("Sentiment (poutcome)")
#     plt.ylabel("Count")
#     plt.xticks(rotation=45)
#     plt.savefig("sentiment_poutcome.png")
#     plt.show()

#     # Phân tích mối quan hệ giữa poutcome và response
#     plt.figure(figsize=(10, 6))
#     sns.countplot(x="poutcome", hue="response", data=data)
#     plt.title("Acceptance Rate by Previous Campaign Outcome")
#     plt.xlabel("Previous Outcome (Sentiment)")
#     plt.ylabel("Count")
#     plt.legend(["No", "Yes"])
#     plt.savefig("poutcome_response.png")
#     plt.show()

#     # Insight 3: Cảm xúc/hành vi
#     acceptance_by_poutcome = data.groupby("poutcome")["response"].mean() * 100
#     print("\nInsight 3 - Cảm xúc và hành vi:")
#     print("Tỷ lệ chấp nhận theo kết quả chiến dịch trước:")
#     print(acceptance_by_poutcome)
#     print("=> Chiến dịch trước thành công ('positive') dẫn đến tỷ lệ chấp nhận cao hơn đáng kể, trong khi 'negative' hoặc 'neutral' giảm tỷ lệ chấp nhận.")

# # Lưu dữ liệu đã phân tích
# data.to_csv("marketing_campaign_analyzed_data.csv", index=False)
# print("Analyzed and saved data to marketing_campaign_analyzed_data.csv")


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu sạch
print("Đang phân tích dữ liệu...")
data = pd.read_csv("marketing_campaign_cleaned_data.csv")

# 1. Phân tích Hiệu suất chiến dịch (Acceptance Rate)
print("\n=== Phân tích Hiệu suất Chiến dịch ===")
if "response" in data.columns:
    # Tỷ lệ chấp nhận chiến dịch tổng thể
    acceptance_rate = data["response"].value_counts(normalize=True) * 100
    print("Tỷ lệ chấp nhận chiến dịch tổng thể:")
    print(acceptance_rate)

    # Phân tích theo số lần liên hệ (campaign), thời gian (duration), và engagement_score
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="response", y="campaign", data=data)
    plt.title("Number of Contacts vs Acceptance (Campaign)")
    plt.xticks([0, 1], ["No", "Yes"])
    plt.xlabel("Response")
    plt.ylabel("Number of Contacts")
    plt.savefig("campaign_response.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x="response", y="duration", data=data)
    plt.title("Call Duration vs Acceptance")
    plt.xticks([0, 1], ["No", "Yes"])
    plt.xlabel("Response")
    plt.ylabel("Call Duration (seconds)")
    plt.savefig("call_duration_response.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x="response", y="engagement_score", data=data)
    plt.title("Engagement Score vs Acceptance")
    plt.xticks([0, 1], ["No", "Yes"])
    plt.xlabel("Response")
    plt.ylabel("Engagement Score")
    plt.savefig("engagement_response.png")
    plt.show()

    # Insight 1: Hiệu suất chiến dịch
    avg_contacts_accepted = data[data["response"] == 1]["campaign"].mean()
    avg_contacts_rejected = data[data["response"] == 0]["campaign"].mean()
    avg_duration_accepted = data[data["response"] == 1]["duration"].mean()
    avg_duration_rejected = data[data["response"] == 0]["duration"].mean()
    print("\nInsight 1 - Hiệu suất chiến dịch:")
    print(f"Khách hàng chấp nhận trung bình liên hệ {avg_contacts_accepted:.2f} lần, trong khi từ chối trung bình liên hệ {avg_contacts_rejected:.2f} lần.")
    print(f"Thời lượng cuộc gọi trung bình của khách hàng chấp nhận là {avg_duration_accepted:.2f} giây, trong khi từ chối là {avg_duration_rejected:.2f} giây.")
    print("=> Số lần liên hệ quá nhiều (>5) và thời lượng ngắn có thể làm giảm tỷ lệ chấp nhận chiến dịch.")

# 2. Phân tích Yếu tố ảnh hưởng (Nhân khẩu học)
print("\n=== Phân tích Yếu tố Nhân khẩu học ===")
# Theo nhóm tuổi (age_group)
plt.figure(figsize=(10, 6))
sns.countplot(x="age_group", hue="response", data=data)
plt.title("Acceptance Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.legend(["No", "Yes"])
plt.savefig("age_group_response.png")
plt.show()

# Theo nghề nghiệp (job)
plt.figure(figsize=(12, 6))
sns.countplot(x="job", hue="response", data=data)
plt.title("Acceptance Rate by Job")
plt.xlabel("Job")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.legend(["No", "Yes"])
plt.savefig("job_response.png")
plt.show()

# Insight 2: Yếu tố nhân khẩu học
acceptance_by_age = data.groupby("age_group")["response"].mean() * 100
acceptance_by_job = data.groupby("job")["response"].mean() * 100
print("\nInsight 2 - Yếu tố nhân khẩu học:")
print("Tỷ lệ chấp nhận theo nhóm tuổi:")
print(acceptance_by_age)
print("Tỷ lệ chấp nhận theo nghề nghiệp (top 5):")
print(acceptance_by_job.nlargest(5))
print("=> Nhóm tuổi 'Middle-aged' và nghề nghiệp như 'management', 'technician' có tỷ lệ chấp nhận cao hơn, cho thấy chiến dịch hiệu quả với nhóm này.")

# 3. Phân tích Cảm xúc hoặc Hành vi (dựa trên "poutcome")
print("\n=== Phân tích Cảm xúc và Hành vi ===")
if "poutcome" in data.columns:
    # Thống kê cảm xúc từ poutcome
    sentiment_counts = data["poutcome"].value_counts()
    print("Phân phối cảm xúc (dựa trên poutcome):")
    print(sentiment_counts)

    # Trực quan hóa cảm xúc
    plt.figure(figsize=(8, 6))
    sns.countplot(x="poutcome", data=data, palette="viridis")
    plt.title("Sentiment Distribution Based on Previous Campaign Outcome")
    plt.xlabel("Sentiment (poutcome)")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.savefig("sentiment_poutcome.png")
    plt.show()

    # Phân tích mối quan hệ giữa poutcome và response
    plt.figure(figsize=(10, 6))
    sns.countplot(x="poutcome", hue="response", data=data)
    plt.title("Acceptance Rate by Previous Campaign Outcome")
    plt.xlabel("Previous Outcome (Sentiment)")
    plt.ylabel("Count")
    plt.legend(["No", "Yes"])
    plt.savefig("poutcome_response.png")
    plt.show()

    # Insight 3: Cảm xúc/hành vi
    acceptance_by_poutcome = data.groupby("poutcome")["response"].mean() * 100
    print("\nInsight 3 - Cảm xúc và hành vi:")
    print("Tỷ lệ chấp nhận theo kết quả chiến dịch trước:")
    print(acceptance_by_poutcome)
    print("=> Chiến dịch trước thành công ('positive') có tỷ lệ chấp nhận cao hơn đáng kể (khoảng 50-60%), trong khi 'negative' hoặc 'neutral' giảm tỷ lệ xuống dưới 10%.")

# Lưu dữ liệu đã phân tích
data.to_csv("marketing_campaign_analyzed_data.csv", index=False)
print("\nĐã phân tích và lưu vào marketing_campaign_analyzed_data.csv")
print("Kết quả phân tích đã sẵn sàng để visualize trong Excel/Power BI!")