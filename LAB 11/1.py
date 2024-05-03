import psycopg2
from config import *

conn = psycopg2.connect(
    host =host,
    user = user,
    password =password,
    database = db_name
    )

cur = conn.cursor()
def pattern():
    global query
    query = """
    SELECT * FROM Phonebook WHERE """ 
    print(r"Do you want to search by user_name(0)/phone_number(1)/break(any num) enter the number:")
    mode = int(input())
    if mode == 0:
        query += "user_name"
        print("Enter string: ")
        substr = input()
        print("""Select option:
            1-user_name is equal to string
            2-user_name starts with the string
            3-user_name ends with the string
            4-user_name contains the string""")
        mode1 = int(input())
        if mode1 == 1:
            query += "='{}'".format(substr)
        elif mode1 == 2:
            query += " iLIKE '{}%'".format(substr)
        elif mode1 == 3:
            query += " iLIKE '%{}'".format(substr)
        else:
            query += " iLIKE '%{}%'".format(substr)
    elif mode == 1:
        query = "SELECT * FROM Phonebook WHERE "
        print("Enter the phone number to search: ")
        phone_number = input()
        query += "phone_number = '{}'".format(phone_number) 
    else:
        return "error"
    cur.execute(query)
    records = cur.fetchall()
    cur.close()
    conn.close()
    return query, records
if __name__ == '__main__':
    query, records = pattern()
    if not records:
        print("No records found for the given query:", query)
    else:
        print("Records found for the query:", query)
        for record in records:
            print(record)