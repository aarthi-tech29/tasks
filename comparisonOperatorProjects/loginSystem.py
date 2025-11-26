# 16.Login System: Check if the entered username and password are exactly equal (==) to the stored ones.

# Simple Login System

print("----- Login System -----")

# Stored credentials
stored_username = "admin"
stored_password = "password123"

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Check login
if username == stored_username and password == stored_password:
    print("Login successful")
else:
    print("Invalid username or password")
