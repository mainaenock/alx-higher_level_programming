#!/usr/bin/python3

""" lists all states """

if __name__ == '__main__':

    import MySQLdb
    import sys
    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )

        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
        results = cur.fetchall()

        for rows in results:
            print(rows)

    except MySQLdb as e:
        print(e)

    finally:
        cur.close()
        db.close()
