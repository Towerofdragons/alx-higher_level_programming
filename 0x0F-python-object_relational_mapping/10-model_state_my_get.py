#!/usr/bin/python3
"""

From hbtn_0e_6_usa, print  prints the State object with the name passed as argument.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
        db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])
        engine = create_engine(db)
        session = sessionmaker(bind=engine)()
        state = session.query(State).filter(State.name == argv[4]).first()
        if state is not None:
            print('{0}'.format(state.id))
        else:
            print("Not found")
