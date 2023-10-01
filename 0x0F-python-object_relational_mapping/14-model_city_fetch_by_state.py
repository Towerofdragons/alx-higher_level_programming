#!/usr/bin/python3
"""
print all City objects
"""

from sys import argv

from model_state import State
from model_state import Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
        db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])

        engine = create_engine(db)
        Session = sessionmaker(bind=engine)

        session = Session()

        results = session.query(City, State).join(State)

        for city, state in results.all():
            print(f"{state.name}: ({city.id}) {city.name}")

        session.commit()
        session.close()
