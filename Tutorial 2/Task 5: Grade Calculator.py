# Grade Calculator
print("Grade Calculator")
marks = []
for i in range(1, 5 + 1):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your average mark is: {average:.2f}")
print(f"Your grade is: {grade}")
