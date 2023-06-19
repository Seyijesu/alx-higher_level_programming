#!/usr/bin/python3
"""lists all State objects that contain
the letter a from the database.
"""
if __name__ == "__main__":
    try:
        import sys
        from model_state import Base, State
        from sqlalchemy import create_engine
        from sqlalchemy.orm import Session
        """This script should take 3 arguments: mysql username, mysql password
        and database name"""
        en = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(en)
        session = Session(en)
        for state in session.query(State)\
                            .filter(State.name.like('%a%')).order_by(State.id):
            print("{}: {}".format(state.id, state.name))
    except:
        pass
