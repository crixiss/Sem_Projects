def student_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

name = input("Enter name: ")
age = input("Enter age: ")
grade = input("Enter grade: ")

student_profile(name=name, age=age, grade=grade)
