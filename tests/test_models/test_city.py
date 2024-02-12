""" tests functionality of class City """
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ test cases for class City """
    def setUp(self):
        """ sets up City object instance to be used in subsequent tests """
        self.c1 = City()

    def test_Is_Base_Model_instance(self):
        """ tests if City object instance inherits from BaseModel """
        self.assertIsInstance(self.c1, BaseModel)

    def test_attr_state_id(self):
        """ tests if City object instance has string attribute state_id """
        self.assertIs(hasattr(self.c1, "state_id"), True)
        self.assertIsInstance(self.c1.state_id, str)
