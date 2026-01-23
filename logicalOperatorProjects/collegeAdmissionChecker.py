# 32.College Admission Checker: Check if marks are >= a minimum AND (&&) the applicant has no backlogs.

# College Admission Checker

print("----- College Admission Checker -----")

# Minimum marks required
min_marks = 60

# Input
marks = float(input("Enter your marks (%): "))
backlogs = int(input("Enter number of backlogs: "))

# Check eligibility
if marks >= min_marks and backlogs == 0:
    print("Congratulations! You are eligible for admission")
else:
    print("Sorry, you are not eligible for admission")
