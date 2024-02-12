#!/usr/bin/python3
""" implements class Review that inherits from BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """ handles all Review object instances """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ initializes a Review object instance """
        super().__init__(*args, **kwargs)
