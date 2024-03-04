#!/usr/bin/python3
"""
File Storage
"""

import json
from os.path import isfile
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method to retrieve all objects from the storage
        1.Return the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """ Method to add a new object to the storage
        1.Generate a unique key for the object
        2.Add the object to the storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Method to save the objects to a file:
        1.Retrieve all objects from the storage
        2.Initialize an empty dictionary to store the objects as dictionaries
        3.Iterate through all objects
        4.Convert the object to a dictionary
        5.Open the file in write mode with utf-8 encoding
        6.Write the objects dictionary as a JSON object to the file
        """
        objects = self.__objects
        dic_data = {}
        for obj in objects.keys():
            dic_data[obj] = objects[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(dic_data, file)

    def reload(self):
        """reload the saved objects from a JSON file.
        1.Open the JSON file with the saved objects and read its contents.
        2.Load the JSON contents into a Python dictionary.
        3.Iterate over the dictionary's items,
                    which represent the saved objects.
        4.Dynamically create a new instance of the corresponding
                    class based on the saved object's class name.
        5.Add the new instance to the self.__objects dictionary,
                    using the original key.
        6.If the file does not exist, no action is taken.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        try:
            with open(self.__file_path, "r", encoding="UTF8") as f:
                for key, value in json.load(f).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass
