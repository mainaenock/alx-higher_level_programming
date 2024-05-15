#!/usr/bin/python3
"""
base class
"""


import json


class Base:
    """
    new class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries:
        """
        if list_dictionaries is None:
            return "[]"

        else:
            return (json.dumps(list_dictionaries))


    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            return "[]"
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([obj.to_json_string() for obj in list_objs], file)
