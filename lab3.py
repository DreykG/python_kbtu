def spy_game(numbers):
    a = False
    for i in range(0,len(numbers)-2):
        if int(numbers[i]) == 0 and int(numbers[i+1]) == 0 and int(numbers[i+2]) == 7:
            a = True
            break
    return a
            
list = input("Input numbers:\n").split()
if spy_game(list):
    print("True")
else:
    print("False")