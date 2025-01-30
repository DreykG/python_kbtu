from random import randint
def fijma(x,name):
    guess = 0
    while True:
        a = int(input("Take a guess.\n"))
        if a < x:
            print("Your guess is too low.")
            guess+=1
        if a > x:
            print("Your guess is too high.")
            guess+=1
        if a==x:
            guess+=1
            print(f"Good job, {name}! You guessed my number in {guess} guesses!")
            break
            
    
    
        
name = input("Hello! What is your name?\n")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
x = randint(1,20)
fijma(x,name)



