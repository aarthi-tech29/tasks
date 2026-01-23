import pandas as pd

# Load existing student data
df = pd.read_csv("student_data.csv")

# Function to check eligibility
def check_eligibility(row):
    if (row['Attendance'] >= 80 and
        row['Tasks'] >= 80 and
        row['Mini_Project'] >= 80 and
        row['Main_Project'] >= 80):
        return "Eligible"
    else:
        return "Not Eligible"

# Apply eligibility check
df['Status'] = df.apply(check_eligibility, axis=1)

print("\nExisting Student Eligibility")
print(df)

# ---- ADD NEW STUDENT DATA ----
print("\nAdd New Student")

name = input("Name: ")
attendance = float(input("Attendance %: "))
tasks = float(input("Tasks %: "))
mini = float(input("Mini Project %: "))
main = float(input("Main Project %: "))

new_student = {
    "Name": name,
    "Attendance": attendance,
    "Tasks": tasks,
    "Mini_Project": mini,
    "Main_Project": main
}

# Append new student
df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)

# Recalculate eligibility
df['Status'] = df.apply(check_eligibility, axis=1)

# Save back to CSV
df.to_csv("student_data.csv", index=False)

print("\nUpdated Student Data")
print(df)
