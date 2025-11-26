# 19.Drive License Issuer: A system that checks if a person's age is >= 16 for a learner's permit and >= 18 for a full license.

# Drive License Issuer

print("----- Drive License Issuer -----")

# Input
age = int(input("Enter your age: "))

# Check license eligibility
if age >= 18:
    print("You are eligible for a full driving license")
elif age >= 16:
    print("You are eligible for a learner's permit")
else:
    print("You are not eligible for any driving license")
