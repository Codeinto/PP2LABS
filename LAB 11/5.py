import psycopg2
from config import *
conn = psycopg2.connect(
    host =host,
    user = user,
    password =password,
    database = db_name
    )

cur = conn.cursor()

def delete  (username=None, phone=None):
    try:
        if username:
            cur.execute("DELETE FROM Phonebook WHERE user_name = %s", (username,))
        elif phone:
            cur.execute("DELETE FROM Phonebook WHERE phone_number = %s", (phone,))
        else:
            print("Please provide either username or phone number.")
            return
        conn.commit()
        print("Data deleted successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error deleting data from database:", e)
    finally:
        cur.close()
        conn.close()

delete(username="Dima")
delete(phone="87055737186")
