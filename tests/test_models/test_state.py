""" tests correct functionality of class State """
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ test cases for class State """
    def setUp(self):
        """ set up State object instances to be used in subsequent tests """
        self.s1 = State()

    def test_Base_Model_Inheritance(self):
        """ tests if State object instance inherits from BaseModel """
        self.assertIsInstance(self.s1, BaseModel)

    def test_State_attr(self):
        """ tests if State object instance has attribute name and attr is str """
        self.assertIs(hasattr(self.s1, "name"), True)
        self.assertIsInstance(self.s1.name, str)
