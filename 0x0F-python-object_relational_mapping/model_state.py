#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    __tablename__ (str): class names
    id (int): State id 
    name (str): State name 
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    id = Column(Integer, primary_key=True)
