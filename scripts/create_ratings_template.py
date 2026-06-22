import pandas as pd

# 1. 读取问题和 AI 回答
questions = pd.read_csv("student_questions_clean.csv")
answers = pd.read_csv("ai_answers.csv")

# 2. 合并，方便你评分时看到问题和回答
df = answers.merge(questions, on="question_id", how="left")

# 3. 创建评分列，先留空
df["accuracy"] = ""
df["helpfulness"] = ""
df["clarity"] = ""
df["actionability"] = ""
df["risk_control"] = ""
df["overall_score"] = ""
df["error_type"] = ""
df["notes"] = ""

# 4. 调整列顺序
columns = [
    "question_id",
    "category",
    "difficulty",
    "expected_risk",
    "student_background",
    "question_text",
    "model_name",
    "answer_text",
    "answer_length",
    "accuracy",
    "helpfulness",
    "clarity",
    "actionability",
    "risk_control",
    "overall_score",
    "error_type",
    "notes"
]

df = df[columns]

# 5. 保存评分模板
df.to_csv("ratings_template.csv", index=False)

print("ratings_template.csv created.")
print("Rows:", df.shape[0])
print(df[["question_id", "category", "expected_risk", "question_text"]].head())