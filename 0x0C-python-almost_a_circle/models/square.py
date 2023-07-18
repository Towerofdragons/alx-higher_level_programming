#!/usr/bin/python3
"""
Module defines 'square' class.
"""


from models.rectangle import Rectangle
class Square(Rectangle):
    """
    Square inherits from Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        #self.size = size
        super().__init__(size, size, x, y, id)


