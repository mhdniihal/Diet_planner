# 🥗 Diet Planner Using BMI Calculator

## 📌 Project Overview

Diet Planner Using BMI Calculator is a Data Science project that helps users analyze their health condition and generate personalized diet plans based on their Body Mass Index (BMI), activity level, and fitness goals.

The system calculates BMI, predicts daily calorie requirements using a Machine Learning model, and recommends suitable breakfast, lunch, and dinner options to help users achieve their goals such as Bulking, Cutting, or Fat Loss.

---

## 🎯 Objectives

* Calculate BMI using user health parameters.
* Classify users into BMI categories.
* Predict daily calorie requirements using Machine Learning.
* Generate personalized diet recommendations.
* Provide a simple and interactive Streamlit dashboard.
* Encourage healthy lifestyle habits and fitness goals.

---

## 👥 Target Users

This application is designed for:

* Health-conscious individuals
* Fitness enthusiasts
* Students and professionals
* People aged between 12 and 68 years
* Users aiming for:

  * Weight Gain (Bulk)
  * Weight Loss (Fat Loss)
  * Body Recomposition (Cut)

---

## 📊 Datasets Used

### 1. Health & BMI Dataset

Contains:

* Age
* Gender
* Height
* Weight
* BMI
* Blood Pressure
* Sleep Hours
* Activity Level
* Fitness Goal

### 2. Food Nutrition Dataset

Contains:

* Food Item
* Calories
* Protein
* Carbohydrates
* Fat
* Meal Type
* Food Category

### 3. Calorie Requirement Dataset

Contains:

* Age
* Gender
* Height
* Weight
* BMI
* Physical Activity Level
* Daily Caloric Intake

---

## 🛠 Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Random Forest Regressor

### Deployment

* Streamlit

### Model Storage

* Joblib

---

## ⚙️ Project Workflow

### Step 1: Data Cleaning

* Removed duplicates
* Handled missing values
* Standardized column names
* Converted data types

### Step 2: Exploratory Data Analysis (EDA)

* BMI Distribution
* Goal Distribution
* Calorie Analysis
* Food Nutrition Analysis
* Correlation Heatmap

### Step 3: BMI Calculator

BMI is calculated using:

BMI = Weight (kg) / Height² (m²)

BMI Categories:

| BMI Range   | Category      |
| ----------- | ------------- |
| < 18.5      | Underweight   |
| 18.5 – 24.9 | Normal Weight |
| 25 – 29.9   | Overweight    |
| ≥ 30        | Obese         |

### Step 4: Calorie Prediction Model

Input Features:

* Age
* Gender
* Weight
* Height
* BMI
* Activity Level

Target:

* Daily Caloric Intake

Algorithm:

* Random Forest Regressor

### Step 5: Diet Recommendation Engine

The system recommends meals based on:

* BMI
* Predicted Calories
* User Goal

Meal Plans:

* Breakfast
* Lunch
* Dinner

### Step 6: Streamlit Dashboard

Interactive dashboard where users can:

* Enter health information
* Calculate BMI
* Predict calorie requirements
* Generate diet plans

---

## 🚀 Features

✅ BMI Calculation

✅ BMI Category Detection

✅ Daily Calorie Prediction

✅ Personalized Diet Planning

✅ Goal-Based Recommendations

✅ Interactive User Interface

✅ Streamlit Dashboard

---

## 📂 Project Structure

Diet_Planner_BMI/

├── data/

│   ├── Health_BMI_Dataset.csv

│   ├── Food_Nutrition_Dataset.csv

│   └── Calorie_Requirement_Dataset.csv

│

├── models/

│   └── calorie_model.pkl

│

├── src/

│   ├── data_cleaning.py

│   ├── eda.py

│   ├── bmi_calculator.py

│   ├── calorie_prediction.py

│   ├── diet_recommender.py

│   └── app.py

│

├── requirements.txt

│

└── README.md

---

## ▶️ How to Run

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit Application

```bash
streamlit run src/app.py
```

### 5. Open Browser

```text
http://localhost:8501
```

---

## 📈 Expected Output

The system generates:

* BMI Score
* BMI Category
* Daily Calorie Requirement
* Breakfast Plan
* Lunch Plan
* Dinner Plan
* Goal-Based Health Recommendations

---

## 🔮 Future Enhancements

* Disease-specific diet plans
* Diabetes diet recommendation
* Blood pressure monitoring
* Weekly meal planner
* Workout recommendation system
* Mobile application integration
* AI-powered meal generation
* Progress tracking dashboard

---

## 📋 Conclusion

The Diet Planner Using BMI Calculator successfully combines Data Science, Machine Learning, and Health Analytics to provide personalized nutrition guidance. By analyzing user health parameters and predicting calorie requirements, the system helps users make informed dietary decisions and work toward their fitness goals through an easy-to-use web application.

---

## 👨‍💻 Developed By

**Mohammed Nihal**

Data Science & Machine Learning Project
