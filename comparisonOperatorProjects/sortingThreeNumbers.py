# 20.Sorting Three Numbers: Use a series of comparisons to sort three numbers in ascending or descending order.

# Sorting Three Numbers

print("----- Sorting Three Numbers -----")

# Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Ask for order
order = input("Sort in ascending or descending order? (asc/desc): ").lower()

# Sorting using comparisons
if order == "asc":
    if num1 <= num2 and num1 <= num3:
        if num2 <= num3:
            sorted_nums = [num1, num2, num3]
        else:
            sorted_nums = [num1, num3, num2]
    elif num2 <= num1 and num2 <= num3:
        if num1 <= num3:
            sorted_nums = [num2, num1, num3]
        else:
            sorted_nums = [num2, num3, num1]
    else:
        if num1 <= num2:
            sorted_nums = [num3, num1, num2]
        else:
            sorted_nums = [num3, num2, num1]
elif order == "desc":
    if num1 >= num2 and num1 >= num3:
        if num2 >= num3:
            sorted_nums = [num1, num2, num3]
        else:
            sorted_nums = [num1, num3, num2]
    elif num2 >= num1 and num2 >= num3:
        if num1 >= num3:
            sorted_nums = [num2, num1, num3]
        else:
            sorted_nums = [num2, num3, num1]
    else:
        if num1 >= num2:
            sorted_nums = [num3, num1, num2]
        else:
            sorted_nums = [num3, num2, num1]
else:
    print("Invalid choice!")
    sorted_nums = []

# Output
if sorted_nums:
    print(f"Sorted numbers: {sorted_nums}")
