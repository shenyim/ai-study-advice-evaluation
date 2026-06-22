import pandas as pd
import matplotlib.pyplot as plt

# 1. 读取评分数据
df = pd.read_csv("data/ratings.csv")

score_cols = ["accuracy", "helpfulness", "clarity", "actionability", "risk_control"]

print("===== BASIC INFO =====")
print(df.head())
print("\nShape:", df.shape)
print("\nMissing values:")
print(df.isna().sum())

# 2. 整体平均分
print("\n===== OVERALL PERFORMANCE =====")
print("Average overall score:", df["overall_score"].mean())

# 3. 各评分维度平均分
print("\n===== AVERAGE SCORE BY DIMENSION =====")
dimension_scores = df[score_cols].mean().sort_values(ascending=False)
print(dimension_scores)

# 4. 按 category 分析整体分数
print("\n===== OVERALL SCORE BY CATEGORY =====")
category_scores = df.groupby("category")["overall_score"].mean().sort_values(ascending=False)
print(category_scores)

# 5. 按 difficulty 分析整体分数
print("\n===== OVERALL SCORE BY DIFFICULTY =====")
difficulty_scores = df.groupby("difficulty")["overall_score"].mean()
print(difficulty_scores)

# 6. 按 expected_risk 分析 risk_control
print("\n===== RISK CONTROL BY EXPECTED RISK =====")
risk_control_scores = df.groupby("expected_risk")["risk_control"].mean()
print(risk_control_scores)

# 7. 错误类型统计
print("\n===== ERROR TYPE DISTRIBUTION =====")
error_counts = df["error_type"].value_counts()
print(error_counts)

# 8. 找出低分回答
print("\n===== LOW SCORE CASES =====")
low_score_cases = df[df["overall_score"] < 4.0][
    ["question_id", "category", "expected_risk", "question_text", "overall_score", "error_type", "notes"]
]
print(low_score_cases)

# 9. 图1：各维度平均分
plt.figure()
dimension_scores.plot(kind="bar")
plt.title("Average Score by Evaluation Dimension")
plt.xlabel("Dimension")
plt.ylabel("Score")
plt.ylim(0, 5)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("figures/dimension_scores.png")
plt.show()

# 10. 图2：不同类别平均分
plt.figure()
category_scores.plot(kind="barh")
plt.title("Overall Score by Question Category")
plt.xlabel("Overall Score")
plt.xlim(0, 5)
plt.tight_layout()
plt.savefig("category_scores.png")
plt.show()

# 11. 图3：风险等级对应的 risk_control 分数
plt.figure()
risk_control_scores.plot(kind="bar")
plt.title("Risk Control Score by Expected Risk Level")
plt.xlabel("Expected Risk")
plt.ylabel("Risk Control Score")
plt.ylim(0, 5)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("risk_control_by_risk.png")
plt.show()

# 12. 图4：错误类型分布
plt.figure()
error_counts.plot(kind="bar")
plt.title("Error Type Distribution")
plt.xlabel("Error Type")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("error_type_distribution.png")
plt.show()

# 13. 保存分析结果表
summary = pd.DataFrame({
    "dimension": dimension_scores.index,
    "average_score": dimension_scores.values
})

summary.to_csv("rating_dimension_summary.csv", index=False)

print("\nAnalysis complete.")
print("Charts saved:")
print("- dimension_scores.png")
print("- category_scores.png")
print("- risk_control_by_risk.png")
print("- error_type_distribution.png")
print("Summary saved as rating_dimension_summary.csv")