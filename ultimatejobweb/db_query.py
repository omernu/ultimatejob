import sqlite3
from sqlite3 import Error


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


def select_all_jobs(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM 'ultimatejobweb_jobs'")

    rows = cur.fetchall()

    for row in rows:
        print(row)


'''def select_jobs_by_company(conn, CompanynName):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM ultimatejobweb_jobs WHERE priority=?", (CompanynName,))

    rows = cur.fetchall()

    for row in rows:
        print(row)'''


def main():
    database = r"//vagrant/.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:
        '''print("1. Query task by priority:")
        select_jobs_by_company(conn, 'Facebook')'''

        print("2. Query all tasks")
        select_all_jobs(conn)


if __name__ == '__main__':
    main()
