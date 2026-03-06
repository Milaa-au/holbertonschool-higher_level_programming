#!/usr/bin/python3
"""A ajouter."""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    query = ("SELECT * FROM states WHERE name LIKE BINARY %s "
         "ORDER BY id ASC")
    cur.execute(query)

    states = cur.fetchall

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
