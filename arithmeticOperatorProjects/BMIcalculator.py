# 3.BMI Calculator: Take weight and height as input, use division and multiplication to compute the Body Mass Index.

# BMI Calculator

print("----- BMI Calculator -----")

# Input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# BMI formula: weight / (height * height)
bmi = weight / (height * height)

print("\n----- RESULT -----")
print(f"Your BMI is: {bmi:.2f}")

# BMI Category (optional)
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 24.9:
    print("Category: Normal weight")
elif bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obesity")
