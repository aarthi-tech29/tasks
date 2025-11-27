# 31.Advanced Login System: Check if the username is correct AND (&&) the password is correct.

# Advanced Login System

print("----- Advanced Login System -----")

# Stored credentials
stored_username = "aarthi"
stored_password = "secure123"

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Check login
if username == stored_username and password == stored_password:
    print("Login successful")
else:
    print("Invalid username or password")
