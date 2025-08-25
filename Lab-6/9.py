class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Addresss:
    def __init__(self,street,city,zipcode):
        self.street=street
        self.city=city
        self.zipcode=zipcode
class Contact:
    def __init__(self,person,address):
        self.person=person
        self.address=address
    def display(self):
        print("Contact Details")
        print(f"Name:{self.person.name}")
        print(f"Age:{self.person.age}")
        print(f"Street:{self.address.street}")
        print(f"City:{self.address.city}")
        print(f"Zipcode:{self.address.zipcode}")
p=Person("Sa",17)
a=Addresss("Pragatinagar marg","Kathmandu","1100")
c=Contact(p,a)
c.display()
