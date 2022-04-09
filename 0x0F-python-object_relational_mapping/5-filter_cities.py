#!/usr/bin/python3
"""Lists al lstaets from hbtn_0e_0_usa database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities \
                 INNER JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id ASC",(argv[4], ))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
