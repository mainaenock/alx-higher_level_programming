#!/usr/bin/python3

import MySQLdb

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

finally:
    cur.close()
    db.close()
