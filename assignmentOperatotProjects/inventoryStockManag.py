# 25.Inventory Stock Management: Use -= to decrease stock when an item is sold and += to increase it during restocking.

# Inventory Stock Management

print("----- Inventory Stock Management -----")

# Initialize stock
inventory = {}

while True:
    print("\nCurrent Inventory:", inventory)
    print("1. Add stock (Restock)")
    print("2. Sell item")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == '1':
        item = input("Enter item name to restock: ")
        qty = int(input("Enter quantity to add: "))
        if item in inventory:
            inventory[item] += qty
        else:
            inventory[item] = qty
        print(f"{qty} {item}(s) added to inventory.")
        
    elif choice == '2':
        item = input("Enter item name to sell: ")
        if item in inventory:
            qty = int(input("Enter quantity to sell: "))
            if qty <= inventory[item]:
                inventory[item] -= qty
                print(f"{qty} {item}(s) sold.")
                if inventory[item] == 0:
                    del inventory[item]  # remove item if stock is 0
            else:
                print(f"Not enough {item} in stock")
        else:
            print(f"{item} not found in inventory")
            
    elif choice == '3':
        print("Exiting Inventory Management...")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

print("\nFinal Inventory:", inventory)
