# 7.Split-a-Bill App: Calculate how much each person owes, including tip and tax, by dividing the total.

# Split-a-Bill App

print("----- Split-a-Bill App -----")

# Inputs
total_amount = float(input("Enter the total bill amount: ₹"))
num_people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage (%): "))
tax_percent = float(input("Enter tax percentage (%): "))

# Calculations
tip_amount = total_amount * (tip_percent / 100)
tax_amount = total_amount * (tax_percent / 100)
final_total = total_amount + tip_amount + tax_amount

amount_per_person = final_total / num_people

# Output
print("\n----- BILL SUMMARY -----")
print(f"Original Bill: ₹{total_amount:.2f}")
print(f"Tip ({tip_percent}%): ₹{tip_amount:.2f}")
print(f"Tax ({tax_percent}%): ₹{tax_amount:.2f}")
print(f"Total Amount: ₹{final_total:.2f}")
print(f"Each Person Owes: ₹{amount_per_person:.2f}")
