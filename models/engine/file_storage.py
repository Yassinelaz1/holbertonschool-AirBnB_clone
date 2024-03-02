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
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split(".")
                    module = __import__("models." + class_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
