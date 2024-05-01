import psycopg2 as ps
from config import *

def get_Phonebook():
    """ Retrieve data from the vendors table """

    try:
        connection = ps.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("SELECT id, user_name FROM Phonebook ORDER BY user_name")
            print("The number of parts: ", cursor.rowcount)
            row = cursor.fetchone()

            while row is not None:
                print(row)
                row = cursor.fetchone()

    except (Exception, ps.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_Phonebook()        