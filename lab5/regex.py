import re

with open("lab5\example.txt", "r", encoding="utf-8") as file:
    words = file.read()
    #words_low = words.lower()
    text = re.findall(r"\b\w+\b", words)


# 1) Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
# list = []
# for i in text:
#     s = re.search("^ab*.*$", i)
#     if s:
#         list.append(i)
# print(list)

# 2) Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
# list = []
# for i in text:
#     s = re.search("^ab{2,3}$", i)
#     if s:
#         list.append(i)  
# print(list)

# 3) Write a Python program to find sequences of lowercase letters joined with a underscore.
# list = []
# for i in text:
#     s = re.search("[a-z]_[a-z]$",i)
#     if s:
#         list.append(i)
# print(list)

# 4) Write a Python program to find the sequences of one uppercase letter followed 
# by lower case letters.
list = []
for i in text:
    s = re.search("^[A-Z][a-z]+$",i)
    if s:
        list.append(i)
print(list)