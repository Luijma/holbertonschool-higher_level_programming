#!/usr/bin/python3
""" Lists all objects from the database """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from model_city import City
import sqlalchemy

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    with Session() as session:
        result = session.query(City, State).join(State)

        for city, state in result:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
