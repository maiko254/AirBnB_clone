""" tests for correct functionality of class User """
import unittest
from models.base_model import BaseModel
from models.user import User


class Test_User(unittest.TestCase):
    """ test cases for class User """
    def setUp(self):
        """ sets up initial User object instance """
        self.u1 = User()

    def test_Is_BaseModel_instance(self):
        """ test class User inherits from class BaseModel """
        self.assertIsInstance(self.u1, BaseModel)

    def test_attr_email(self):
        """ test class User has string attribute email """
        self.assertIs(hasattr(self.u1, "email"), True)
        self.assertIsInstance(self.u1.email, str)
    
    def test_attr_password(self):
        """ test class User has string attribute password """
        self.assertIs(hasattr(self.u1, "password"), True)
        self.assertIsInstance(self.u1.password, str)
    
    def test_attr_first_name(self):
        """ test class User has string attribute first_name """
        self.assertIs(hasattr(self.u1, "first_name"), True)
        self.assertIsInstance(self.u1.first_name, str)
    
    def test_attr_last_name(self):
        """ test class User has string attribute last_name """
        self.assertIs(hasattr(self.u1, "last_name"), True)
        self.assertIsInstance(self.u1.last_name, str)
