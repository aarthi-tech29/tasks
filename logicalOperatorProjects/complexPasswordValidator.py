# 35.Complex Password Validator: Check if password length is >= 8 AND (&&) it contains at least one digit AND (&&) one special character.

# Complex Password Validator

import re # regular Expression

print("----- Complex Password Validator -----")

# Input
password = input("Enter your password: ")

# Check conditions
has_length = len(password) >= 8
has_digit = bool(re.search(r"\d", password))
has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

# Validate password
if has_length and has_digit and has_special:
    print("Password is strong!")
else:
    print("Password is weak. It must be at least 8 characters long, contain a digit and a special character.")
