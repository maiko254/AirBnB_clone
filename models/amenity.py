#!/usr/bin/python3
""" implements class Amenity that inherits from BaseModel """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ handles all Amenity object instances """
    name = ""

    def __init__(self, *args, **kwargs):
        """ initializes Amenity object instance """
        super().__init__(*args, **kwargs)
