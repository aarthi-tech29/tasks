# 5.Loan EMI Calculator: Calculate the Equated Monthly Installment using the principal, rate, and time (involves exponentiation).

# Loan EMI Calculator

print("----- Loan EMI Calculator -----")

# Inputs
principal = float(input("Enter loan amount (P): "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan duration in years: "))

# Calculations
monthly_rate = annual_rate / (12 * 100)   # Convert annual % rate to monthly decimal
months = years * 12

# EMI formula
emi = (principal * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)

print("\n----- RESULT -----")
print(f"Monthly EMI: ₹{emi:.2f}")
