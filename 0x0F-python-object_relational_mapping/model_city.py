#!/usr/bin/python3
"""
Define a City class
"""
from model_state import Base, State
from sqlalchemy import Integer, ForeignKey, Column, String


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
