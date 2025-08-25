class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Saksham", 72)
s2 = Student("Crixis", 99)
s3 = Student("Kira", 88)

s1.show_details()
s2.show_details()
s3.show_details()
