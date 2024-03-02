#!/usr/bin/python3
"""
File Storage
"""

import json
from os.path import isfile


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
        """ Method to reload the objects from the file
            1. Check if the file exists
            2. If it exists, open the file in read mode with utf-8 encoding
            3. Load the objects from the file
            4. Iterate through the loaded objects
            5. Convert the object to its original class
            6. Store the object in the storage dictionary"""
        if isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                _load = json.load(file)
                for key, value in _load.items():
                    class_name, class_id = key.split(".")
                    obj_class = eval(class_name)
                    self.__objects[key] = obj_class(**value)
