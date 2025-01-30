class Shape:
    def area(self):
        return 0

class Square(Shape):  #nasleduetsya from Shape
    def __init__(self, lenght):
        self.lenght = lenght
        
    def area(self):
        return self.lenght * self.lenght
    
class Rectangle(Shape):
    def __init__(self, lenght, weight):
        self.lenght = lenght
        self.weight = weight
        
    def area(self):
        return 2*(self.lenght+self.weight)
    
my_cl = Shape()
print(f"Shape area: {my_cl.area()}")

my_cl = Square(5)
print(f"Square area: {my_cl.area()}")
#good
my_cl = Rectangle(5,4)
print(f"Rectangle area: {my_cl.area()}")