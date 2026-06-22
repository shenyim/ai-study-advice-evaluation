import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(
    page_title="AI Study Advice Evaluation",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/ratings.csv")
    return df

df = load_data()

score_cols = ["accuracy", "helpfulness", "clarity", "actionability", "risk_control"]

# Title
st.title("AI Study Advice Assistant Evaluation Dashboard")

st.write(
    """
    This dashboard evaluates a simulated AI study advice assistant using a human-centered data science approach.
    The assistant is scored across accuracy, helpfulness, clarity, actionability, and risk control.
    """
)

# Sidebar filters
st.sidebar.header("Filters")

category_options = ["All"] + sorted(df["category"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Select category", category_options)

risk_options = ["All"] + sorted(df["expected_risk"].dropna().unique().tolist())
selected_risk = st.sidebar.selectbox("Select expected risk", risk_options)

difficulty_options = ["All"] + sorted(df["difficulty"].dropna().unique().tolist())
selected_difficulty = st.sidebar.selectbox("Select difficulty", difficulty_options)

filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]

if selected_risk != "All":
    filtered_df = filtered_df[filtered_df["expected_risk"] == selected_risk]

if selected_difficulty != "All":
    filtered_df = filtered_df[filtered_df["difficulty"] == selected_difficulty]

# Key metrics
st.subheader("Overall Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Number of Questions", len(filtered_df))

if len(filtered_df) > 0:
    col2.metric("Average Overall Score", f"{filtered_df['overall_score'].mean():.2f} / 5")
    col3.metric("Average Risk Control", f"{filtered_df['risk_control'].mean():.2f} / 5")
    col4.metric("Average Actionability", f"{filtered_df['actionability'].mean():.2f} / 5")
else:
    col2.metric("Average Overall Score", "N/A")
    col3.metric("Average Risk Control", "N/A")
    col4.metric("Average Actionability", "N/A")

if len(filtered_df) == 0:
    st.warning("No data available for the selected filters.")
    st.stop()

# Dimension scores
st.subheader("Average Score by Evaluation Dimension")

dimension_scores = filtered_df[score_cols].mean().sort_values(ascending=False)

fig1, ax1 = plt.subplots()
dimension_scores.plot(kind="bar", ax=ax1)
ax1.set_ylim(0, 5)
ax1.set_ylabel("Score")
ax1.set_xlabel("Evaluation Dimension")
ax1.set_title("Average Score by Dimension")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig1)

# Category scores
st.subheader("Overall Score by Question Category")

category_scores = filtered_df.groupby("category")["overall_score"].mean().sort_values(ascending=True)

fig2, ax2 = plt.subplots()
category_scores.plot(kind="barh", ax=ax2)
ax2.set_xlim(0, 5)
ax2.set_xlabel("Overall Score")
ax2.set_ylabel("Category")
ax2.set_title("Overall Score by Category")
plt.tight_layout()

st.pyplot(fig2)

# Risk control
st.subheader("Risk Control by Expected Risk Level")

risk_scores = filtered_df.groupby("expected_risk")["risk_control"].mean()

fig3, ax3 = plt.subplots()
risk_scores.plot(kind="bar", ax=ax3)
ax3.set_ylim(0, 5)
ax3.set_ylabel("Risk Control Score")
ax3.set_xlabel("Expected Risk")
ax3.set_title("Risk Control by Expected Risk")
plt.xticks(rotation=0)
plt.tight_layout()

st.pyplot(fig3)

# Error type distribution
st.subheader("Error Type Distribution")

error_counts = filtered_df["error_type"].value_counts()

fig4, ax4 = plt.subplots()
error_counts.plot(kind="bar", ax=ax4)
ax4.set_ylabel("Count")
ax4.set_xlabel("Error Type")
ax4.set_title("Error Type Distribution")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig4)

# Low-score cases
st.subheader("Low Score Cases")

threshold = st.slider("Show answers with overall score below:", min_value=1.0, max_value=5.0, value=4.0, step=0.1)

low_score_df = filtered_df[filtered_df["overall_score"] < threshold]

if len(low_score_df) == 0:
    st.success("No low-score cases under the selected threshold.")
else:
    st.dataframe(
        low_score_df[
            [
                "question_id",
                "category",
                "difficulty",
                "expected_risk",
                "question_text",
                "answer_text",
                "overall_score",
                "error_type",
                "notes"
            ]
        ],
        use_container_width=True
    )

# Full data table
st.subheader("Full Evaluation Data")

st.dataframe(
    filtered_df[
        [
            "question_id",
            "category",
            "difficulty",
            "expected_risk",
            "question_text",
            "overall_score",
            "accuracy",
            "helpfulness",
            "clarity",
            "actionability",
            "risk_control",
            "error_type",
            "notes"
        ]
    ],
    use_container_width=True
)

# Product recommendations
st.subheader("Product Recommendations")

st.markdown(
    """
    Based on the evaluation results, the AI study advice assistant can be improved in several ways:

    1. **Improve actionability**  
       Some answers are correct but should include more concrete steps, examples, and timelines.

    2. **Add stronger risk control for high-risk questions**  
       PhD planning, career planning, and academic decision questions should include uncertainty warnings and encourage students to verify important information.

    3. **Increase personalization**  
       The assistant should ask follow-up questions about the student's background, goals, timeline, and skill level.

    4. **Track evaluation metrics continuously**  
       Future versions should monitor answer quality across category, risk level, difficulty, and error type.
    """
)