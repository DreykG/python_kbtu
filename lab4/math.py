import math as m
# 1) Write a Python program to convert degree to radian.
def transfer(deg):
    return round(deg*(m.pi/180), 6)
degree = int(input())
print(f"Input degree: {degree}")
print(f"Output radian: {transfer(degree)}")

#or
def transfer2(n):
    return round(m.radians(n),6)
N = int(input())
print(f"Input degree: {N}")
print(f"Output radian: {transfer2(N)}")


# 2) Write a Python program to calculate the area of a trapezoid.
def trapezoid_area(h,a,b):
    print(f"Height: {h}")
    print(f"Base, first value: {a}")
    print(f"Base, second value: {b}")
    print(f"Expected Output: {round(0.5*h*(a+b), 1)}")

h = float(input())
a = float(input())
b = float(input())
trapezoid_area(h,a,b)


# 3) Write a Python program to calculate the area of regular polygon.
def area_perfect_poly(n,l):
    print(f"Input number of sides: {n}")
    print(f"Input the length of a side: {l}")
    print(f"The area of the polygon is: {round((n*l**2)/4*m.tan(m.pi/n))}")
    
N = int(input())
L = int(input())
area_perfect_poly(N,L)


# 4)Write a Python program to calculate the area of a parallelogram.
def area_parallelogram(l,h):
    print(f"Length of base: {l}")
    print(f"Height of parallelogram: {h}")
    print(f"Expected Output: {round(l*h,0)}")
    
l = float(input())
h = float(input())
area_parallelogram(l,h)