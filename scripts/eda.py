import pandas as pd
import matplotlib.pyplot as plt

# 1. 读取清洗后的数据
df = pd.read_csv("data/student_questions_clean.csv")

print("===== BASIC INFO =====")
print(df.head())
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())

print("\n===== MISSING VALUES =====")
print(df.isna().sum())

# 2. 看每个类别有多少问题
print("\n===== CATEGORY DISTRIBUTION =====")
category_counts = df["category"].value_counts()
print(category_counts)

# 3. 看难度分布
print("\n===== DIFFICULTY DISTRIBUTION =====")
difficulty_counts = df["difficulty"].value_counts()
print(difficulty_counts)

# 4. 看风险等级分布
print("\n===== RISK DISTRIBUTION =====")
risk_counts = df["expected_risk"].value_counts()
print(risk_counts)

# 5. 交叉分析：不同类别的问题风险如何？
print("\n===== CATEGORY x RISK =====")
category_risk = pd.crosstab(df["category"], df["expected_risk"])
print(category_risk)

# 6. 交叉分析：不同难度的问题风险如何？
print("\n===== DIFFICULTY x RISK =====")
difficulty_risk = pd.crosstab(df["difficulty"], df["expected_risk"])
print(difficulty_risk)

# 7. 增加一个简单字段：问题文本长度
df["question_length"] = df["question_text"].str.len()

print("\n===== QUESTION LENGTH =====")
print(df["question_length"].describe())

# 8. 按类别看问题平均长度
print("\n===== AVERAGE QUESTION LENGTH BY CATEGORY =====")
print(df.groupby("category")["question_length"].mean().sort_values(ascending=False))

# 9. 画图：类别分布
plt.figure()
category_counts.plot(kind="bar")
plt.title("Question Count by Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("figures/category_distribution.png")
plt.show()

# 10. 画图：风险分布
plt.figure()
risk_counts.plot(kind="bar")
plt.title("Question Count by Expected Risk")
plt.xlabel("Expected Risk")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("figures/risk_distribution.png")
plt.show()

# 11. 保存带 question_length 的分析数据
df.to_csv("data/student_questions_eda.csv", index=False)

print("\nEDA file saved as student_questions_eda.csv")
print("Charts saved as category_distribution.png and risk_distribution.png")