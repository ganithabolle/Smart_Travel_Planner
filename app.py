import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import recommend_trip, suggest_vehicle
from utils import load_data

st.set_page_config(page_title="Smart AI Travel Planner", layout="wide")
st.title("🌍 Smart AI Travel Planner")

import sys

# Load data
try:
    data = load_data()
except FileNotFoundError as e:
    st.error(f"File not found: {e}")
    if hasattr(st, "stop"):
        st.stop()
    print(f"ERROR: File not found: {e}")
    sys.exit(1)
except pd.errors.EmptyDataError as e:
    st.error(f"Invalid CSV content: {e}")
    if hasattr(st, "stop"):
        st.stop()
    print(f"ERROR: Invalid CSV content: {e}")
    sys.exit(1)

if 'data' not in globals() or data is None:
    # Fail-fast in non-Streamlit / stray execution paths
    print("ERROR: Data not loaded. Exiting.")
    sys.exit(1)

# Sidebar inputs
st.sidebar.header("🧳 Plan Your Trip")
interest = st.sidebar.selectbox("Select Interest", data["Interest"].unique())
budget = st.sidebar.slider("Budget (₹)", 1000, 50000, 10000)
distance = st.sidebar.slider("Distance (km)", 50, 2000, 300)

# AI Recommendations
results = recommend_trip(data, interest, budget)
st.subheader("🤖 AI Recommended Places")
for _, row in results.iterrows():
    st.markdown(f"""
    ### 📍 {row['Place']} ({row['Location']})
    🎯 Interest: {row['Interest']}  
    🏨 Hotel: {row['Hotel']}  
    💰 Price: ₹{row['Price']}
    """)

# Vehicle Suggestion
vehicle = suggest_vehicle(distance, budget)
st.subheader("🚗 Suggested Vehicle")
st.success(vehicle)

# Map
st.subheader("🗺 Travel Map")
st.map(results[["lat", "lon"]])

# Hotel Table
st.subheader("🏨 Hotel Details")
st.dataframe(results[["Place", "Hotel", "Price"]])

# Charts
st.subheader("📊 Budget Distribution")
budget_df = pd.DataFrame({
    "Category": ["Hotel", "Food", "Travel"],
    "Amount": [budget * 0.5, budget * 0.3, budget * 0.2]
})
fig, ax = plt.subplots()
ax.pie(budget_df["Amount"], labels=budget_df["Category"], autopct="%1.1f%%")
st.pyplot(fig)

st.subheader("📊 Travel Summary")
summary_df = pd.DataFrame({
    "Type": ["Places", "Hotels", "Vehicle"],
    "Count": [len(results), len(results), 1]
})
fig2, ax2 = plt.subplots()
ax2.bar(summary_df["Type"], summary_df["Count"])
st.pyplot(fig2)

# Feedback
st.subheader("💬 Feedback")
feedback = st.text_area("Write your feedback")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback! 😊")
