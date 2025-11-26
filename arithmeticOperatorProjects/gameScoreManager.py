# 6.Game Score Manager: A program to add points for achievements and subtract for penalties in a game.

# Game Score Manager

print("----- Game Score Manager -----")

score = 0  # initial score

while True:
    print("\nCurrent Score:", score)
    print("1. Add points (Achievement)")
    print("2. Subtract points (Penalty)")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == '1':
        points = int(input("Enter points to add: "))
        score += points
        print(f"{points} points added!")
        
    elif choice == '2':
        points = int(input("Enter points to subtract: "))
        score -= points
        print(f"{points} points subtracted!")
        
    elif choice == '3':
        print("Exiting the Game Score Manager...")
        break
        
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

print("\nFinal Score:", score)
