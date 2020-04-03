#!/usr/bin/python3
"""Test Place"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


type_storage = os.getenv("HBNB_TYPE_STORAGE", "fs")


class Testplace(unittest.TestCase):
    """ This is a test for checking place class """

    def test_pep8_conformance_place(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """ creates a place instance"""
        place1 = Place()
        self.assertEqual(place1.__class__.__name__, "Place")

    def test_father(self):
        """ checks if subclass"""
        place1 = Place()
        self.assertTrue(issubclass(place1.__class__, BaseModel))

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.new_instance = Place(city_id="1001", user_id="1002",
                                 name="The room", description="nice",
                                 number_rooms=1, number_bathrooms=1,
                                 max_guest=2, price_by_night=190,
                                 latitude=15.5, longitude=22.22)

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.new_instance

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_inheritance(self):
        """Tests inheritance"""
        self.assertIsInstance(self.new_instance, BaseModel)

    def test_pep8_Place(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_table_name(self):
        """
            Check the table name
        """
        self.assertEqual(self.new_instance.__tablename__, 'places')

    def test_attributes_Place(self):
        """chekcing if amenity have attributes"""
        self.assertTrue('id' in self.new_instance.__dict__)
        self.assertTrue('created_at' in self.new_instance.__dict__)
        self.assertTrue('updated_at' in self.new_instance.__dict__)
        self.assertTrue('city_id' in self.new_instance.__dict__)
        self.assertTrue('user_id' in self.new_instance.__dict__)
        self.assertTrue('name' in self.new_instance.__dict__)
        self.assertTrue('description' in self.new_instance.__dict__)
        self.assertTrue('number_rooms' in self.new_instance.__dict__)
        self.assertTrue('number_bathrooms' in self.new_instance.__dict__)
        self.assertTrue('max_guest' in self.new_instance.__dict__)
        self.assertTrue('price_by_night' in self.new_instance.__dict__)
        self.assertTrue('latitude' in self.new_instance.__dict__)
        self.assertTrue('longitude' in self.new_instance.__dict__)

    def test_is_subclass_Place(self):
        """test if Place is subclass of Basemodel"""
        self.assertTrue(issubclass(self.new_instance.__class__,
                                   BaseModel), True)

    def test_attribute_types_Place(self):
        """test attribute type for Place"""
        self.assertEqual(type(self.new_instance.user_id), str)
        self.assertEqual(type(self.new_instance.name), str)
        self.assertEqual(type(self.new_instance.description), str)
        self.assertEqual(type(self.new_instance.number_rooms), int)
        self.assertEqual(type(self.new_instance.number_bathrooms), int)
        self.assertEqual(type(self.new_instance.max_guest), int)
        self.assertEqual(type(self.new_instance.price_by_night), int)
        self.assertEqual(type(self.new_instance.latitude), float)
        self.assertEqual(type(self.new_instance.amenity_ids), list)

    @unittest.skipIf(type_storage == "db", "Testing database")
    def test_amenity_atr(self):
        self.assertTrue("amenity_ids" in self.new_instance.__dir__())

    @unittest.skipIf(type_storage != "db", "Testing database")
    def test_place_amenity_dbattrb(self):
        self.assertTrue("amenities" in self.new_instance.__dir__())
        self.assertTrue("reviews" in self.new_instance.__dir__())

    @unittest.skipIf(type_storage == "db", "Testing database")
    def test_type_latitude(self):
        '''
            Test the type of latitude
        '''
        latitude = getattr(self.new_instance, "latitude")
        self.assertIsInstance(latitude, float)

    @unittest.skipIf(type_storage == "db", "Testing database")
    def test_type_amenity(self):
        '''
            Test the type of latitude
        '''
        amenity = getattr(self.new_instance, "amenity_ids")
        self.assertIsInstance(amenity, list)

    @unittest.skipIf(type_storage == "db", "Testing database")
    def test_type_price_by_night(self):
        '''
            Test the type of price_by_night
        '''
        price_by_night = getattr(self.new_instance, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    @unittest.skipIf(type_storage == "db", "Testing database")
    def test_type_max_guest(self):
        '''
            Test the type of max_guest
        '''
        max_guest = getattr(self.new_instance, "max_guest")
        self.assertIsInstance(max_guest, int)

    @unittest.skipIf(type_storage == "db", "Testing database")
    def test_type_number_bathrooms(self):
        '''
            Test the type of number_bathrooms
        '''
        number_bathrooms = getattr(self.new_instance, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    @unittest.skipIf(type_storage == "db", "Testing database")
    def test_type_number_rooms(self):
        '''
            Test the type of number_bathrooms
        '''
        number_rooms = getattr(self.new_instance, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    @unittest.skipIf(type_storage == "db", "Testing database")
    def test_type_description(self):
        '''
            Test the type of description
        '''
        description = getattr(self.new_instance, "description")
        self.assertIsInstance(description, str)

    @unittest.skipIf(type_storage == "db", "Testing database")
    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_instance, "name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(type_storage == "db", "Testing database")
    def test_type_user_id(self):
        '''
            Test the type of user_id
        '''
        user_id = getattr(self.new_instance, "user_id")
        self.assertIsInstance(user_id, str)

    @unittest.skipIf(type_storage == "db", "Testing database")
    def test_type_city_id(self):
        '''
            Test the type of city_id
        '''
        city_id = getattr(self.new_instance, "city_id")
        self.assertIsInstance(city_id, str)
