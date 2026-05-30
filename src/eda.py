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

# calories by activity level
plt.figure(figsize=(8,5))
sns.boxplot(
    x='Physical_Activity_Level',
    y='Daily_Caloric_Intake',
    data=calorie_df
)
plt.show()  


# protein food distribution
top_protein = food_df.sort_values(
    by='Protein (g)',
    ascending=False
).head(10)

plt.figure(figsize=(10,5))
sns.barplot(
    x='Protein (g)',
    y='Food_Item',
    data=top_protein
)
plt.title("Top Protein Foods")
plt.show()

