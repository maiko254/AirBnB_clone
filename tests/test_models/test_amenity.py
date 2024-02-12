""" tests functionality of class Amenity """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ test cases for class Amenity """
    def setUp(self):
        """ sets up initial Amenity object instance """
        self.a1 = Amenity()

    def test_Is_BaseModel_instance(self):
        """ test if class Amenity inherits from class BaseModel """
        self.assertIsInstance(self.a1, BaseModel)

    def test_attr_name(self):
        """ test if class Amenity has string attribute name """
        self.assertIs(hasattr(self.a1, "name"), True)
        self.assertIsInstance(self.a1.name, str)
