#!/usr/bin/python3
"""
Module Defines function 'inherits_from'
"""

def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False
    """

    return True if (issubclass(obj.__class__, a_class) and obj.__class__ != a_class) else False
