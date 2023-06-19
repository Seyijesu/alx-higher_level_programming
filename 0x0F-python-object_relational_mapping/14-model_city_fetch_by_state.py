#!/usr/bin/python3
"""prints all City objects from
the database hbtn_0e_14_usa.
"""


if __name__ == "__main__":
    try:
        import sys
        from model_state import Base, State
        from model_city import City
        from sqlalchemy import create_engine
        from sqlalchemy.orm import Session
        n = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                          .format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(n)
        session = Session(n)
        for state, city in session.query(State, City).\
                filter(City.state_id == State.id).order_by(City.id).all():
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    except:
        pass
