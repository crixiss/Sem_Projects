class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        x=self.x+ other.x
        y=self.y+other.y
        return Vector(x,y)
    def __str__(self):
        return(f"({self.x},{self.y})")
v1=Vector(1,2)
v2=Vector(6,7)
v3=v1+v2
print(v3)

