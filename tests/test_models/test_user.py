#!/usr/bin/python3
# test_user.py
# Michael O Bonyo
"""Implements unit tests for class User"""

import unittest
from models.user import User
from models.base_model import BaseModel


class Test_User(unittest.TestCase):

    def test_instance_BaseModel(self):
        u = User()
        self.assertIsInstance(u, BaseModel)
    
    def test_instance_User(self):
        u = User()
        self.assertIsInstance(u, User)

    def test_attr_email(self):
        u = User()
        self.assertIn("email", u.__class__.__dict__.keys())
    
    def test_attr_passwd(self):
        u = User()
        self.assertIn("password", u.__class__.__dict__.keys())
    
    def test_attr_first_name(self):
        u = User()
        self.assertIn("first_name", u.__class__.__dict__.keys())
    
    def test_attr_last_name(self):
        u = User()
        self.assertIn("last_name", u.__class__.__dict__.keys())

    def test_email_isstr(self):
        u = User()
        self.assertIsInstance(u.email, str)
    
    def test_passwd_isstr(self):
        u = User()
        self.assertIsInstance(u.password, str)
    
    def test_first_name_isstr(self):
        u = User()
        self.assertIsInstance(u.first_name, str)
    
    def test_last_name_isstr(self):
        u = User()
        self.assertIsInstance(u.last_name, str)
