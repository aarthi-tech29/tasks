# 8.Percentage & Grade Calculator: Find the percentage from marks obtained and total marks, then assign a grade.

# Percentage & Grade Calculator

print("----- Percentage & Grade Calculator -----")

# Inputs
marks_obtained = float(input("Enter marks obtained: "))
total_marks = float(input("Enter total marks: "))

# Percentage calculation
percentage = (marks_obtained / total_marks) * 100

# Grade assignment
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B+'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
else:
    grade = 'F'

# Output
print("\n----- RESULT -----")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
