import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Streamlit App Title
st.title("Credit Score Tracker and Score Ingredients Analyzer")

# Sidebar Input for Credit Factors
st.sidebar.header("Credit Score Components")
payment_history = st.sidebar.slider("Payment History (35%)", 0, 100, 90)
amount_of_debt = st.sidebar.slider("Amount of Debt (30%)", 0, 100, 50)
credit_history_length = st.sidebar.slider("Length of Credit History (15%)", 0, 100, 40)
new_credit_amount = st.sidebar.slider("Amount of New Credit (10%)", 0, 100, 20)
credit_mix = st.sidebar.slider("Credit Mix (10%)", 0, 100, 30)

# Calculate the Score based on Inputs
def calculate_fico_score():
    score = (
        payment_history * 0.35 +
        amount_of_debt * 0.30 +
        credit_history_length * 0.15 +
        new_credit_amount * 0.10 +
        credit_mix * 0.10
    )
    return min(850, int(score * 8.5))  # Scale score to 850 max

current_score = calculate_fico_score()

# Display the Calculated Score
st.header("Calculated FICO Score")
st.metric("Your FICO Score:", current_score)

# Credit Summary Section
st.header("Debt Summary")
st.write("Enter current balances for the following debt categories:")

# Debt Type Input
credit_card_debt = st.number_input("Credit Card Debt", min_value=0, value=5000, step=100)
real_estate_loans = st.number_input("Real Estate Loans", min_value=0, value=150000, step=1000)
student_loans = st.number_input("Student Loans", min_value=0, value=20000, step=500)
personal_loans = st.number_input("Personal Loans", min_value=0, value=3000, step=100)
collections = st.number_input("Collections", min_value=0, value=500, step=50)

# Display the Debt Summary
debt_data = {
    "Type": ["Credit Cards", "Real Estate", "Student Loans", "Personal Loans", "Collections"],
    "Amount": [credit_card_debt, real_estate_loans, student_loans, personal_loans, collections]
}
debt_df = pd.DataFrame(debt_data)
st.table(debt_df)

# Score Tracker Section
st.header("Credit Score Tracker")
st.write("Track changes in your score over time across different categories.")

# Sample Data for Score Tracking (this can be modified or replaced with user input over time)
dates = pd.date_range(datetime(2022, 1, 1), periods=12, freq='M')
sample_data = {
    "Credit Cards": np.random.randint(600, 850, len(dates)),
    "Auto Loans": np.random.randint(600, 850, len(dates)),
    "Mortgages": np.random.randint(600, 850, len(dates))
}
score_tracker_df = pd.DataFrame(sample_data, index=dates)

# Plot Score Tracker
fig, ax = plt.subplots(figsize=(10, 6))
for column in score_tracker_df.columns:
    ax.plot(score_tracker_df.index, score_tracker_df[column], label=column)
ax.set_title("Credit Score Tracker")
ax.set_ylabel("FICO Score")
ax.set_xlabel("Time")
ax.set_ylim(550, 850)
ax.legend()
st.pyplot(fig)

# Additional Insights Section
st.header("Insights")
st.write("""
    - **Payment History (35%)**: The most significant factor. Ensure all payments are on time.
    - **Amount of Debt (30%)**: Keep debt levels low relative to your credit limits.
    - **Credit History Length (15%)**: Older accounts contribute positively.
    - **Amount of New Credit (10%)**: Avoid opening multiple new accounts in a short time.
    - **Credit Mix (10%)**: A variety of credit types (e.g., cards, loans) can improve scores.
""")

