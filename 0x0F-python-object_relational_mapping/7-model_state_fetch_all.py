#!/usr/bin/python3
"""
Lists all state objects from 
the db `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State

from model_state import Base
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Get all states from the DB
    After accessing db.
    """
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])

    engine = create_engine(db)

    Session = sessionmaker(bind=engine)

    session = Session()

    for inst in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(inst.id, inst.name))
