students = [
    ("Anton", [5, 4, 5, 3]),
    ("Misha", [3, 3, 4, 2]),
    ("Dima", [5, 5, 5, 5]),
    ("Oleg", [2, 3, 2, 4]),
]
student_loosers = {}
slownik = {}
for student in students:
    name, grades = student
    average = sum(grades) / len(grades)
    slownik[name] = average
print(slownik)
max_average=max(slownik.values())

for name, average in slownik.items():
    if average == max_average:
        print(f"Student with the highest average grade: {name} with an average of {average}")
    if average < 4:
        student_loosers[name] = average
print(f"Students with an average grade below 4: {student_loosers}")

sorted_student = sorted(slownik.items(),reverse=True)
print(f"Students sorted by name: {sorted_student}")