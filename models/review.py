#!/usr/bin/python3
"""Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""