#!/usr/bin/env python3
# base_model.py
# Michael O Bonyo
"""Implements a BaseModel class for the project"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel instance

        Args:
            args (tuple): contains all positional arguments
            kwargs (dict): contains all key worded arguments
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at":
                    self.created_at = datetime.fromisoformat(v)
                elif k == "updated_at":
                    self.updated_at = datetime.fromisoformat(v)
                elif k == "id":
                    self.id = v
        else:
            a = uuid.uuid4()
            self.id = str(a)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns string representation of BaseModel"""
        cname = self.__class__.__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of this instance"""
        new = self.__dict__
        for key, value in new.items():
            if key == "created_at":
                new[key] = value.isoformat()
            if key == "updated_at":
                new[key] = value.isoformat()

        new['__class__'] = self.__class__.__name__

        return new
