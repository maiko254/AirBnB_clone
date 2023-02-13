#!/usr/bin/env python3
# review.py
# Michael O Bonyo
"""Implements the class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """defines Review class that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
