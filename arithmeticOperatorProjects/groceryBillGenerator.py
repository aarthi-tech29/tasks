# 2.Grocery Bill Generator: Calculate the total cost, apply tax, and give the final amount based on item prices and quantities.

# Grocery Bill Generator

print("----- Grocery Bill Generator -----")

items = {}
num_items = int(input("Enter number of different items: "))

for i in range(num_items):
    print(f"\nItem {i+1}:")
    name = input("Enter item name: ")
    price = float(input("Enter price of one unit: "))
    qty = int(input("Enter quantity: "))
    
    items[name] = price * qty  # total for that item
    print(items)

# Calculate total
subtotal = sum(items.values())
tax_rate = 0.05   # 5% GST (you can change)

tax_amount = subtotal * tax_rate
final_amount = subtotal + tax_amount

print("\n--------- BILL ---------")
for item, total in items.items():
    print(f"{item}: ₹{total:.2f}")

print("------------------------")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Tax (5%): ₹{tax_amount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")
print("------------------------")
