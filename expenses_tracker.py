#  Expense Tracker(Daily + Weekly + Monthly)
import pandas as pd
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        # Initialize empty DataFrame
        self.data = pd.DataFrame(columns=["date", "amount", "category", "note"])

    def add_expense(self, date_str, amount, category, note=""):
        """Add a new expense"""
        date_value = pd.to_datetime(date_str, errors="coerce")
        if pd.isna(date_value):
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        new_row = {
            "date": date_value,
            "amount": float(amount),
            "category": category,
            "note": note
        }

        # Add row directly without using concat
        self.data.loc[len(self.data)] = new_row

    def daily_total(self, date_str):
        """Return total spent on a particular day"""
        date_value = pd.to_datetime(date_str, errors="coerce")
        if pd.isna(date_value):
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        df = self.data[self.data["date"].dt.date == date_value.date()]
        return df["amount"].sum()

    def weekly_total(self, year, week_number):
        """Return total expense for a given week"""
        self.data["year"] = self.data["date"].dt.isocalendar().year
        self.data["week"] = self.data["date"].dt.isocalendar().week
        df = self.data[(self.data["year"] == year) & (self.data["week"] == week_number)]
        return df["amount"].sum()

    def monthly_total(self, year, month):
        """Return total expenses for a given month"""
        df = self.data[(self.data["date"].dt.year == year) & (self.data["date"].dt.month == month)]
        return df["amount"].sum()

    def show_all(self):
        """Return all expenses"""
        return self.data

# -------------------------
# Example usage
# -------------------------

tracker = ExpenseTracker()

tracker.add_expense("2025-12-01", 120, "Food", "Snacks")
tracker.add_expense("2025-12-01", 300, "Grocery")
tracker.add_expense("2025-12-02", 150, "Travel")
tracker.add_expense("2025-12-05", 500, "Shopping")
tracker.add_expense("2025-12-10", 200, "Food")
tracker.add_expense("2025-12-10", 200, "Food")
tracker.add_expense("2025-11-28", 100, "Travel", "Bus Fare")
tracker.add_expense("2025-11-20", 900, "Rent", "House Rent")
tracker.add_expense("2025-11-20", 200, "Food", "Grocery")


print("Daily Total (2025-12-01):", tracker.daily_total("2025-12-01"))
print("Weekly Total (2025, Week 49):", tracker.weekly_total(2025, 49))
print("Monthly Total (Dec 2025):", tracker.monthly_total(2025, 12))

print("\nAll Expenses:")
print(tracker.show_all())

# ---------------------------------------------------------------------------------
# Adding the date, amount, category, note in terminal
# ----------------------------------------------------------------------------------
import pandas as pd
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        # Initialize empty DataFrame
        self.data = pd.DataFrame(columns=["date", "amount", "category", "note"])

    def add_expense(self, date_value, amount, category, note=""):
        """Add a new expense"""
        new_row = {
            "date": date_value,
            "amount": amount,
            "category": category,
            "note": note
        }
        self.data.loc[len(self.data)] = new_row

    def daily_total(self, date_value):
        df = self.data[self.data["date"].dt.date == date_value.date()]
        return df["amount"].sum()

    def weekly_total(self, year, week_number):
        self.data["year"] = self.data["date"].dt.isocalendar().year
        self.data["week"] = self.data["date"].dt.isocalendar().week
        df = self.data[(self.data["year"] == year) & (self.data["week"] == week_number)]
        return df["amount"].sum()

    def monthly_total(self, year, month):
        df = self.data[(self.data["date"].dt.year == year) & (self.data["date"].dt.month == month)]
        return df["amount"].sum()

    def show_all(self):
        return self.data

    def input_expense(self):
        """Ask user for expense details with validation"""
        # Date validation
        while True:
            date_str = input("Enter date (YYYY-MM-DD): ")
            try:
                date_value = pd.to_datetime(date_str, errors="raise")
                break
            except Exception:
                print("Invalid date format. Please enter YYYY-MM-DD.")

        # Amount validation (integer)
        while True:
            amount_str = input("Enter amount (integer): ")
            if amount_str.isdigit():
                amount = int(amount_str)
                break
            else:
                print("Amount must be an integer. Try again.")

        # Category validation (alphabetic only)
        while True:
            category = input("Enter category (alphabetic only): ").strip()
            if category.isalpha():
                break
            else:
                print("Category must contain alphabetic only. Try again.")

        # Note validation (alphabetic only, optional)
        while True:
            note = input("Enter note (optional, alphabetic only): ").strip()
            if note == "" or note.isalpha():
                break
            else:
                print("Note must contain alphabetic only. Try again.")

        # Add the expense
        self.add_expense(date_value, amount, category, note)
        print("Expense added successfully!\n")


# -------------------------
# Example usage
# -------------------------

tracker = ExpenseTracker()

# Input multiple expenses
while True:
    tracker.input_expense()
    cont = input("Do you want to add another expense? (yes/no): ").strip().lower()
    if cont != "yes":
        break

# Show all expenses
print("\nAll Expenses:")
print(tracker.show_all())

# Validate daily total
while True:
    date_check = input("\nCheck daily total for date (YYYY-MM-DD): ")
    try:
        date_value = pd.to_datetime(date_check, errors="raise")
        print("Daily Total:", tracker.daily_total(date_value))
        break
    except:
        print("Invalid date format. Try again.")

# Validate weekly total
while True:
    try:
        year = int(input("\nEnter year for weekly/monthly totals (YYYY): "))
        week = int(input("Enter week number (1-53) to check weekly total: "))
        if 1 <= week <= 53:
            break
        else:
            print("Week number must be between 1 and 53. Try again.")
    except ValueError:
        print("Enter valid integers for year and week.")

# Validate monthly total
while True:
    try:
        month = int(input("Enter month number (1-12) to check monthly total: "))
        if 1 <= month <= 12:
            break
        else:
            print("Month number must be between 1 and 12. Try again.")
    except ValueError:
        print("Enter a valid integer for month.")

print("Weekly Total:", tracker.weekly_total(year, week))
print("Monthly Total:", tracker.monthly_total(year, month))
