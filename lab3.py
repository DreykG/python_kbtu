def take_it_easy(x):
    x2 = round(x**(1/2))
    z=True
    for i in range(2,x2+1):
        if x%i == 0:
            return 0
    print(x)
        
list = input("Input numbers:\n").split()
for i in list:
    take_it_easy(int(i))
    