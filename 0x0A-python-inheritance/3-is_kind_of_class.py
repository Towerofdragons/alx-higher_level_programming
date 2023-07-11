#!/usr/biin/python3
"""
Module holds definition for funtion 'is_in_of_class'
"""

def is_kind_of_class(obj, a_class):
    """
     returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False
    """
    return True if isinstance(obj, a_class) else False
