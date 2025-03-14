#!/usr/bin/python3
"""
Defines the City class, which represents a city in the databases.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False
                )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
