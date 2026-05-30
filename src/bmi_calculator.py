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
    
weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (cm): "))

bmi = calculate_bmi(weight, height)

category = bmi_category(bmi)

print(f"\nBMI: {bmi}")
print(f"Category: {category}")

goal = input("Enter Goal (Bulk/Cut/Fat Loss): ")

# recommendation based on goal
def recommendation(category, goal):

    if goal == "Bulk":
        return "Increase calorie intake and protein."

    elif goal == "Cut":
        return "Maintain high protein and reduce calories."

    elif goal == "Fat Loss":
        return "Create calorie deficit and increase activity."

    return "Maintain healthy lifestyle."

print(f"Recommendation: {recommendation(category, goal)}")