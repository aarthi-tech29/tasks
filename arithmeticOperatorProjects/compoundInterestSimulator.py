# 9.Compound Interest Simulator: Calculate the future value of an investment using the compound interest formula.

# Compound Interest Simulator

print("----- Compound Interest Simulator -----")

# Inputs
principal = float(input("Enter the principal amount: ₹"))
rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter number of years: "))

# Compound Interest Calculation
future_value = principal * (1 + rate/100)**years

# Output
print("\n----- RESULT -----")
print(f"Future Value after {years} years: ₹{future_value:.2f}")
