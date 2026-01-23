# 10.Fuel Efficiency Calculator: Calculate miles per gallon (or km per liter) using division (distance / fuel used).

# Fuel Efficiency Calculator

print("----- Fuel Efficiency Calculator -----")

# Input
distance = float(input("Enter distance traveled: "))
fuel_used = float(input("Enter fuel used: "))

# Choose unit
unit = input("Enter unit system (mpg/kmpl): ").lower()

if unit == "mpg":
    efficiency = distance / fuel_used
    print(f"\nFuel Efficiency: {efficiency:.2f} miles per gallon (mpg)")
    
elif unit == "kmpl":
    efficiency = distance / fuel_used
    print(f"\nFuel Efficiency: {efficiency:.2f} km per liter (kmpl)")
    
else:
    print("Invalid unit! Please enter 'mpg' or 'kmpl'.")
