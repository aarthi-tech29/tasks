# 23.Loyalty Points Tracker: A system that uses += to add points for each purchase and -= to deduct points when redeemed.

# Loyalty Points Tracker

print("----- Loyalty Points Tracker -----")

# Initialize points
points = 0

while True:
    print(f"\nCurrent Points: {points}")
    print("1. Add points for purchase")
    print("2. Redeem points")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == '1':
        earned = int(input("Enter points earned from purchase: "))
        points += earned
        print(f"{earned} points added!")
        
    elif choice == '2':
        redeem = int(input("Enter points to redeem: "))
        if redeem <= points:
            points -= redeem
            print(f"{redeem} points redeemed!")
        else:
            print("Not enough points to redeem")
            
    elif choice == '3':
        print("Exiting Loyalty Points Tracker...")
        break
        
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

print(f"\nFinal Points Balance: {points}")

