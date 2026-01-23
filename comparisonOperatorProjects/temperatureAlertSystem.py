# 18.Temperature Alert System: Check if the current temperature is < 0 (freezing alert) or > 40 (heat alert).

# Temperature Alert System

print("----- Temperature Alert System -----")

# Input
temperature = float(input("Enter the current temperature (°C): "))

# Check temperature conditions
if temperature < 0:
    print("Freezing Alert! Stay warm!")
elif temperature > 40:
    print("Heat Alert! Stay hydrated!")
else:
    print("Temperature is normal.")
