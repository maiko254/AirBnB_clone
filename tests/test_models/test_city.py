#!/usr/bin/env python3
# test_city.py
# Michael O Bonyo
"""Implements unit tests for class City"""

import unittest
from models.city import City
from models.base_model import BaseModel


class Test_City(unittest.TestCase):

    def test_instance_BaseModel(self):
        c = City()
        self.assertIsInstance(c, BaseModel)
    
    def test_instance_City(self):
        c = City()
        self.assertIsInstance(c, City)

    def test_has_state_id(self):
        c = City()
        self.assertIn("state_id", c.__class__.__dict__.keys())
    
    def test_has_state_id(self):
        c = City()
        self.assertIn("name", c.__class__.__dict__.keys())

    def test_state_id_isstr(self):
        c = City()
        self.assertIsInstance(c.state_id, str)
    
    def test_name_isstr(self):
        c = City()
        self.assertIsInstance(c.name, str)
