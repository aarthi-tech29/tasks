# 39.E-commerce Shipping: Offer free shipping if the cart total is > $50 OR (||) the user is a premium member.

# E-commerce Shipping Checker

print("----- E-commerce Shipping Checker -----")

# Input
cart_total = float(input("Enter your cart total ($): "))
is_premium = input("Are you a premium member? (yes/no): ").lower()

# Check free shipping eligibility
if cart_total > 50 or is_premium == "yes":
    print("You are eligible for FREE shipping")
else:
    print("Standard shipping charges apply")
