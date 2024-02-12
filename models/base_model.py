#!/usr/bin/python3
""" Base class that defines common methods and attributes for other classes """
import uuid
from datetime import datetime
import models


class BaseModel():
    """ Defines common attributes and methods for other classes """
    def __init__(self, *args, **kwargs):
        """ initializes BaseModel instance """
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
            self.created_at = datetime.strptime(kwargs['created_at'],
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            u = uuid.uuid4()
            self.id = str(u)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ prints base model class description """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates updated_at attribute with the current time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
           returns a dictionary containing
           all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': self.__class__.__name__})
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
