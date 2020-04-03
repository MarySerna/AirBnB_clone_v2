#!/usr/bin/python3
"""test for state"""
import unittest
import os
import models
from models.state import State
from models.city import City
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """this will test the State class"""

    def test_pep8_conformance_state(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    def test_class(self):
        """ creates instance of State"""
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")


    def test_father(self):
        """ chacks if subclass"""
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_create_state(self):
        """ state is created in DB"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            value_a = len(models.storage.all("State"))
            my_state = State(name="Arizona")
            my_state.save()
            self.assertEqual(value_a + 1, len(models.storage.all("State")))

    def test_relation_state(self):
        """check relationship with City"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            my_state = State(name="California")
            my_state.save()
            city = City(name="San_Francisco", state_id=my_state.id)
            city.save()
            self.assertTrue(city.state == my_state)
            n_ins = len(models.storage.all("City"))
            models.storage.delete(city)
            self.assertEqual(n_ins - 1, len(models.storage.all("City")))

    def test_relation_getter(self):
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            my_state = State(name="California")
            my_state.save()
            city = City(name="San_Francisco", state_id=my_state.id)
            city.save()
            self.assertTrue(city in my_state.cities)


if __name__ == "__main__":
    unittest.main()
