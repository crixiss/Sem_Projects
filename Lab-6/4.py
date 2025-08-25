class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
class Circle(Shape):
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius*self.radius*3.14
shapes = [Rectangle(10,30), Circle(14)]
for shape in shapes:
    print(f"Area: {shape.area()}")
