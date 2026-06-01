import pandas as pd

food_df = pd.read_csv("data/cleaned/food_cleaned.csv")
print(food_df.head())
print(food_df.columns)


# fat loss foods separated
fat_loss_foods = food_df[
    (food_df['Calories'] < 300)
]

# bulking foods separated
bulk_foods = food_df[
    (food_df['Calories'] > 400)
]

#maintenance foods separated
maintenance_foods = food_df[
    (food_df['Calories'] >= 250) &
    (food_df['Calories'] <= 400)
]