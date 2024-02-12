#!/usr/bin/python3
""" implements user class that inherits from BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """ implements class User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ initializes user class """
        super().__init__(*args, **kwargs)
