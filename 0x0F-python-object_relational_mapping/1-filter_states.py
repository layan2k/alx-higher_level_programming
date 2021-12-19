#!/usr/bin/python3
""" script that lists all states with a name starting with N
 (upper N) from the database hbtn_0e_0_usa.
Script should take 3 arguments: mysql username,
 mysql password and database name"""

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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    db.close()

