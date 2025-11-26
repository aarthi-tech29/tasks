# 27."Double or Nothing" Game Simulator: A betting game where the player's balance is multiplied by 2 (*= 2) on a win or set to 0 on a loss.

# Double or Nothing Game Simulator

import random

print("----- Double or Nothing Game Simulator -----")

# Initialize balance
balance = float(input("Enter your starting balance: ₹"))

while True:
    print(f"\nCurrent Balance: ₹{balance:.2f}")
    choice = input("Do you want to play 'Double or Nothing'? (yes/no): ").lower()
    
    if choice == 'yes':
        # Simulate win or loss (50% chance)
        result = random.choice(["win", "lose"])
        
        if result == "win":
            balance *= 2
            print("You won! Your balance is doubled!")
        else:
            balance = 0
            print("You lost! Your balance is now 0.")
            break  # Game over on loss
    elif choice == 'no':
        print("Exiting game...")
        break
    else:
        print("Please enter 'yes' or 'no'.")

print(f"\nFinal Balance: ₹{balance:.2f}")
