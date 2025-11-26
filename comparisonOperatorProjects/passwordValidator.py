# 12.Password Validator: Check if a newly created password's length is >= a minimum requirement (e.g., 8 characters).

# Password Validator

print("----- Password Validator -----")

# Minimum password length
min_length = 8

# Input
password = input("Enter your new password: ")

# Check password length
if len(password) >= min_length:
    print("Password is valid")
else:
    print(f"Password is too short! Must be at least {min_length} characters")
