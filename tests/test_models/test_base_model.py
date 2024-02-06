#!/usr/bin/python3
""" test cases for BaseModel class """
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    """ Tests for BaseModel instances """
    def setUp(self):
        b1 = BaseModel()
        b2 = BaseModel()

    def testUUID(self):
        self.assertNotEqual(b1.id, b2.id)
