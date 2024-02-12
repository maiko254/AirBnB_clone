#!/usr/bin/python3
""" handles file storage of object instances converted to JSON """
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review


class FileStorage():
    """
       serializes object instances to a JSON file and
       deserializes JSON file to object instances
    """
    __file_path = "file.json"
    __objects = {}

    classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
               "Place": Place, "State": State, "City": City, "Review": Review}

    def all(self):
        """ returns dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ add obj to __objects with key <obj class name>.id """
        FileStorage.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """ serializes __objects to a JSON file """
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """ deserializes a JSON file into an object instance """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                obj = json.load(f)
            for key in obj:
                self.__objects[key] = self.classes[obj[key]['__class__']](**obj[key])
