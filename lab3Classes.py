class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        self.money = int(input("How much do you want to deposit your balance?\n"))
        self.balance += self.money
        
    def withdraw(self):
        while True:
            self.money = int(input("How much do you want to withdraw your balance?\n"))
            if self.money > self.balance:
                print("On your balance no so much money!")
            else:
                self.balance -= self.money
                break
        
    def check(self):
        print(f"Your balance: {self.balance}")
        

name = input("What is your name?\n")
balance = int(input("What is your balance?\n"))
my_bank = Bank(name,balance)
while True:
    z = input('''What do you want to do?
            -deposite
            -withdraw
            -check
            -exit\n''')
    if z == "deposite":
        my_bank.deposit()
        
    if z == "check":
        my_bank.check()
        
    if z == "withdraw":
        my_bank.withdraw()
        
    if z == "exit":
        break