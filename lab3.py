def check(numbers):
    a = False
    for i in range(0,len(numbers)-1):
        if int(numbers[i]) == 3 and int(numbers[i+1]) == 3:
            a = True
            break
    return a
            
list = input("Input numbers:\n").split()
if check(list):
    print("True")
else:
    print("False")