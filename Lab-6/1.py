class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def display_info(self):
        print("Student Details:")
        print(f'Name={self.name}\n Roll no.={self.roll_number}\n Marks={self.marks}')
s1=Student("saksham","72",72)
s1.display_info()
