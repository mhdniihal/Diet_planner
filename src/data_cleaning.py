import pandas as pd

health_df = pd.read_csv(r"C:\Documents\Projects\Diet_planner\data\Health & BMI Dataset.csv")

food_df = pd.read_csv(r"C:\Documents\Projects\Diet_planner\data\Food Nutrition Dataset.csv")

calorie_df = pd.read_csv(r"C:\Documents\Projects\Diet_planner\data\Calorie Requirement Dataset.csv")

print(health_df.info())
print(food_df.info())
print(calorie_df.info())

print(health_df.head())
print(food_df.head())
print(calorie_df.head())

health_df = health_df.loc[:, ~health_df.columns.str.contains('^Unnamed')]
food_df = food_df.loc[:, ~food_df.columns.str.contains('^Unnamed')]
calorie_df = calorie_df.loc[:, ~calorie_df.columns.str.contains('^Unnamed')]

print(health_df.isnull().sum())
print(food_df.isnull().sum())
print(calorie_df.isnull().sum())

health_df.fillna(
    health_df.select_dtypes(include='number').mean(),
    inplace=True
)

health_df.fillna("Unknown", inplace=True)

health_df.drop_duplicates(inplace=True)
food_df.drop_duplicates(inplace=True)
calorie_df.drop_duplicates(inplace=True)

health_df["Gender"] = health_df["Gender"].str.capitalize()
health_df["Goal"] = health_df["Goal"].str.title()

print(health_df.shape)
print(food_df.shape)
print(calorie_df.shape)

health_df.to_csv(
    "data/cleaned/health_cleaned.csv",
    index=False
)

food_df.to_csv(
    "data/cleaned/food_cleaned.csv",
    index=False
)

calorie_df.to_csv(
    "data/cleaned/calorie_cleaned.csv",
    index=False
)
