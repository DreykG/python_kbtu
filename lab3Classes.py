a = lambda x: x>1 and all(x%i != 0 for i in range(2, int(x**0.5)+1))
# -all- checks, that all coundtition in () were True
list2 = list(map(int, input("Input your numbers:\n").split()))

prime_num = list(filter(a,list2))#a-name of funct. list2-name of objects, with we work.
print("Prime numbers from previous lust:")
print(prime_num)


