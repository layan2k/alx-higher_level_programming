#!/usr/bin/python3

""" script that takes in an argument and displays all values
 in the states table of hbtn_0e_0_usa where name matches the argument
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
    cursor.execute("""SELECT *
                   FROM states WHERE name LIKE
                   '{:s}' ORDER BY id ASC""".format(argv[4]))
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    db.close()
