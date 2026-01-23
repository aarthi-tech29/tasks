# 38.Access Control System: Grant admin access if the user role is "admin" AND (&&) their account is active (e.g., !isSuspended).

# Access Control System

print("----- Access Control System -----")

# Input
role = input("Enter user role: ").lower()
is_suspended = input("Is the account suspended? (yes/no): ").lower()

# Check admin access
if role == "admin" and is_suspended != "yes":
    print("Admin access granted!")
else:
    print("Access denied")
