def uniq(list):
    i=0
    while i <len(list):
        j = i+1
        while j<len(list):
            if list[i] == list[j]:
                del list[j]
            else:
                j += 1
        i += 1
    print(list)    
    
list = list(map(int, input("Input your numbers:\n").split()))
uniq(list)