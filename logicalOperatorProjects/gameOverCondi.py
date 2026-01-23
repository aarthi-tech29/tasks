# 40.Game Over Condition: The game is over if the player's health is <= 0 OR (||) the timer has reached zero.

# Game Over Condition

print("----- Game Over Checker -----")

# Input
health = int(input("Enter player's health: "))
timer = int(input("Enter remaining time (seconds): "))

# Check game over condition
if health <= 0 or timer <= 0:
    print("Game Over!")
else:
    print("Keep playing!")
