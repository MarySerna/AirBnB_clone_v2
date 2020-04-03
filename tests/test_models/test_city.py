#!/usr/bin/python3
"""Test City"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
import models

class Testcity(unittest.TestCase):
    """ unittest for City class"""
    def test_pep8_conformance_city(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """ creates City instance"""
        city1 = City()
        self.assertEqual(city1.__class__.__name__, "City")

    def test_father(self):
        """ checks if subclass"""
        city1 = City()
        self.assertTrue(issubclass(city1.__class__, BaseModel))

    def test_relation_db(self):
        """ Check relation """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            my_state = State(name="California")
            my_state.save()
            city = City(name="Arizona", state_id=my_state.id)
            city.save()
            self.assertTrue(city.state == my_state)

    def test_create_db(self):
        """ check create obj"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            value_a = len(models.storage.all("City"))
            my_state = State(name="California")
            my_state.save()
            my_city = City(name="Arizona", state_id=my_state.id)
            my_city.save()
            self.assertEqual(value_a + 1, len(models.storage.all("City")))
            models.storage.delete(my_city)
            self.assertEqual(value_a, len(models.storage.all("City")))
