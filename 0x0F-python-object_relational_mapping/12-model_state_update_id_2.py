#!/usr/bin/python3
"""
Modify the name of a State object
"""

from sys import argv

from model_state import Base
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    session = sessionmaker(bind=engine)()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()
