import pandas as pd

# 1. 读取清洗后的问题数据
questions = pd.read_csv("student_questions_clean.csv")

# 2. 手动/模拟生成 AI 回答
answer_map = {
    "Q001": "Start with Python basics such as variables, loops, functions, and lists. Then learn pandas and numpy for data analysis. After that, practice with small CSV datasets and build simple projects like cleaning student data or analyzing course reviews.",
    
    "Q002": "With one week before your statistics exam, divide your review into topics. Spend the first two days reviewing probability and distributions, the next two days on hypothesis testing and confidence intervals, and the final days doing practice problems. Focus more on weak areas.",
    
    "Q003": "You can apply for a PhD without research experience, but it is usually a major disadvantage. PhD programs care strongly about research potential, so you should try to gain RA experience, complete a research-style project, and get strong faculty recommendations before applying.",
    
    "Q004": "Yes, you still need to learn pandas even if you use AI to write code. AI can generate code, but you need pandas knowledge to check whether the code is correct, debug errors, understand data transformations, and explain your analysis decisions.",
    
    "Q005": "Both GPA and research matter for PhD applications, but research experience and strong recommendation letters are usually more important for showing research potential. A strong GPA helps, but it cannot fully replace research experience, especially for competitive programs.",
    
    "Q006": "To clean a dataset, first inspect its shape, column types, missing values, duplicates, and unusual values. Then remove duplicates, standardize text formats, convert data types, handle missing values carefully, and document every cleaning decision.",
    
    "Q007": "If your main goal is applying for a PhD, RA experience is usually more valuable than a general internship because it directly shows research ability. However, an AI or data-focused research internship can also be useful if it involves evaluation, experiments, or publishable work.",
    
    "Q008": "To detect hallucination, check whether the AI provides unsupported facts, overly specific claims without sources, outdated information, or confident answers to uncertain questions. For important decisions, verify the answer using official sources or expert advice.",
    
    "Q009": "To prepare for a machine learning course, review Python, linear algebra, probability, statistics, and basic calculus. You should also understand train-test split, overfitting, regression, classification, and evaluation metrics before the course starts.",
    
    "Q010": "AI will not completely replace data scientists, but it will change the job. Routine coding and reporting may become more automated, while skills like problem framing, data quality judgment, experimental design, model evaluation, and business interpretation will become more important.",
    
    "Q011": "Important SQL skills for data science include SELECT, WHERE, GROUP BY, JOIN, subqueries, common table expressions, and window functions. You should be comfortable extracting, aggregating, and combining data from multiple tables.",
    
    "Q012": "To evaluate an AI chatbot, define clear criteria such as accuracy, helpfulness, clarity, safety, personalization, and risk control. Then collect test questions, score the chatbot responses, analyze failure cases, and identify where the system needs improvement.",
    
    "Q013": "You should not blindly trust AI career advice. AI can help brainstorm options, but career decisions depend on your background, goals, constraints, and current market information. Use AI as a starting point, then verify with advisors, mentors, and official sources.",
    
    "Q014": "To build a data visualization dashboard, first define the key questions and metrics. Then clean the data, create charts, organize them into a clear layout, and make the dashboard interactive using tools like Streamlit, Tableau, Power BI, or Plotly Dash."
}

# 3. 生成回答表
rows = []

for _, row in questions.iterrows():
    qid = row["question_id"]
    answer = answer_map.get(qid, "No answer available.")
    
    rows.append({
        "question_id": qid,
        "model_name": "Simulated_GPT",
        "answer_text": answer,
        "answer_length": len(answer.split())
    })

answers = pd.DataFrame(rows)

# 4. 保存
answers.to_csv("ai_answers.csv", index=False)

print("AI answers saved as ai_answers.csv")
print(answers.head())
print("\nShape:", answers.shape)