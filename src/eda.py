import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

health_df = pd.read_csv("data/cleaned/health_cleaned.csv")
food_df = pd.read_csv("data/cleaned/food_cleaned.csv")
calorie_df = pd.read_csv("data/cleaned/calorie_cleaned.csv")

# BMI distribution
plt.figure(figsize=(8,5))
sns.histplot(health_df['BMI'], bins=20, kde=True)
plt.title("BMI Distribution")
plt.show()

# Goal distribution
plt.figure(figsize=(8,5))
sns.countplot(x='Goal', data=health_df)
plt.title("Goal Distribution")
plt.show()

# Age vs BMI
plt.figure(figsize=(8,5))
sns.scatterplot(x='Age', y='BMI', data=health_df)
plt.title("Age vs BMI")
plt.show()