#!/usr/bin/python3
"""takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name = %s "
                "COLLATE 'latin1_general_cs' "
                "ORDER BY id ASC", (sys.argv[4],))
    for r in cur.fetchall():
        print(r)
    cur.close()
    db.close()
