#!/usr/bin/python3
""" A Ajouter """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=mymetadata)

class State(Base):
    """desc"""
    __tablenam__ = 'state'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)