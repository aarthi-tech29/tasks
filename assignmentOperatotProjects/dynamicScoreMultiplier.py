# 29.Dynamic Score Multiplier: In a game, use *= to double the points for a limited time during a "power-up."

# Dynamic Score Multiplier

import time

print("----- Dynamic Score Multiplier -----")

# Initial score
score = 50
print(f"Current Score: {score}")

# Simulate normal points gain
points_earned = 10
score += points_earned
print(f"Points earned: {points_earned} -> New Score: {score}")

# Activate power-up
print("\nPower-Up Activated! Points will double for next 3 actions")

for i in range(3):
    points_earned = 10
    points_earned *= 2  # double the points during power-up
    score += points_earned
    print(f"Power-Up Points earned: {points_earned} -> Score: {score}")
    time.sleep(0.5)

print("\nPower-Up ended! Final Score:", score)
