# 21.Shopping Cart Quantity Manager: Use += to add an item to the cart and -= to remove it.

# Shopping Cart Quantity Manager

print("----- Shopping Cart Quantity Manager -----")

# Initialize cart
cart = {}

while True:
    print("\nCurrent Cart:", cart)
    print("1. Add item")
    print("2. Remove item")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == '1':
        item = input("Enter item name to add: ")
        if not item.isalpha():
            print("Invalid item name! Please enter correctly")
            continue
        qty = int(input("Enter quantity to add: "))
        if item in cart:
            cart[item] += qty  # add quantity
        else:
            cart[item] = qty
        print(f"{qty} {item}(s) added to the cart.")
        
    elif choice == '2':
        item = input("Enter item name to remove: ")
        if item in cart:
            qty = int(input("Enter quantity to remove: "))
            cart[item] -= qty  # remove quantity
            if cart[item] <= 0:
                del cart[item]  # remove item if quantity <= 0
            print(f"{qty} {item}(s) removed from the cart.")
        else:
            print(f"{item} is not in the cart.")
            
    elif choice == '3':
        print("Exiting Shopping Cart Manager...")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

print("\nFinal Cart:", cart)
