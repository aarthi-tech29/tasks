# 13.Maximum & Minimum Finder: Take three numbers as input and find the largest and smallest among them.

# Maximum & Minimum Finder

print("----- Maximum & Minimum Finder -----")

# Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find maximum
maximum = max(num1, num2, num3)

# Find minimum
minimum = min(num1, num2, num3)

# Output
print(f"The largest number is: {maximum}")
print(f"The smallest number is: {minimum}")
