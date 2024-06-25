#!/usr/bin/python3

"""  lists all states with a name starting with
    N (upper N) from the database hbtn_0e_0_usa """

if __name__ == '__main__':

    import MySQLdb
    import sys

    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )

        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
        results = cur.fetchall()

        for row in results:
            if row[1] == sys.argv[4]:
                print(row)
    except MySQLdb.Error as e:
        print(e)

    finally:
        cur.close()
        db.close()
