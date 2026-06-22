## Live Demo

[Open the Streamlit Dashboard](https://ai-study-advice-evaluation.streamlit.app/)

## Disclaimer

This project uses simulated student questions and simulated GPT-style answers. It is intended as a small MVP demonstration of an AI evaluation workflow, not a production-level evaluation system.

# AI Study Advice Assistant Evaluation

This project evaluates a simulated AI study advice assistant using a human-centered data science workflow.

The goal is to assess whether AI-generated study advice is accurate, helpful, clear, actionable, and safe for student decision-making.

## Project Workflow

1. Create a student question dataset
2. Clean and standardize the data
3. Conduct exploratory data analysis
4. Generate simulated AI answers
5. Evaluate answers using a human-centered rubric
6. Analyze scores and error types
7. Write product evaluation recommendations
8. Build an interactive Streamlit dashboard

## Evaluation Dimensions

Each AI answer is evaluated across five dimensions:

- Accuracy
- Helpfulness
- Clarity
- Actionability
- Risk Control

## Tech Stack

- Python
- pandas
- matplotlib
- Streamlit

## Project Structure

```text
AI-STUDY-ADVICE-EVALUATION/
├── data/
├── scripts/
├── figures/
├── reports/
├── dashboard.py
├── README.md
├── requirements.txt
└── .gitignore