#!/usr/bin/python3
"""a modifier"""


import MySQLdb
import sys

if __name__ == "__main__":
    """A mettre"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        pwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
