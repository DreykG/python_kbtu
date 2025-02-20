import re

with open("lab5\example.txt", "r", encoding="utf-8") as file:
    words = file.read()
    #words_low = words.lower()
    text = re.findall(r"\b\w+\b", words)


# 1) Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
list = []
for i in text:
    s = re.search("^ab*.*$", i)
    if s:
        list.append(i)
print(list)

# 2) Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
list = []
for i in text:
    s = re.search("^ab{2,3}$", i)
    if s:
        list.append(i)  
print(list)

# 3) Write a Python program to find sequences of lowercase letters joined with a underscore.
list = []
for i in text:
    s = re.search("[a-z]_[a-z]",i)
    if s:
        list.append(i)
print(list)

# 4) Write a Python program to find the sequences of one uppercase letter followed 
# by lower case letters.
list = []
for i in text:
    s = re.search("^[A-Z][a-z]+$",i)
    if s:
        list.append(i)
print(list)

#5) Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
list = []
for i in text:
    s = re.search(".+ab$",i)
    if s:
        list.append(i)
print(list)

#6) Write a Python program to replace all occurrences of space, comma, or dot with a colon.
word_duble_points = re.sub("[,. ]", ":",words)
print(word_duble_points)

# 7) Write a python program to convert snake case string to camel case string.
list = []
for i in text:
    s = re.search(".*[a-z]_[a-z]+$",i)
    if s:
        print(i, end=", ")
        new_word = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), i)
        list.append(new_word)
print()
print(list)

# 8) Write a Python program to split a string at uppercase letters.

# for my string:
a = "Hello, the best student of KBTU"
b = a.upper()
s = re.findall(r'.',b)
print(s)

#for all text:
for i in text:
    b = i.upper()
    s = re.findall(r'.',b)
    print(s)

# 9) Write a Python program to insert spaces between words starting with capital letters.
string = "HelloTheBestStudentOfKBTU"
new_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
print(new_string)


# 10) Write a Python program to convert a given camel case string to snake case.
camelcase = "TheBestStudentOfKbtuUniversityFikus"
snake = re.sub(r'([a-z])([A-Z])', r'\1_\2', camelcase)
snake_case = re.sub(r'(_)([A-Z])', lambda m: m.group(1) + m.group(2).lower(), snake)
print(snake_case)