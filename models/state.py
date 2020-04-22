#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """
    This is the class for State
    Attributes:
    name: input name
    """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              cascade="all, delete",
                              backref="my_state")
    else:
        name = ""

    if os.environ.get('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            cities_dict = models.storage.all(City)
            cities_list = []
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
