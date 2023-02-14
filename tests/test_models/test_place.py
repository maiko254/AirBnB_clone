#!/usr/bin/env python3
# test_place.py
# Michael O Bonyo
"""Implements unit tests for class Place"""


import unittest
from models.place import Place
from models.base_model import  BaseModel


class Test_Place(unittest.TestCase):

    def test_instance_BaseModel(self):
        p = Place()
        self.assertIsInstance(p, BaseModel)
    
    def test_instance_Place(self):
        p = Place()
        self.assertIsInstance(p, Place)

    def test_attr_city_id_isstr(self):
        p = Place()
        self.assertIsInstance(p.city_id, str)
    
    def test_attr_user_id_isstr(self):
        p = Place()
        self.assertIsInstance(p.user_id, str)
    
    def test_attr_name_isstr(self):
        p = Place()
        self.assertIsInstance(p.name, str)
    
    def test_attr_description_isstr(self):
        p = Place()
        self.assertIsInstance(p.description, str)

    def test_attr_number_rooms_isint(self):
        p = Place()
        self.assertIsInstance(p.number_rooms, int)
    
    def test_attr_number_bathrooms_isint(self):
        p = Place()
        self.assertIsInstance(p.number_bathrooms, int)
    
    def test_attr_max_guest_isint(self):
        p = Place()
        self.assertIsInstance(p.max_guest, int)
    
    def test_attr_price_by_night_isint(self):
        p = Place()
        self.assertIsInstance(p.price_by_night, int)

    def test_attr_latitude_isfloat(self):
        p = Place()
        self.assertIsInstance(p.latitude, float)
    
    def test_attr_longitude_isfloat(self):
        p = Place()
        self.assertIsInstance(p.longitude, float)

    def test_attr_amenity_ids_islist(self):
        p = Place()
        self.assertIsInstance(p.amenity_ids, list)
