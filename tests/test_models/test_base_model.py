#!/usr/bin/env python3
# test_base_model.py
# Michael O Bonyo
"""Implements unit tests for class BaseModel"""

import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime



class Test_Base_Model(unittest.TestCase):

    def test_uuid_str(self):
        b = BaseModel()
        self.assertIsInstance(b.id, str)
    
    def test_uuid_uuid(self):
        b = BaseModel()
        self.assertIsInstance(uuid.UUID(b.id), uuid.UUID)

    def test_unique_uuid(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_to_dict(self):
        b = BaseModel()
        self.assertIsInstance(b.to_dict(), dict)

    def test_attr(self):
        b = BaseModel()
        keys = b.to_dict()
        self.assertIn('id', keys.keys())
        self.assertIn('created_at', keys.keys())
        self.assertIn('updated_at', keys.keys())

    def test_created_at_type(self):
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime)

    def test_updated_at_type(self):
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime)

    def test_instance_type(self):
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
