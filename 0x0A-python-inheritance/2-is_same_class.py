#!/usr/bin/python3
""" Module defines function 'is_same_class' """


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.
    """
    #print(obj.__class__)
    #print(a_class.__class__)
    return True if obj.__class__ == a_class else False

