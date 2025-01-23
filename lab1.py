from random import *

boys = ['Vlad','Egor','Isa','Anatoliy','Timur']
girls = ['Marina','Katya','Elena','Daria','Alina']
a = "Mustafa"
boys.append(a)
for i in range(0,len(boys)):
    if "a" in boys[i]:
        boys.remove(boys[i])
        i = 1
        
        
for j in boys:
    print(j)
