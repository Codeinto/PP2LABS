import psycopg2
from config import *
conn = psycopg2.connect(
    host =host,
    user = user,
    password =password,
    database = db_name
    )

cur = conn.cursor()

def fetch_phonebook_data(limit, offset):
    try:
        cur.execute("SELECT id, user_name, phone_number FROM Phonebook ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()
        return rows
    except psycopg2.Error as e:
        print("Error fetching data from database:", e)
    finally:
        cur.close()
        conn.close()

# Example usage with input
limit = int(input("Enter the limit: "))
offset = int(input("Enter the offset: "))
phonebook_data = fetch_phonebook_data(limit, offset)
for row in phonebook_data:
    print(row)
