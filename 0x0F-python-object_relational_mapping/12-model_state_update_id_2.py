#!/usr/bin/python3
""" Lists all objects from the database """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select, update
import sqlalchemy

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    with Session() as session:
        statement = update(State).where(State.id == 2).\
                    values(name='New Mexico')

        session.execute(statement)
        session.commit()
