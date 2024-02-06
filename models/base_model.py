#!/usr/bin/python3
""" Base class that defines common methods and attributes for other classes """
import uuid
from datetime import datetime

class BaseModel():
    """ Defines common attributes and methods for other classes """
    def __init__(self, id, created_at, updated_at):
        """ initializes BaseModel instance """
        u = uuid.uuid4()
        self.id = str(u)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ prints base model class description """
        print(f"[{self.__class__.name}] ({self.id}) {self.__dict__}")

    def save(self):
        """ updates updated_at attribute with the current time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ 
           returns a dictionary containing 
           all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__
        new_dict.update({'__class__': self.__class__.__name__})
        return new_dict
