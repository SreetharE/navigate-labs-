n = int(input("Enter number of students: "))

students = {}

for i in range(n):
    name = input("Enter student name: ")
    modules = input("Enter modules completed (space separated): ").split()
    students[name] = modules

print("\nModules completed by each student:")
for student in students:
    print(student, "completed", len(students[student]), "modules")

max_modules = 0
top_student = ""

for student in students:
    count = len(students[student])
    if count > max_modules:
        max_modules = count
        top_student = student

print("\nStudent with maximum modules:")
print(top_student, "completed", max_modules, "modules")
