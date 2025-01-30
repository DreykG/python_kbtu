def histo(list):
    for i in list:
        print(i*"*")
        
list = list(map(int, input("Input your numbers:\n").split()))
histo(list)