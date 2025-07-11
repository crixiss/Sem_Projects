students = {
    'Alice': [85, 90, 88],
    'Bob': [78, 82, 80],
    'Carol': [95, 92, 98]
}

def average_marks():
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        print(f"{name}: {avg:.2f}")

def find_topper():
    topper = max(students, key=lambda name: sum(students[name])/3)
    print("Topper:", topper)

def update_marks(name, new_marks):
    if name in students:
        students[name] = new_marks
    else:
        print("Student not found.")

average_marks()
find_topper()
update_marks("Bob", [88, 90, 92])
