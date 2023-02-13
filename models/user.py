#!/usr/bin/env python3
# user.py
# Michael O Bonyo
"""Implements a User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """defines a user object and inherits rom BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
