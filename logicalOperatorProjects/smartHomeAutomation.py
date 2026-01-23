# 34.Smart Home Automation: Turn on the lights only if it is night-time (e.g., after 7 PM) AND (&&) motion is detected.

# Smart Home Automation

print("----- Smart Home Automation -----")

# Input
current_hour = int(input("Enter the current hour (0-23): "))
motion_detected = input("Is motion detected? (yes/no): ").lower()

# Check if lights should turn on
if current_hour >= 19 and motion_detected == "yes":
    print("Lights turned ON")
else:
    print("Lights remain OFF")
