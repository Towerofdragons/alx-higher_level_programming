#!/usr/bin/python3
"""
Using SQLAlchemy
Defines a state class 
utilize ORM
"""

from model_state import Base, State
import sys
from sqlalchemy import (create_engine)

if __name__ == "__main__":
        eng= create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(eng)
