# 15.E-commerce Discount Applier: Check if the cart total is > $100 to apply a 10% discount.

# E-commerce Discount Applier

print("----- E-commerce Discount Applier -----")

# Input
cart_total = float(input("Enter your cart total: Rs."))

# Check and apply discount
if cart_total > 100:
    discount = cart_total * 0.10
    final_total = cart_total - discount
    print(f"Congratulations! You get a 10% discount of Rs.{discount:.2f}")
else:
    final_total = cart_total
    print("No discount applied.")

# Output final amount
print(f"Final amount to pay: Rs.{final_total:.2f}")
