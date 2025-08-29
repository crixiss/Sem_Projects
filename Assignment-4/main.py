class Number:
    def __init__(self, value):
        self.value = value

    # Arithmetic Operators
    def __add__(self, other):
        return Number(self.value + other.value)
    
    def __sub__(self, other):
        return Number(self.value - other.value)
    
    def __mul__(self, other):
        return Number(self.value * other.value)
    
    def __truediv__(self, other):
        return Number(self.value / other.value)
    
    def __floordiv__(self, other):
        return Number(self.value // other.value)
    
    def __mod__(self, other):
        return Number(self.value % other.value)
    
    def __pow__(self, other):
        return Number(self.value ** other.value)

    # Relational Operators
    def __eq__(self, other):
        return self.value == other.value
    
    def __ne__(self, other):
        return self.value != other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.value >= other.value

    def __str__(self):
        return str(self.value)

a = Number(10)
b = Number(3)

# Arithmetic
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
