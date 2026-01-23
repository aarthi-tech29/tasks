# 37.Loan Approval System: Approve a loan if the income is high AND (&&) the credit score is good OR (||) a guarantor is available.

# Loan Approval System

print("----- Loan Approval System -----")

# Input
income = float(input("Enter your monthly income (₹): "))
credit_score = int(input("Enter your credit score (0-850): "))
guarantor = input("Do you have a guarantor? (yes/no): ").lower()

# Define thresholds
high_income = 50000
good_credit_score = 700

# Check loan approval
if (income >= high_income and credit_score >= good_credit_score) or guarantor == "yes":
    print("Loan Approved!")
else:
    print("Loan Denied")
