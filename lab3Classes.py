class Points:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def show(self):
        print(f"Coordinates of point1 = ({self.x1},{self.y1})")
        print(f"Coordinates of point2 = ({self.x2},{self.y2})")
        
    def move(self):
        m = int(input("What is point do you want to change? 1 or 2\n"))
        if m == 1:
            self.x1 = int(input("Input X1-coord\n"))
            self.y1 = int(input("Input Y1-coord\n"))
        if m == 2:
            self.x2 = int(input("Input X2-coord\n"))
            self.y2 = int(input("Input Y2-coord\n"))
    
    def lenght(self):
        self.lenght = round(float(     (((self.x2 - self.x1)**2)  + ((self.y2 - self.y1)**2))**0.5),1)
        print(f"Lenght between 2 points = {self.lenght}")
        
x1 = int(input("Input X1-coord\n"))
y1 = int(input("Input Y1-coord\n"))
x2 = int(input("Input X2-coord\n"))
y2 = int(input("Input Y2-coord\n"))

newp = Points(x1,y1,x2,y2)
while True:
    print("Input action, which you want to complete:")
    print("show")
    print("move")
    print("lenght")
    print("exit")
    dd = input()
    if dd == "show":
        newp.show()
    if dd == "move":
        newp.move()
    if dd == "lenght":
        newp.lenght()
    if dd == "exit":
        break