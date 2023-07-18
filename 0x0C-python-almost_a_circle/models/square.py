#!/usr/bin/python3
"""
Module defines class 'Square'
"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square inherits from class 'Rectangle'
    """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)
