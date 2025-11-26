# 36.Weather-Based Activity Suggestion: Suggest "Go for a walk" if it is NOT (!) raining AND (&&) the temperature is pleasant.

# Weather-Based Activity Suggestion

print("----- Weather-Based Activity Suggestion -----")

# Input
is_raining = input("Is it raining? (yes/no): ").lower()
temperature = float(input("Enter current temperature (°C): "))

# Define pleasant temperature range
pleasant_min = 20
pleasant_max = 30

# Suggest activity
if is_raining != "yes" and pleasant_min <= temperature <= pleasant_max:
    print("Go for a walk!")
else:
    print("Better to stay indoors")
