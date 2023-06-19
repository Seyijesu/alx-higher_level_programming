#!/usr/bin/python3
"""contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
Base = declarative_base()


class City(Base):
    """the Class City"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, autoincrement=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
