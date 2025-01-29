from itertools import permutations

def generate_per(string):
    perms = permutations(string)
    for perm in perms:
        print("".join(perm)) #Преобразование в строку:
                            #Каждая перестановка — это кортеж символов. 
                            #Мы объединяем их в строку с помощью "".join().
        
stroka = input("Input string\n")
generate_per(stroka)