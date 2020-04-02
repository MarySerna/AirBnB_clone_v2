#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    This is the class for user
    Attributes:
    email: email address
    password: password for you login
    first_name: first name
    last_name: last name
    """
    __tablename__ = "users"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
#        places = relationship("Place", backref="user", cascade="delete")
#        reviews = relationship("Review", backref="user", cascade="delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
