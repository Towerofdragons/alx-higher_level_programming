#!/usr/bin/python3
"""
Using SQLAlchemy
Define a state class with an ORM
"""
import sys
from model_state import  State
from model_state import  Base
from sqlalchemy import (create_engine)

if __name__ == "__main__":
        eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(eng)
