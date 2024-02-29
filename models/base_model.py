#!/usr/bin/python3
"""
module documentation
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel is a class that provides a basic structure for other models in the application.
    It includes attributes for id, created_at, and updated_at.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor method for BaseModel.
        Initializes instance attributes.
        """
        time_f = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key,value in kwargs.items():
                if key not in ["__class__", "created_at", "updated_at"]:
                    setattr(self, key, value)
                if key in {"created_at", "updated_at"}:
                    setattr(self, key, datetime.strptime(value, time_f))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """
        String representation method for BaseModel.
        Returns a printable representation of the object.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save method for BaseModel.
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.utcnow()
        

    def to_dict(self):
        """
        To dictionary method for BaseModel.
        Converts the object's attributes to a dictionary.
        """
        instance_dic = self.__dict__.copy()
        instance_dic["__class__"] = self.__class__.__name__
        instance_dic["created_at"] = self.created_at.isoformat()
        instance_dic["updated_at"] = self.updated_at.isoformat()
        return instance_dic
