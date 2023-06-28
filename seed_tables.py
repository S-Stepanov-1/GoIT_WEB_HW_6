import sqlite3
from datetime import datetime, date, timedelta
from random import randint
from faker import Faker
from connect import database, make_connection


NUMBER_OF_STUDENTS = 50
NUMBER_OF_TEACHERS = 4
GROUPS = ["BMX-20", "KFC-20", "UFC-20", "MU-20"]
SUBJECTS = ["Physics", "Maths", "Art", "PE", "Philosophy", "IT"]

fake = Faker()


def do_filling(connect, sql_code, values):
    """The function creates a cursor object, inserts data into the database table.
    Then it commits the changes and close the cursor object"""

    cursor = connect.cursor()
    try:
        cursor.executemany(sql_code, values)
        connect.commit()
    except sqlite3.Error as err:
        print(err)
    finally:
        cursor.close()


def seed_groups(connect):
    """The function prepared SQL code and calls 'do_filling' function"""
    sql_groups = "INSERT INTO groups (name) VALUES (?);"
    do_filling(connect, sql_groups, zip(GROUPS,))


def seed_students(connect):
    """The function prepared SQL code, forms students' list and list of group id.
     Then it calls 'do_filling' function"""
    students = [fake.name() for _ in range(NUMBER_OF_STUDENTS)]  # generate students' list
    sql_students = "INSERT INTO students (fullname, group_id) VALUES (?, ?);"
    list_group_id = [randint(1, len(GROUPS)) for _ in range(NUMBER_OF_STUDENTS)]

    do_filling(connect, sql_students, zip(students, list_group_id))


def seed_teachers(connect):
    """The function prepared SQL and calls 'do_filling' function"""
    teachers = [fake.name() for _ in range(NUMBER_OF_TEACHERS)]  # generate students' list
    sql_students = "INSERT INTO teachers (fullname) VALUES (?);"

    do_filling(connect, sql_students, zip(teachers,))


def seed_subjects(connect):
    """The function prepared SQL code and forms teachers' id list.
         Then it calls 'do_filling' function"""
    list_teacher_id = [randint(1, NUMBER_OF_TEACHERS) for _ in range(len(SUBJECTS))]
    sql_groups = "INSERT INTO subjects (name, teacher_id) VALUES (?, ?);"

    do_filling(connect, sql_groups, zip(SUBJECTS, list_teacher_id))


def get_list_date(start, finish) -> list[date]:
    """The function return a list with workdays between two dates: start and finish"""
    result = []
    current_day = start
    while current_day < finish:
        if current_day.isoweekday() < 6:
            result.append(current_day)
        current_day += timedelta(1)

    return result


def seed_grades(connect):
    """The function prepared SQL code, calls the 'get_list_date' function to get the workdays and
    forms grades list with tuples. Then it calls 'do_filling' function to insert the data into table."""
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    finish_date = datetime.strptime("2023-05-31", "%Y-%m-%d")

    sql_grades = "INSERT INTO grades (student_id, subject_id, grade, date_of) VALUES (?, ?, ?, ?)"
    list_date = get_list_date(start_date, finish_date)

    grades = []
    for day in list_date:
        random_subject = randint(1, len(SUBJECTS))  # choosing a random subject

        random_students = [randint(1, NUMBER_OF_STUDENTS) for _ in range(5)]  # making a list with 5 random students
        for student in random_students:
            #  append a tuple(student_id, subject, grade, day of the week) to grades
            grades.append((student, random_subject, randint(1, 5), day))

    do_filling(connect, sql_grades, grades)


if __name__ == '__main__':
    with make_connection(database) as connection:
        if connection is not None:
            seed_groups(connection)
            seed_students(connection)
            seed_teachers(connection)
            seed_subjects(connection)
            seed_grades(connection)
        else:
            print("Something went wrong...")
