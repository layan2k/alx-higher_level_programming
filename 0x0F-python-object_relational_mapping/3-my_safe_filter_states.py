#!/usr/bin/python3

"""  a script that takes in arguments and displays
 all values in the states table of hbtn_0e_0_usa
 where name matches the argument.
But this time,one that is safe from MySQL injections
Script should take 3 arguments: mysql username,
 mysql password ,database name and state name searched"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    # Database Connection
    db = MySQLdb.connect(host='localhost',
                         port='3306',
                         user=argv[1],
                         password=argv[2],
                         db=argv[3])

    # crs
    cursor = db.cursor()
    cmd = """SELECT *
            FROM states
            WHERE name=%s ORDER BY id ASC"""
    cursor.execute(cmd, argv[4])
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    db.close()
