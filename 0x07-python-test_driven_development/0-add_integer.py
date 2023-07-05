#!/usr/bin/python3
""" This Module describes the add_integer function alone."""
def add_integer(a, b=98):
    """
    Add two integers and return the result.
    """
    if type(a) != float and type (a) != int:
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
