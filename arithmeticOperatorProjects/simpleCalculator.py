# 1.Simple Calculator: A program that takes two numbers and an operator (+, -, *, /, %) to perform basic arithmetic.

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation"


print(f"Result: {result}")