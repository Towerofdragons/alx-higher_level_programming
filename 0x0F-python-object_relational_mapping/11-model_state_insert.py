#!/usr/bin/python3
"""
Add State object:
Louisiana 
to db
"""

from sys import argv

from model_state import State
from model_state import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])

    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(f'{format(new_state.id)}')
    session.close()
