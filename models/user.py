#!/usr/bin/python3
"""Implements the user's model"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    It inherits from the BaseModel class and adds the functionalities of the user.

    Args:
        email (str): the email of the user
        password (str): the password of the user
        first_name (str): the first name of the user
        last_name (str): the last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
