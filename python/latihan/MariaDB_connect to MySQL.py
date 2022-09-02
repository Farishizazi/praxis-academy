#!/usr/bin/python 
import mariadb 

#Connect to MariaDB Server
conn = mariadb.connect(
    user="db_user",
    password="db_user_passwd",
    host="localhost",
    database="employees")
cur = conn.cursor() 

#retrieving information 
some_name = "Georgi" 
cur.execute("SELECT first_name,last_name FROM employees WHERE first_name=?", (some_name,)) #Retrieving Data

for first_name, last_name in cur: 
    print(f"First name: {first_name}, Last name: {last_name}")
    
#insert information 
try: 
    cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB")) #Adding data  
except mariadb.Error as e: 
    print(f"Error: {e}") #Catching Exceptions

conn.commit() 
print(f"Last Inserted ID: {cur.lastrowid}")
    
conn.close()