from sqlite3 import Error
from connect import database, make_connection
from sql_code import *


def create_tables(connect, create_table_sql: str):
    try:
        cursor = connect.cursor()
        cursor.executescript(create_table_sql)
        connect.commit()
    except Error as err:
        print(err)


if __name__ == '__main__':
    tables = sql_create_groups_table + \
             "\n" + sql_create_teachers_table + \
             "\n" + sql_create_students_table + \
             "\n" + sql_create_subjects_table + \
             "\n" + sql_create_grades_table

    with make_connection(database) as connection:
        if connection is not None:
            create_tables(connection, tables)
        else:
            print("Something went wrong...")
