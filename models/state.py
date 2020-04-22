#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
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
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

        @property
        def cities(self):
            cities_dict = models.storage.all(City)
            cities_list = []
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
    else:
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
