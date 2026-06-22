import pandas as pd

df = pd.read_csv("ratings.csv")

score_cols = ["accuracy", "helpfulness", "clarity", "actionability", "risk_control"]

overall_avg = df["overall_score"].mean()
dimension_scores = df[score_cols].mean().sort_values(ascending=False)
category_scores = df.groupby("category")["overall_score"].mean().sort_values(ascending=False)
risk_scores = df.groupby("expected_risk")["risk_control"].mean().sort_values(ascending=False)
error_counts = df["error_type"].value_counts()

with open("report_summary.txt", "w") as f:
    f.write("REPORT SUMMARY\n")
    f.write("====================\n\n")

    f.write(f"Average overall score: {overall_avg:.2f} / 5\n\n")

    f.write("Average score by dimension:\n")
    for dim, score in dimension_scores.items():
        f.write(f"- {dim}: {score:.2f}\n")

    f.write("\nOverall score by category:\n")
    for cat, score in category_scores.items():
        f.write(f"- {cat}: {score:.2f}\n")

    f.write("\nRisk control by expected risk:\n")
    for risk, score in risk_scores.items():
        f.write(f"- {risk}: {score:.2f}\n")

    f.write("\nError type distribution:\n")
    for err, count in error_counts.items():
        f.write(f"- {err}: {count}\n")

print("report_summary.txt created.")