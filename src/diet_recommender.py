import pandas as pd

food_df = pd.read_csv("data/cleaned/food_cleaned.csv")
print(food_df.head())
print(food_df.columns)


food_df['Calories (kcal)'] = pd.to_numeric(
    food_df['Calories (kcal)'],
    errors='coerce'
)

food_df.dropna(subset=['Calories (kcal)'], inplace=True)

# fat loss foods separated
fat_loss_foods = food_df[
    (food_df['Calories (kcal)'] < 300)
]

# bulking foods separated
bulk_foods = food_df[
    (food_df['Calories (kcal)'] > 400)
]

#maintenance foods separated
maintenance_foods = food_df[
    (food_df['Calories (kcal)'] >= 250) &
    (food_df['Calories (kcal)'] <= 400)
]

# function to recommend diet based on goal

def recommend_diet(goal):

    if goal == "Fat Loss":
        foods = fat_loss_foods

    elif goal == "Bulk":
        foods = bulk_foods

    else:
        foods = maintenance_foods

    return foods

# Breakfast food recommendations
breakfast = food_df[
    food_df['Meal_Type'] == 'Breakfast'
].head(3)

# Lunch food recommendations
lunch = food_df[
    food_df['Meal_Type'] == 'Lunch'
].head(3)

# Dinner food recommendations
dinner = food_df[
    food_df['Meal_Type'] == 'Dinner'
].head(3)