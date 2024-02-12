#!/usr/bin/python3
""" implements class State that inherits from class BaseModel """

from models.base_model import BaseModel


class State(BaseModel):
    """ Handles all State object instances """
    name = ""

    def __init__(self, *args, **kwargs):
        """ initializes user object instance """
        super().__init__(*args, **kwargs)
