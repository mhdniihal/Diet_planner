import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


df = pd.read_csv("data/cleaned/calorie_cleaned.csv")
print(df.head())

print(df.columns)

'''X = df[
    [
        'Age',
        'Weight_kg',
        'Height_cm',
        'BMI'
    ]
]'''

encoder = LabelEncoder()

df['Gender'] = encoder.fit_transform(df['Gender'])

df['Physical_Activity_Level'] = encoder.fit_transform(
    df['Physical_Activity_Level']
)

X = df[
    [
        'Age',
        'Gender',
        'Weight_kg',
        'Height_cm',
        'BMI',
        'Physical_Activity_Level'
    ]
]

y = df['Daily_Caloric_Intake']


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)



mae = mean_absolute_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)

print("MAE:", mae)
print("R2 Score:", r2)