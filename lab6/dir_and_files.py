import os

# # 1) Write a Python program to list only directories, files and all directories, 
# # files in a specified path.
def ouput_list(path):
    all_elements = os.listdir(path)
    only_direct = [dir for dir in all_elements if os.path.isdir(os.path.join(path, dir))]
    only_files = [file for file in all_elements if os.path.isfile(os.path.join(path, file))]
    
    print("-"*90)
    print(f"Your Path: {path}")
    print("-"*90)
    print(f"Only directories: {only_direct}")
    print("-"*90)
    print(f"Only files: {only_files}")
    print("-"*90)
    print(f"All files in path: {all_elements}")
    
my_path = r"C:\Users\Влад\Desktop\LABA"
ouput_list(my_path)



# # 2) Write a Python program to check for access to a specified path. 
# # Test the existence, readability, writability and executability of the specified path
def absolute_check(path):
    if os.access(path, os.F_OK):
        print("Yes, the file/directory exist")
    else:
        print("The file/directory doesn't exist")
        
    if os.access(path, os.R_OK):
        print("Yes, the file/directory is readability")
    else:
        print("The file/directory isn't readability")
        
    if os.access(path, os.W_OK):
        print("Yes, the file/directory is writability")
    else:
        print("The file/directory isn't writability")
        
    if os.access(path, os.X_OK):
        print("Yes, the file/directory is executability")
    else:
        print("The file/directory isn't executability")

my_path = r"C:\Users\Влад\Desktop\Check\one more\wow.docx"
absolute_check(my_path)



# # 3) Write a Python program to test whether a given path exists or not. 
# # If the path exist find the filename and directory portion of the given path.

def feedback(path):
    if os.path.exists(path):
        print("The path exist")
        print(f"Directory portion: {os.path.dirname(path)}")
        print(f"The filename: {os.path.basename(path)}")
    else:
        print("The Path doesn't exist")
            
my_path = r"C:\Users\Влад\Desktop\Check\one more\wow.docx"
feedback(my_path)



# 4) Write a Python program to count the number of lines in a text file.
file = open(r"lab6\note.txt",'r')    
content = file.readlines()
print(f"The number of lines in a text file: {len(content)}")
file.close()



# # 5) Write a Python program to write a list to a file.
file = open(r"lab6\note.txt", 'a')
our_list = ["Vladislav", "Timuriy", "Anatoliy", "Talghat", "Maxagen"]
for i in our_list:
    file.write(i + " ")
file.close()



# # 6) Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string
letters = list(string.ascii_uppercase)
folder_n = r"lab6\Anarchy"
for i in letters:
    file_name = i + ".txt"
    file_path = os.path.join(folder_n,file_name)
    file = open(file_path, 'w')
    file.close()



# 7) Write a Python program to copy the contents of a file to another file
import shutil
main_file = r"lab6\note.txt"
second_file = r"lab6\second_file.txt"
shutil.copyfile(main_file, second_file)

check_sec = open(second_file,'r')
content = check_sec.read()
print(content)



# 8) Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.
def full_check(my_path):
    if os.path.exists(my_path):
        print("The file exists")
        if os.access(my_path, os.R_OK) and os.access(my_path, os.W_OK):
            print("The path has an access!")
        else:
            print("The path doesn't have an access!")
        os.remove(my_path)
        print(f"The file was deleted! {my_path}")
    else:
        print(f"The path doesn't exist! {my_path}")
        
    f = open(my_path, 'w')

path = r"C:\Users\Влад\Desktop\Check\one more\wow.docx"
full_check(path)
