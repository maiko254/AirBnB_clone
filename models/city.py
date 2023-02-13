#!/usr/bin/env python3
# city.py
# Michael O Bonyo
"""Implements the class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """defines a city"""

    state_id = ""
    name = ""
