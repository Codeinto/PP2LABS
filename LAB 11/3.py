import psycopg2
from config import *
conn = psycopg2.connect(
    host =host,
    user = user,
    password =password,
    database = db_name
    )

cur = conn.cursor()
def insert_many_users(users):
    incorrect_data = []

    try:
        for user in users:
            user_data = user.split(',')
            if len(user_data) != 2:
                incorrect_data.append((user, "Invalid data format: expected 'user_name,phone_number'"))
                continue
            
            user_name, phone_number = user_data
            if not phone_number.isdigit() or len(phone_number) != 11:
                incorrect_data.append((user, "Invalid phone number format"))
                continue
            
            cur.execute("INSERT INTO Phonebook (id, user_name, phone_number) VALUES (DEFAULT, %s, %s)", (user_name, phone_number))

        if incorrect_data:
            print("Incorrect data:")
            for user_data, error_message in incorrect_data:
                print(user_data, "-", error_message)
        else:
            print("All users inserted successfully")
        
        conn.commit()

    except psycopg2.Error as e:
        print("Error:", e)
    
    finally:
        cur.close()
        conn.close()

# Example usage
users_to_insert = [
    "Asik,12345678901",
    "Zhasik,9876543210",  # Incorrect phone number
    "Dima,87055737186"
]

insert_many_users(users_to_insert)
