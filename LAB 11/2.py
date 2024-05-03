import psycopg2
from config import *
conn = psycopg2.connect(
    host =host,
    user = user,
    password =password,
    database = db_name
    )
cur = conn.cursor()
def insert(user_name, phone_number):
    try:
        cur.execute("SELECT * FROM Phonebook WHERE user_name = %s", (user_name,))
        exist = cur.fetchone()
        if exist:
            cur.execute("UPDATE Phonebook SET phone_number = %s WHERE user_name = %s", (phone_number, user_name))
            print("Phone number updated for existing user:", user_name)
        else:
            user_id = input("Enter ID for the new user: ")
            cur.execute("INSERT INTO Phonebook (id, user_name, phone_number) VALUES (%s, %s, %s)", (user_id, user_name, phone_number))
            print("New record inserted successfully")
        conn.commit()
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()
insert(input("Enter user name: "), input("Enter phone number: "))
