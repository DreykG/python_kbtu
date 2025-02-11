# 1) Create a generator that generates the squares of numbers up to some number N.
n = int(input())
for i in range(1,n+1):
    print(f"{i} in square = {i**2}")


# 2) Write a program using generator to print the even numbers 
# between 0 and n in comma separated form where n is input from console.
def even_num(n):
    for i in range(0,n+1):
        if i%2 == 0:
            yield i #like return, but doesnt stop function. Saved value

n = int(input())
nums = [str(num) for num in even_num(n)]
print(",".join(nums))


# 3)Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and n.
def generating(n):
    for i in range(0, n+1):
        if i%3 == 0 and i%4 == 0:
            yield i
            
N = int(input())
generator = [str(n) for n in generating(N)]
print(",".join(generator))


# 4) Implement a generator called squares to yield the square of all numbers from (a) to (b). 
# Test it with a "for" loop and print each of the yielded values.
def squares(a,b):
    for i in range(a,b+1):
        print(i**2, end=" ")
    
A = int(input("A\n"))
B = int(input("B\n"))
squares(A,B)


# 5) Implement a generator that returns all numbers from (n) down to 0.
def returning(n):
    for i in range(n,-1,-1):
        print(i,end=" ")

N = int(input())
returning(N)