import sqlite3
from contextlib import contextmanager

database = "./SQLite/HW_6_GoIT.db"


@contextmanager
def make_connection(db_file):
    connection = sqlite3.connect(db_file)
    yield connection
    connection.rollback()
    connection.close()
