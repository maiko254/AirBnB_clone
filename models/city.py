#!/usr/bin/python3
""" implement class City that inherits from class BaseModel """

from models.base_model import BaseModel


class City(BaseModel):
    """ handles all City object instances """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ initializes City object instance """
        super().__init__(*args, **kwargs)
