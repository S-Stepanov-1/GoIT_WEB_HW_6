from sqlite3 import Error
from connect import database, make_connection
from sql_code import *


def create_table(connect, create_table_sql: str):
    try:
        cursor = connect.cursor()
        cursor.execute(create_table_sql)
        connect.commit()
    except Error as err:
        print(err)


if __name__ == '__main__':
    with make_connection(database) as connection:
        if connection is not None:
            create_table(connection, sql_create_groups_table)  # creating groups' table
            create_table(connection, sql_create_teachers_table)  # creating teachers' table
            create_table(connection, sql_create_students_table)  # creating students' table
            create_table(connection, sql_create_subjects_table)  # creating subjects' table
            create_table(connection, sql_create_grades_table)  # creating grades' table
        else:
            print("Something went wrong...")
