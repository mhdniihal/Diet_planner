import streamlit as st

st.title("🥗 Diet Planner Using BMI Calculator")
st.write("Generate personalized diet plans based on your BMI and fitness goals.")

# User Inputs
age = st.number_input(
    "Age",
    min_value=12,
    max_value=68
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

height = st.number_input(
    "Height (cm)"
)

weight = st.number_input(
    "Weight (kg)"
)

goal = st.selectbox(
    "Goal",
    ["Bulk", "Cut", "Fat Loss"]
)

