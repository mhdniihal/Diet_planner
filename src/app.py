import streamlit as st
import joblib

from diet_recommender import generate_diet

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Diet Planner",
    page_icon="🥗",
    layout="centered"
)

# =====================================
# TITLE
# =====================================

st.title("🥗 Diet Planner Using BMI Calculator")

st.write(
    "Generate personalized diet plans based on your BMI and fitness goals."
)

# =====================================
# USER INPUTS
# =====================================

age = st.number_input(
    "Age",
    min_value=12,
    max_value=68,
    value=21
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"],
    key="gender"
)

height = st.number_input(
    "Height (cm)",
    min_value=100.0,
    max_value=250.0,
    value=170.0
)

weight = st.number_input(
    "Weight (kg)",
    min_value=20.0,
    max_value=250.0,
    value=70.0
)

activity = st.selectbox(
    "Activity Level",
    ["Low", "Moderate", "High"],
    key="activity"
)

goal = st.selectbox(
    "Goal",
    ["Bulk", "Cut", "Fat Loss"],
    key="goal"
)

# =====================================
# FUNCTIONS
# =====================================

def calculate_bmi(weight, height):

    height_m = height / 100

    bmi = weight / (height_m ** 2)

    return round(bmi, 2)


def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


# =====================================
# LOAD MODEL
# =====================================

try:
    model = joblib.load(
        "models/calorie_model.pkl"
    )

except Exception as e:

    st.error(f"Model Loading Error: {e}")

# =====================================
# BUTTON
# =====================================

if st.button("🚀 Generate Diet Plan"):

    try:

        # BMI Calculation
        bmi = calculate_bmi(weight, height)

        category = bmi_category(bmi)

        st.subheader("BMI Analysis")

        st.success(f"BMI: {bmi}")

        st.info(f"Category: {category}")

        # Encoding

        gender_encoded = 1 if gender == "Male" else 0

        activity_map = {
            "Low": 0,
            "Moderate": 1,
            "High": 2
        }

        activity_encoded = activity_map[activity]

        # Prediction Input

        sample = [[
            age,
            gender_encoded,
            weight,
            height,
            bmi,
            activity_encoded
        ]]

        # Calorie Prediction

        calories = model.predict(sample)

        st.subheader("Daily Calorie Requirement")

        st.success(
            f"{int(calories[0])} kcal/day"
        )

        # Diet Recommendation

        breakfast, lunch, dinner = generate_diet(goal)

        # Breakfast

        st.subheader("🍳 Breakfast")

        breakfast_items = breakfast["Food_Item"].tolist()

        for i, item in enumerate(
            breakfast_items,
            start=1
        ):
            st.write(f"{i}. {item}")

        # Lunch

        st.subheader("🍛 Lunch")

        lunch_items = lunch["Food_Item"].tolist()

        for i, item in enumerate(
            lunch_items,
            start=1
        ):
            st.write(f"{i}. {item}")

        # Dinner

        st.subheader("🌙 Dinner")

        dinner_items = dinner["Food_Item"].tolist()

        for i, item in enumerate(
            dinner_items,
            start=1
        ):
            st.write(f"{i}. {item}")

        # Footer

        st.markdown("---")

        st.success(
            "Diet plan generated successfully!"
        )

    except Exception as e:

        st.error(
            f"Application Error: {e}"
        )