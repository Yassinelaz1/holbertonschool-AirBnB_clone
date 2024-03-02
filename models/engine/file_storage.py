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
        """Method to reload the objects from the file
            1.Check if the file exists
            2.Open the JSON file in read mode with utf-8 encoding
            3.Try to load the objects from the file
            4.Iterate through each key-value pair in the loaded dictionary
            5.plit the key into class name and object ID
            6.Get the class from the class name
            7.Instantiate the class with the loaded attributes
            8.Add the instantiated object to the __objects dictionary
            9.Print the error message if there is an exception   
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    dic_obj = json.load(file)

                    for key, value in dic_obj.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
