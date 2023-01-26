import sqlite3
file = 'data.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()

def createdata():
    file = 'data.db'
    connection = sqlite3.connect(file)
    print(connection)
    cursor = connection.cursor()
    query ="""
    create table if not exists customers (
        id integer primary key autoincrement,
        petname tinytext,
        species tinytext,
        name tinytext,
        number tinytext,
        email tinytext,
        amountowed float,
        firstvisit tinytext);
        """
    cursor.execute(query)

def addcustomer():
    petname = input("Enter pet name: ")
    species = input("Enter species of pet: ")
    name = input("Enter name: ")
    number = input("Enter number: ")
    email = input("Enter email: ")
    amountowed = float(input("Enter the amount owed: "))
    firstvisit = input("Enter the date of first visit: ")
    data = [petname,species,name,number,email,amountowed,firstvisit]
    query = f"insert into customers (petname,species,name,number,email,amountowed,firstvisit) values ('{data[0]}','{data[1]}','{data[2]}','{data[3]}','{data[4]}',{data[5]},'{data[6]}');"
    cursor = connection.cursor()  
    cursor.execute(query)
    connection.commit()

def readcustomerid():
    name = input("Enter customers id: ")
    query = f'select * from customers where id={name}'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

def readcustomeremail():
    name = input("Enter customers email: ")
    query = f'select * from customers where email="{name}"'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

def readcustomernumber():
    name = input("Enter customers phone number: ")
    query = f'select * from customers where number="{name}"'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
for __name__ in "__main__":
    createdata()
    while True:
        print("1. Add a new customer\n2. Retrieve customers information\n3. Exit")
        x = input("Enter option: ")
        if x == '1':
            addcustomer()
        if x == '2':
            print("1. Search by ID\n2. Search by email\n3. Search by phone number")
            y = input("Enter option: ")
            if y == '1':
                readcustomerid()
            if y == '2':
                readcustomeremail()
            if y == '3':
                readcustomernumber()
        if x == '3':
            exit()