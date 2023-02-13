#!/usr/bin/env python3
# file_storage.py
# Michael O Bonyo
"""Implements persistence through file storage"""


import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes an object instance to a JSON file and deserializes
    SON file to BaseModel instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """set in __objects obj with key <obj_class_name>.id

        Args:
            obj (BaseModel): object to add to dict __objects
        """
        clsname = obj.__class__.__name__
        self.__objects["{}.{}".format(clsname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(json_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects if file exists"""
        try:
            with open(self.__file_path) as f:
                json_dict = json.load(f)
                for v in json_dict.values():
                    cname = v["__class__"]
                    del v["__class__"]
                    self.new(eval(cname)(**v))
        except FileNotFoundError:
            return
