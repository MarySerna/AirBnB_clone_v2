#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """
    This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places_amenities = relationship("Place",
                                        secondary='place_amenity')
        name = Column(String(128), nullable=False)
    else:
        name = ""
