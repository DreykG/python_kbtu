def palidrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

s = input("Input your word\n")
if palidrome(s):
    print("Yes")
else:
    print("No")