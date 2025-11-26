# 14.Leap Year Checker: Determine if a year is a leap year using conditions with modulo (%) and equality (==) operators.

# Leap Year Checker

print("----- Leap Year Checker -----")

# Input
year = int(input("Enter a year: "))

# Check leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

