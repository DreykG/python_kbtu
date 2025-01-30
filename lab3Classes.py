class strings:
    def __init__(self): #run when class start creating
        self.s = input("Input string:\n")
        
    def printstring(self):
        print(f"Your string: {self.s}")
        
    def reverstr(self):
        print(f"reversed string: {self.s[::-1]}")
        
    def lenghtstr(self):
        print(f"Lenght of string = {len(self.s)}")
        
my_class = strings()
my_class.printstring()
my_class.reverstr()
my_class.lenghtstr()