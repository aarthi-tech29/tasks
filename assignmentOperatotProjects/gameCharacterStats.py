# 22.Game Character Stats: Use += to increase health when a potion is used and -= when the character takes damage.

# Game Character Stats Manager

print("----- Game Character Stats -----")

# Initialize character health
health = 100

while True:
    print(f"\nCurrent Health: {health}")
    print("1. Use Health Potion (+20)")
    print("2. Take Damage (-15)")
    print("3. Exit")
    
    choice = input("Choose an action (1-3): ")
    
    if choice == '1':
        health += 20
        if health > 100:
            health = 100  # max health limit
        print("Potion used! Health increased.")
        
    elif choice == '2':
        health -= 15
        if health < 0:
            health = 0  # min health limit
        print("Took damage! Health decreased.")
        
    elif choice == '3':
        print("Exiting Game Character Stats...")
        break
        
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

print(f"\nFinal Health: {health}")
