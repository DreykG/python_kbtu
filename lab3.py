def rev(stroka):
    string = stroka.split()
    for i in range(len(string)-1,-1,-1):
        print(string[i],end=" ")
    
stroka = input("Input string\n")
rev(stroka)