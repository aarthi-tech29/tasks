# 4.Unit Converter: Convert between units (e.g., kilometers to miles, Celsius to Fahrenheit) using multiplication/division.

# Unit Converter Program

print("----- Unit Converter -----")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = int(input("Choose a conversion (1-4): "))

if choice == 1:
    km = float(input("Enter kilometers: "))
    miles = km * 0.621371
    print(f"{km} km = {miles:.3f} miles")

elif choice == 2:
    miles = float(input("Enter miles: "))
    km = miles / 0.621371
    print(f"{miles} miles = {km:.3f} km")

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f:.2f}°F")

elif choice == 4:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c:.2f}°C")

else:
    print("Invalid choice!")
