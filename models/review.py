#!/usr/bin/python3
"""Has the Review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Implements the model"""
    place_id = ""
    user_id = ""
    text = ""
