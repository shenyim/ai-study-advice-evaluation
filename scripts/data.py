import pandas as pd

# 1. 读取原始数据
df = pd.read_csv("student_questions_raw.csv")

print("===== BEFORE CLEANING =====")
print(df)
print("\nShape:", df.shape)
print("\nMissing values:")
print(df.isna().sum())

# 2. 按 question_id 去重
df = df.drop_duplicates(subset=["question_id"], keep="first")

# 3. 清理文本字段：去空格
df["question_id"] = df["question_id"].str.strip()
df["question_text"] = df["question_text"].str.strip()
df["category"] = df["category"].str.strip().str.lower()
df["difficulty"] = df["difficulty"].str.strip().str.lower()
df["expected_risk"] = df["expected_risk"].str.strip().str.lower()

# 4. 清理 student_background
df["student_background"] = df["student_background"].fillna("unknown")
df["student_background"] = df["student_background"].str.strip().str.lower()

# 5. 修复拼写错误
df["difficulty"] = df["difficulty"].replace({
    "medum": "medium"
})

# 6. 检查 difficulty 合法值
valid_difficulty = ["easy", "medium", "hard"]
df.loc[~df["difficulty"].isin(valid_difficulty), "difficulty"] = "unknown"

# 7. 检查 expected_risk 合法值
valid_risk = ["low", "medium", "high"]
df.loc[~df["expected_risk"].isin(valid_risk), "expected_risk"] = "unknown"

# 8. 输出清洗后结果
print("\n===== AFTER CLEANING =====")
print(df)
print("\nShape:", df.shape)

print("\nMissing values:")
print(df.isna().sum())

print("\nCategory counts:")
print(df["category"].value_counts())

print("\nDifficulty counts:")
print(df["difficulty"].value_counts())

print("\nRisk counts:")
print(df["expected_risk"].value_counts())

# 9. 保存清洗后的数据
df.to_csv("student_questions_clean.csv", index=False)

print("\nCleaned file saved as student_questions_clean.csv")
