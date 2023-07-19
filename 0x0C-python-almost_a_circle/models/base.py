#!/usr/bin/python3
"""
This module defines: 'Base' class
"""


import json
class Base:
    """
    This class will be the “base” of all other classes in this project. 
    The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        json_list = []
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
         """Save JSON representation to file"""
         file_name = cls.__name__ + ".json"
         with open(file_name, "w") as file:
             if list_objs is None:
                 file.write("[]")
             else:
                 list_dicts = [obj.to_dictionary() for obj in list_objs]
                 file.write(Base.to_json_string(list_dicts))


    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representations"""
        json_list = []

        if json_string is not None and json_string != '':
           # if type(json_list) != str:
            #    raise TypeError("Input must be a JSON string")
            json_list = json.loads(json_string)

        return json_list

    @classmethod
    def create(cls, **dictionary):

        """ Returns a new object with settings from 'dictionary' """
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(1, 2)
        if cls.__name__ == "Square":
            dummy_obj = cls(1)
        dummy_obj.update(**dictionary)
        return dummy_obj

