#!/usr/bin/python3

"""a script that takes in the name of a state
 as an argument and lists all cities of that state,
  using the database hbtn_0e_4_usa
Script should take 3 arguments: mysql username, mysql password ,
database name and state name searched"""

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
    cursor.execute("""SELECT cities.id, cities.name, states.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 ORDER BY cities.id ASC""")
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    db.close()
