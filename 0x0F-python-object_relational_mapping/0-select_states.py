#!/usr/bin/python3

import MySQLdb
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py root kali hbtn_0e_0_usa")
        sys.exit(1)

    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

try:
    db = MySQLdb.connect(
            user='root',
            host='localhost',
            passwd='kali',
            db='hbtn_0e_0_usa'
            )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = cur.fetchall()

    for rows in results:
        print(rows)

except MySQLdb as e:
    print(e)

finally:
    cur.close()
    db.close()
