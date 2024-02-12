""" tests correct functionality of class Review """
import unittest
from models.base_model import BaseModel
from models.review import Review


class Test_Review(unittest.TestCase):
    """ test cases for class Review """
    def setUp(self):
        """ sets up initial Review object instance """
        self.r1 = Review()

    def test_Is_BaseModel_instance(self):
        """ tests if class Review inherits from class BaseModel """
        self.assertIsInstance(self.r1, BaseModel)

    def test_attr_place_id(self):
        """ tests if class Review has string attribute place_id """
        self.assertIs(hasattr(self.r1, "place_id"), True)
        self.assertIsInstance(self.r1.place_id, str)
    
    def test_attr_user_id(self):
        """ tests if class Review has string attribute user_id """
        self.assertIs(hasattr(self.r1, "user_id"), True)
        self.assertIsInstance(self.r1.user_id, str)
    
    def test_attr_text(self):
        """ tests if class Review has string attribute text """
        self.assertIs(hasattr(self.r1, "text"), True)
        self.assertIsInstance(self.r1.text, str)
