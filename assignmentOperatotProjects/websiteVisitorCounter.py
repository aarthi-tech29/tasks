# 24.Website Visitor Counter: A simple counter that uses ++ to increment the count for each new visitor.

# Website Visitor Counter

print("----- Website Visitor Counter -----")

# Initialize visitor count
visitor_count = 0

while True:
    action = input("\nNew visitor? (yes/no): ").lower()
    
    if action == "yes":
        visitor_count += 1  # increment by 1
        print(f"Visitor added! Total visitors: {visitor_count}")
    elif action == "no":
        print("Exiting Visitor Counter...")
        break
    else:
        print("Please enter 'yes' or 'no'.")

print(f"\nTotal Visitors: {visitor_count}")
