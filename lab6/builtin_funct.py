import re 
# # 1) Write a Python program with built in function to multiply all the numbers in a list
storage = []
a = int(input())
for i in range(0, a):
    n = int(input())
    storage.append(n)
    
mult = eval('*'.join(map(str, storage)))
print(f"Muliplication of all numbers = {mult}")

# # 2) Write a Python program with builtin function that accepts a string 
# and calculate the number of upper case letters and lower case letters
string = input()
upper_sum = sum(map(str.isupper, string))
lower_sum = sum(map(str.islower, string))
print(f"Sum of uppercase: {upper_sum}")
print(f"Sum of lowercase: {lower_sum}")

# # 3) Write a Python program with builtin function that checks whether a passed string 
# is palindrome or not.
text = input()
reversed_text = ''.join(reversed(text))
print(reversed_text)
if text == reversed_text:
    print("Yes")
else:
    print("No")
    
    
# # 4) Write a Python program that invoke square root function after specific milliseconds.
import time
root = int(input())
timer = int(input())
ms = timer/1000
time.sleep(ms)
print(f"Root from {root} after {timer} miliseconds is {root**0.5}")

# # 5) Write a Python program with builtin function that 
# returns True if all elements of the tuple are true.
tuple = (1,1,1,1,1,1)
compare = all(tuple)
if compare:
    print("true")
else:
    print("else")