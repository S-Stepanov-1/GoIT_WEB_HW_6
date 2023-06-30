from sqlite3 import Error
from connect import database, make_connection


def handle_input():
    while True:
        try:
            q_num = int(input("Please enter the query number you want to perform: "))
            if 1 <= q_num <= 11:
                return q_num
            else:
                print("\nThe query number must be from 1 to 11. Try again.\n")
        except ValueError:
            print("\nPlease use integer number like 1, 2, 3...\n")


def do_query(curs, sql_query):
    rows = None
    try:
        curs.execute(sql_query)
        rows = curs.fetchall()
    except Error as err:
        print(err)

    return rows


if __name__ == '__main__':
    query_number = str(handle_input())
    sql_file = f"SQLite/query_{query_number}.sql"

    with open(sql_file, "r") as file:
        sql_code = file.read()
        print("\n" + sql_code.split("\n")[0])  # The first line in query_X.sql that describes the work of query

        with make_connection(database) as connection:
            cursor = connection.cursor()

            data = do_query(cursor, sql_code)
            for row in data:
                print(row)
