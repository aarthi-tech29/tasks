# 26.Budget Tracker: Start with a monthly budget and use -= to subtract each expense, updating the remaining balance.

# Budget Tracker

print("----- Budget Tracker -----")

# Input monthly budget
budget = float(input("Enter your monthly budget: ₹"))
remaining = budget

while True:
    print(f"\nRemaining Budget: ₹{remaining:.2f}")
    print("1. Add an expense")
    print("2. Exit")
    
    choice = input("Choose an option (1-2): ")
    
    if choice == '1':
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: ₹"))
        if expense_amount <= remaining:
            remaining -= expense_amount
            print(f"{expense_name} expense of ₹{expense_amount:.2f} recorded")
        else:
            print("Expense exceeds remaining budget")
    elif choice == '2':
        print("Exiting Budget Tracker...")
        break
    else:
        print("Invalid choice! Please select 1 or 2.")

print(f"\nFinal Remaining Budget: ₹{remaining:.2f}")
