#!/usr/bin/env python3
# test_state.py
# Michael O Bonyo
"""Implements unit tests for class State"""

import unittest
from models.state import State
from models.base_model import BaseModel


class Test_State(unittest.TestCase):

    def test_instance_BaseModel(self):
        s = State()
        self.assertIsInstance(s, BaseModel)
    
    def test_instance_State(self):
        s = State()
        self.assertIsInstance(s, State)

    def test_hasattr_name(self):
        s = State()
        self.assertIn("name", s.__class__.__dict__.keys())

    def test_attr_name_isstr(self):
        s = State()
        self.assertIsInstance(s.name, str)
