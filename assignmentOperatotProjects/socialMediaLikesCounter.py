# 30.Social Media "Likes" Counter: A simple counter that uses ++ for each new like on a post.

# Social Media Likes Counter

print("----- Social Media Likes Counter -----")

# Initialize likes
likes = 0

while True:
    action = input("\nNew like? (yes/no): ").lower()
    
    if action == "yes":
        likes += 1  # increment by 1
        print(f"Like added! Total Likes: {likes}")
    elif action == "no":
        print("Exiting Likes Counter...")
        break
    else:
        print("Please enter 'yes' or 'no'.")

print(f"\nFinal Likes Count: {likes}")
