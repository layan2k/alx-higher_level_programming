#!/usr/bin/python3
"""
state objects from database via python
Script should take 3 arguments: mysql username, mysql password ,database name
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    for i in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(i.id, i.name))

    session.close()
