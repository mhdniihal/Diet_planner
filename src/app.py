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

# BMI Calculation
bmi = 0
def calculate_bmi(weight, height):

    height_m = height / 100

    bmi = weight / (height_m ** 2)

    return round(bmi, 2)

if st.button("Calculate BMI"):

    bmi = calculate_bmi(weight, height)

    st.success(f"Your BMI is {bmi}")


# BMI Category
def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"
    
category = bmi_category(bmi)

st.info(f"Category: {category}")


import joblib

model = joblib.load(
    "models/calorie_model.pkl"
)

sample = [[
    age,
    weight,
    height,
    bmi
]]

calories = model.predict(sample)

st.success(
    f"Recommended Calories: {int(calories[0])} kcal/day"
)