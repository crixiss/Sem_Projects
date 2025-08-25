class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.employee_id=employee_id
        self.salary=salary
    def display_employee(self):
        print("Employee Details:")
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')
        print(f'Employee_id:{self.employee_id}')
        print(f'Salary:{self.salary}')
e1=Employee("Ram",27,"Sa72",20000)
e1.display_employee()
