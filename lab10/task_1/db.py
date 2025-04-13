import psycopg2
import csv

#Connect to DataBase
connect = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="vlad19supkbtu",
    host="localhost",
    port="5432" 
)

cursor = connect.cursor() #Our Bridge for DataBase
def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Phonebook(
        name VARCHAR(100),
        phone_number VARCHAR(20)
        );
        """)
    connect.commit()
    print("Table was created!")
    
def add_contact():
    name = input("Name:\n")
    phone = input("Phone number:\n")
    
    query = "INSERT INTO Phonebook (name,phone_number) VALUES (%s,%s)"
    cursor.execute(query,(name,phone))
    connect.commit()
    print("Contact was sucessfully added!")
    
def show_contacts():
    cursor.execute("SELECT * FROM Phonebook;")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Name: {row[0]} | Phone number: {row[1]}")
        
    connect.commit()
    
def search_by_name():
    name = input("Input name:\n")
    query = "SELECT * FROM Phonebook WHERE name=%s"
    cursor.execute(query, (name,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"Name: {row[0]} | Phone number: {row[1]}")
    else:
        print(f"Contact does not exist!") 
    connect.commit()
    
def delete_contact():
    name = input("Name:\n")
    phone = input("Phone number:\n")
    check_query ="SELECT * FROM phonebook WHERE name=%s AND phone_number=%s"
    cursor.execute(check_query, (name,phone,))
    finded = cursor.fetchall()
    if finded:
        query = "DELETE FROM Phonebook WHERE name=%s AND phone_number=%s"
        cursor.execute(query, (name,phone,))
        connect.commit()
        print(f"Contact {name} with phone number {phone} was deleted!")
    else:
        print("Contact wasn't deleted, because it doesn't exist")
    

def update_contact():
    choice = int(input('''What do you want to update?
1 - name.
2 - phone number.
'''))
    if choice == 1:
        old_name = input("Old name:\n")
        check_query = "SELECT * FROM Phonebook WHERE name=%s"
        cursor.execute(check_query,(old_name,))
        finded = cursor.fetchall()
        if finded:
            new_name = input("New name:\n")
            query = "UPDATE Phonebook SET name =%s WHERE name =%s"
            cursor.execute(query, (new_name,old_name,))
            connect.commit()
            print("Contact's name was updated!")
        else:
            print("Contact wasn't finded!")
        
    elif choice == 2:
        old_phone = input("Old phone:\n")
        check_query = "SELECT * FROM Phonebook WHERE phone_number=%s"
        cursor.execute(check_query,(old_phone,))
        finded = cursor.fetchall()
        if finded:
            new_phone = input("New phone:\n")
            query = "UPDATE Phonebook SET phone_number =%s WHERE phone_number =%s"
            cursor.execute(query, (new_phone,old_phone,))
            connect.commit()
            print("Contact's phone was updated!")
        else:
            print("Contact wasn't finded!")
        
def import_csv_file():
    file_name = input("Input the name of file. Example: contacts.csv\n")
    with open(rf"lab10\task_1\{file_name}", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';') #Reading such as Dictionary
        for row in reader:
            name = row['name']
            phone = row['phone_number']
            query = "INSERT INTO Phonebook (name,phone_number) VALUES (%s,%s)"
            cursor.execute(query,(name,phone))
        
        connect.commit()
        print("Contacts were added!")
            
            
def filter_by():
    asc_desc = int(input('''
Input criteria for filtration of name:
1 - by ascension.
2 - by descension.\n'''))
    if asc_desc == 1:
        filt = "ASC"
    elif asc_desc == 2:
        filt = "DESC"
    else:
        print("Error!")
        return 0
    query = f"SELECT * FROM phonebook ORDER BY name {filt};"
    cursor.execute(query,(filt,))
    rows = cursor.fetchall()
    for row in rows:
        print(f"Name: {row[0]} | Phone number: {row[1]}")
    
    connect.commit()
    
    
    
    
    
    
action = int(input('''List of survices:
1 - Add new contact. 
2 - Get list of all contacts.
3 - Search contact by name.
4 - Delete contact.
5 - Update contact.
6 - Import from CSV.
7 - Filtration.

0 - create Table "Phonebook".
'''))
if action == 0:
    create_table()
#Checking on table existing
cursor.execute("SELECT to_regclass('public.phonebook')")
result = cursor.fetchone()[0]

if result:
    print("This table exists.")
    if action == 1:
        add_contact()
    elif action == 2:
        show_contacts()
    elif action == 3:
        search_by_name()
    elif action == 4:
        delete_contact()
    elif action == 5:
        update_contact() 
    elif action == 6:
        import_csv_file()
    elif action == 7:
        filter_by()
else:
    print("Table doesn't exist!")
cursor.close()

    