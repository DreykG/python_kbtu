#Python has no command for declaring a variable.
#A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)



#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)



#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0



#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))



#String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'



#Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a



#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"



#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"



#Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)



#And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)



#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. 
# This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



#The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)



#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)



#You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)



#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)



#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "John"
print(x + y)



#The best way to output multiple variables in the print() function is to separate them with commas, 
#which even support different data types:
x = 5
y = "John"
print(x, y)



#Variables that are created outside of a function (as in all of the examples in the previous pages) 
#are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.
#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()



#The global Keyword
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.

#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



#Also, use the global keyword if you want to change a global variable inside a function.
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)




