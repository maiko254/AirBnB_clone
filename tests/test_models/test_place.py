""" tests for correct functionality of class Place """
import unittest
from models.base_model import BaseModel
from models.place import Place


class Test_Place(unittest.TestCase):
    """ test cases for class Place """
    def setUp(self):
        """ sets up initial Place object instance """
        self.p1 = Place()

    def test_Is_BaseModel_instance(self):
        """ tests class Place inherits from BaseModel """
        self.assertIsInstance(self.p1, BaseModel)

    def test_attr_city_id(self):
        """ tests Place object instance has string attribute city_id """
        self.assertIs(hasattr(self.p1, "city_id"), True)
        self.assertIsInstance(self.p1.city_id, str)
    
    def test_attr_user_id(self):
        """ tests Place object instance has string attribute user_id """
        self.assertIs(hasattr(self.p1, "user_id"), True)
        self.assertIsInstance(self.p1.user_id, str)

    def test_attr_name(self):
        """ tests Place object instance has string attribute name """
        self.assertIs(hasattr(self.p1, "name"), True)
        self.assertIsInstance(self.p1.name, str)
        
    def test_attr_description(self):
        """ tests Place object instance has string attribute description """
        self.assertIs(hasattr(self.p1, "description"), True)
        self.assertIsInstance(self.p1.description, str)
    
    def test_attr_number_rooms(self):
        """ tests Place object instance has integer attribute number_rooms """
        self.assertIs(hasattr(self.p1, "number_rooms"), True)
        self.assertIsInstance(self.p1.number_rooms, int)
    
    def test_attr_number_bathrooms(self):
        """ tests Place object instance has integer attribute number_bathrooms """
        self.assertIs(hasattr(self.p1, "number_bathrooms"), True)
        self.assertIsInstance(self.p1.number_bathrooms, int)
    
    def test_attr_max_guest(self):
        """ tests Place object instance has integer attribute max_guest """
        self.assertIs(hasattr(self.p1, "max_guest"), True)
        self.assertIsInstance(self.p1.max_guest, int)
    
    def test_attr_price_by_night(self):
        """ tests Place object instance has integer attribute price_by_night """
        self.assertIs(hasattr(self.p1, "price_by_night"), True)
        self.assertIsInstance(self.p1.max_guest, int)

    def test_attr_latitude(self):
        """ tests Place object instance has float attribute latitude """
        self.assertIs(hasattr(self.p1, "latitude"), True)
        self.assertIsInstance(self.p1.latitude, float)
    
    def test_attr_longitude(self):
        """ tests Place object instance has float attribute longitude """
        self.assertIs(hasattr(self.p1, "longitude"), True)
        self.assertIsInstance(self.p1.longitude, float)
    
    def test_attr_amenity_ids(self):
        """ tests Place object instance has list attribute amenity_ids """
        self.assertIs(hasattr(self.p1, "amenity_ids"), True)
        self.assertIsInstance(self.p1.amenity_ids, list)
