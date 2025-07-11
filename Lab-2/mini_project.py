
students = []

def add_student():
    print("\n--- Add Student ---")
    name = input("Enter student's name: ")
    roll = input("Enter roll number: ")

    num_subjects = int(input("Enter number of subjects: "))
    marks = {}

    for _ in range(num_subjects):
        subject = input("Enter subject name: ")
        score = int(input(f"Enter marks for {subject}: "))
        marks[subject] = score

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def view_all_students():
    print("\n--- All Students Report ---")
    if not students:
        print("No students to show.\n")
        return

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Roll Number: {student['roll']}")
        for subject, score in student['marks'].items():
            print(f"{subject}: {score}")
        avg = sum(student['marks'].values()) / len(student['marks'])
        print(f"Average Marks: {avg:.2f}")
        print("-----------------------------")


def find_topper():
    print("\n--- Topper(s) ---")
    if not students:
        print("No records found.\n")
        return

    highest_avg = 0
    toppers = []

    for student in students:
        avg = sum(student['marks'].values()) / len(student['marks'])
        if avg > highest_avg:
            highest_avg = avg
            toppers = [student]
        elif avg == highest_avg:
            toppers.append(student)

    for student in toppers:
        print(f"Name: {student['name']}, Roll: {student['roll']}, Avg: {highest_avg:.2f}")
    print()


def search_by_roll():
    print("\n--- Search Student by Roll ---")
    roll = input("Enter roll number: ")
    found = False

    for student in students:
        if student['roll'] == roll:
            print(f"Name: {student['name']}")
            print(f"Roll Number: {student['roll']}")
            for subject, score in student['marks'].items():
                print(f"{subject}: {score}")
            avg = sum(student['marks'].values()) / len(student['marks'])
            print(f"Average Marks: {avg:.2f}")
            found = True
            break

    if not found:
        print("Student not found.\n")


def show_failed_students():
    print("\n--- Failed Students ---")
    failed_any = False

    for student in students:
        failed_subjects = [sub for sub, mark in student['marks'].items() if mark < 40]
        if failed_subjects:
            failed_any = True
            print(f"{student['name']} (Roll: {student['roll']}) failed in: {', '.join(failed_subjects)}")

    if not failed_any:
        print("No student has failed.\n")


def update_marks():
    print("\n--- Update Student Marks ---")
    roll = input("Enter roll number of the student: ")

    for student in students:
        if student['roll'] == roll:
            print(f"Current Marks: {student['marks']}")
            subject = input("Enter subject to update: ")
            if subject in student['marks']:
                new_marks = int(input(f"Enter new marks for {subject}: "))
                student['marks'][subject] = new_marks
                print("Marks updated successfully!\n")
            else:
                print("Subject not found in this student's record.\n")
            return

    print("Student with this roll number not found.\n")


def main():
    while True:
        print("\n===== Student Report Card Menu =====")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Display Topper(s)")
        print("4. Search by Roll Number")
        print("5. Show Failed Students")
        print("6. Update Marks")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            find_topper()
        elif choice == '4':
            search_by_roll()
        elif choice == '5':
            show_failed_students()
        elif choice == '6':
            update_marks()
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input! Please enter a number from 1 to 7.\n")

main()
