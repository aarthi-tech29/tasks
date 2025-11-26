# 33.Special Discount Eligibility: Offer a special discount if the user is a senior citizen (age >= 65) OR (||) a student.

# Special Discount Eligibility

print("----- Special Discount Eligibility Checker -----")

# Input
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower()

# Check discount eligibility
if age >= 65 or is_student == "yes":
    print("You are eligible for a special discount")
else:
    print("Sorry, you are not eligible for a special discount")
