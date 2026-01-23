# 17.Game Level Unlocker: Check if a player's score is >= the required score to unlock the next level.

# Game Level Unlocker

print("----- Game Level Unlocker -----")

# Required score to unlock next level
required_score = 100

# Player's score input
score = int(input("Enter your current score: "))

# Check if player can unlock the next level
if score >= required_score:
    print("Congratulations! You unlocked the next level")
else:
    print(f"Keep playing! You need {required_score - score} more points to unlock the next level")
