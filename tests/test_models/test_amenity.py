#!/usr/bin/env python3
# test_amenity.py
# Michael Odhiambo Bonyo
"""Implements unit tests for class Amenity"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Amenity(unittest.TestCase):
    """defines unit tests for class Amenity"""

    def test_instance_BaseModel(self):
        a = Amenity()
        self.assertIsInstance(a, BaseModel)
    
    def test_instance_Amenity(self):
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_attr_str(self):
        a = Amenity()
        self.assertIsInstance(a.name, str)

    def test_attr_name_isempty(self):
        a = Amenity()
        self.assertEqual(a.name, "")
