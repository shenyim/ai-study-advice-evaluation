# Evaluating an AI Study Advice Assistant

## 1. Project Overview

This project evaluates an AI study advice assistant designed to answer student questions about programming, statistics, data science, machine learning, AI learning, PhD planning, and career planning.

The goal of this project is not only to test whether the assistant can give useful answers, but also to evaluate whether its responses are accurate, clear, actionable, and safe for student decision-making.

This project follows a human-centered data science workflow:

1. Data collection
2. Data cleaning
3. Exploratory data analysis
4. AI answer generation
5. Human-centered evaluation
6. Product-level analysis
7. Product improvement recommendations

---

## 2. Dataset

The dataset contains student questions related to academic learning and career planning.

The main fields include:

- `question_id`: unique question identifier
- `question_text`: student question
- `category`: topic category
- `difficulty`: estimated question difficulty
- `student_background`: student background
- `expected_risk`: expected risk level if the AI gives poor advice

After cleaning, duplicate question IDs were removed, text fields were standardized, missing student background values were filled as `unknown`, and inconsistent labels were corrected.

---

## 3. Evaluation Rubric

Each AI answer was evaluated using five dimensions:

| Dimension | Meaning |
|---|---|
| Accuracy | Whether the answer is factually and conceptually correct |
| Helpfulness | Whether the answer is useful for the student |
| Clarity | Whether the answer is easy to understand |
| Actionability | Whether the answer gives concrete next steps |
| Risk Control | Whether the answer avoids overconfidence, misleading advice, or unsupported claims |

Each dimension was scored from 1 to 5.

The overall score was calculated as the average of the five dimension scores.

---

## 4. Key Results

The AI study advice assistant performed well overall in this small evaluation.

Its strongest dimension was clarity. Most answers were easy to understand and written in a student-friendly way.

The assistant also performed well on basic technical learning questions, such as how to start learning Python, how to clean a dataset, and what SQL skills are useful for data science.

However, the assistant was weaker in actionability for some answers. Some responses gave correct general advice but did not always provide detailed steps, examples, or personalized planning.

---

## 5. Category-Level Findings

The assistant performed better on technical learning categories such as:

- programming
- data science
- AI evaluation
- machine learning

These questions usually have clearer answers and lower decision-making risk.

The assistant required more careful evaluation for categories such as:

- PhD planning
- career planning

These topics are more complex because they depend heavily on the student's background, goals, academic record, research experience, and constraints.

---

## 6. Risk-Level Findings

High-risk questions require stronger risk control because poor answers may influence important student decisions.

Examples of high-risk questions include:

- Can I apply for a PhD without research experience?
- Should I choose an internship or RA if I want to apply for a PhD?
- Should I trust AI career advice?

For these questions, the assistant should avoid overly confident claims and should clearly state limitations. It should also encourage students to verify important information with advisors, faculty members, or official sources.

---

## 7. Error Analysis

The most common error type in this evaluation was `missing_steps`.

This means that some answers were generally correct but lacked specific next actions.

For example, an answer might correctly say that SQL is important for data science, but it may not provide a concrete learning sequence or example tasks.

Another potential issue is insufficient personalization. Some answers could be improved by asking about the student's background, current skill level, academic goal, or timeline.

---

## 8. Product Recommendations

Based on this evaluation, the AI study advice assistant should be improved in four ways.

### 1. Add stronger guardrails for high-risk advice

For PhD planning, career planning, academic policy, and other high-impact topics, the assistant should include uncertainty warnings and encourage students to verify information with official sources.

### 2. Improve personalization

The assistant should ask follow-up questions when the student's background is unclear. For example, it could ask about GPA, research experience, programming level, career goals, or application timeline.

### 3. Make answers more actionable

The assistant should provide step-by-step plans, example tasks, timelines, and resource suggestions instead of only giving general advice.

### 4. Build a continuous evaluation dashboard

The product team should track answer quality across categories, risk levels, and error types. This would help identify weak areas and improve the system over time.

---

## 9. Limitations

This project has several limitations.

First, the dataset is small and contains only a limited number of student questions.

Second, the AI answers were generated using a simulated GPT-style response set rather than a real API-based multi-model comparison.

Third, there was only one evaluator, so the ratings may contain subjective bias.

Fourth, this project did not include real student user testing.

Future work should include more questions, multiple real AI models, multiple human raters, and real user feedback.

---

## 10. Conclusion

This project shows how a human-centered data science workflow can be used to evaluate an AI study advice assistant.

The assistant appears useful for general technical learning support, especially for programming, data science, and AI learning questions.

However, high-risk academic and career planning questions require stronger risk control, better personalization, and more concrete action steps.

Overall, this project demonstrates that AI assistants should not only be evaluated by whether they sound helpful, but also by whether they are accurate, actionable, safe, and appropriate for real student decision-making.