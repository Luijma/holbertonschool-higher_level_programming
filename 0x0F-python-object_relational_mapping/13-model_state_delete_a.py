#!/usr/bin/python3
""" Lists all objects from the database """

from sys import argv
from model_state import Base, State
from sqlalchemy import table, create_engine, column, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
import sqlalchemy

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    with Session() as session:
        statement = delete(State).where(State.name.contains("a")).\
                execution_options(synchronize_session="fetch")
        session.execute(statement)
        session.commit()
