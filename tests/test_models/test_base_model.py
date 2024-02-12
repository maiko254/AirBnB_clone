""" test cases for BaseModel class """
from models.base_model import BaseModel
import unittest
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """ Tests for BaseModel instances """
    def setUp(self):
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_created_at_attr(self):
        """ test created_at attribute is datetime object """
        self.assertIsInstance(self.b1.created_at, datetime)
    
    def test_updated_at_attr(self):
        """ test updated_at attribute is datetime object """
        self.assertIsInstance(self.b1.updated_at, datetime)

    def test_save_method(self):
        """ test save instance method updates update_at attr """
        oldtime = self.b2.updated_at
        self.b2.save()
        newtime = self.b2.updated_at
        self.assertNotEqual(oldtime, newtime)

    def test_to_dict(self):
        """ test to_dict method returns a dictionary """
        self.assertIsInstance(self.b2.to_dict(), dict)

    def test_UUID_instance(self):
        """ test attribute id is uuid string """
        self.assertIsInstance(self.b1.id, str)

    def testUUID(self):
        """ test unique id for each class instance """
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_BaseModel_creation(self):
        """ test creation of new instance of BaseModel """
        self.assertIsInstance(self.b1, BaseModel)

    def test_BaseModel_from_dict(self):
        """ test BaseModel instance is recreated from dict and also with empty dict """
        d = {'id': 'f9ba9bb2-7149-4c44-b349-0ae0cc9cf8f7', 'created_at': '2024-02-07T11:34:15.133029', 'updated_at': '2024-02-07T11:34:15.133305', 'name': 'My_First_Model', 'my_number': 89, '__class__': 'BaseModel'}
        emptydict = {}
        b3 = BaseModel(**d)
        b4 = BaseModel(**emptydict)
        self.assertIsInstance(b3, BaseModel)
        self.assertIsInstance(b4, BaseModel)
        self.assertIs(hasattr(b3, "id"), True)
        self.assertIs(hasattr(b3, "created_at"), True)
        self.assertIs(hasattr(b3, "updated_at"), True)
        self.assertIs(hasattr(b4, "id"), True)
        self.assertIs(hasattr(b4, "created_at"), True)
        self.assertIs(hasattr(b4, "updated_at"), True)
