# Input age and salary
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary (₹): "))

# Check eligibility
if age < 21 or age > 60:
    print("Not eligible for loan due to age criteria")
elif salary >= 50000:
    print("Eligible for High Loan")
elif salary >= 30000:
    print("Eligible for Medium Loan")
else:
    print("Eligible for Low Loan")