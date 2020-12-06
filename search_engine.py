import sqlite3
from sqlite3 import Error
import reqeusts
from bs import beautifulsuop4


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_preferences_by_UserID(conn, User):
    """
    Query preferences by UserID
    :param conn: the Connection object
    :param UserID:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Users WHERE User=?", (User,))
    rows = cur.fetchall()

    for row in rows:
        print(row)
        return row


def main():
    """
    main func for the search engine
    """
    database = r"/vagrant/db.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:
 
        select_preferences_by_UserID(conn, User)
      

if __name__ == '__main__':
    main()