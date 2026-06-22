import pandas as pd

df = pd.read_csv("ratings_template.csv")

sample_scores = {
    "Q001": [5, 5, 5, 5, 5, "none", "Clear beginner-friendly Python learning plan."],
    "Q002": [5, 4, 5, 4, 4, "none", "Good weekly review plan, but could mention practice exams."],
    "Q003": [5, 5, 5, 4, 5, "none", "Strong risk control; clearly states research experience matters."],
    "Q004": [5, 5, 5, 5, 5, "none", "Good explanation of why pandas still matters with AI coding."],
    "Q005": [5, 4, 5, 3, 4, "missing_steps", "Accurate, but could give more specific application strategy."],
    "Q006": [5, 5, 5, 5, 5, "none", "Clear data cleaning workflow."],
    "Q007": [5, 5, 5, 4, 5, "none", "Good comparison between RA and internship for PhD goals."],
    "Q008": [5, 4, 5, 4, 5, "none", "Good hallucination detection advice."],
    "Q009": [5, 4, 5, 4, 4, "missing_steps", "Good topic list, but could include a concrete weekly plan."],
    "Q010": [5, 5, 5, 4, 5, "none", "Balanced answer about AI and data scientist roles."],
    "Q011": [5, 4, 5, 4, 4, "missing_steps", "Good SQL list, but could include examples."],
    "Q012": [5, 5, 5, 5, 5, "none", "Very aligned with AI evaluation framework."],
    "Q013": [5, 5, 5, 4, 5, "none", "Good warning about not blindly trusting AI advice."],
    "Q014": [5, 4, 5, 4, 4, "none", "Good dashboard workflow, could be more detailed about metrics."]
}

for qid, values in sample_scores.items():
    mask = df["question_id"] == qid

    df.loc[mask, "accuracy"] = values[0]
    df.loc[mask, "helpfulness"] = values[1]
    df.loc[mask, "clarity"] = values[2]
    df.loc[mask, "actionability"] = values[3]
    df.loc[mask, "risk_control"] = values[4]
    df.loc[mask, "error_type"] = values[5]
    df.loc[mask, "notes"] = values[6]

score_cols = ["accuracy", "helpfulness", "clarity", "actionability", "risk_control"]

for col in score_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["overall_score"] = df[score_cols].mean(axis=1)

df.to_csv("ratings.csv", index=False)

print("ratings.csv created.")
print(df[["question_id", "overall_score", "error_type"]])