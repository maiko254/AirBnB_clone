#!/usr/bin/python3
""" command interpreter to manipulate object instances from the console """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """ implements commands of the interpreter """

    prompt = '(hbnb) '

    classes = ['BaseModel', 'User', 'Place', 'State',
               'Amenity', 'City', 'Review']

    def do_create(self, line):
        """ creats a new instance of BaseModel and save it to JSON file """
        if not line:
            print("** class doesn't exist **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            for cls_name in self.classes:
                if cls_name == line:
                    cls_obj = globals()[cls_name]
                    inst = cls_obj()
                    inst.save()
                    print(inst.id)

    def do_show(self, line):
        """
           Prints string representation of an instance based on
           the class name and id
        """
        if not line:
            print("** class name missing **")
            return
        arg = line.split()
        if arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1 and arg[0] in self.classes:
            print("** instance id missing **")
        elif arg[0]+"."+arg[1] not in models.storage.all().keys():
            print("** no instance found **")
        else:
            objs = models.storage.all()
            print(objs[f"{l[0]}.{l[1]}"].__str__())

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        if not line:
            print("** class name missing **")
            return
        arg = line.split()
        if arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == arg and arg[0] in self.classes:
            print("** instance id missing **")
        elif arg[0]+"."+arg[1] not in models.storage.all().keys():
            print("** no instance found **")
        else:
            models.storage.all().pop(f"{l[0]}.{l[1]}")
            models.storage.save()

    def do_all(self, line):
        """
           prints list of string representation of all instances based
           or not on the class name
        """
        if line and line not in self.classes:
            print("** class doesn't exist **")
        elif line:
            lstr = []
            for k, v in models.storage.all().items():
                if k.split('.')[0] == line:
                    lstr.append(v.__str__())
            print(lstr)
        else:
            lstr = []
            for v in models.storage.all().values():
                lstr.append(v.__str__())
            print(lstr)

    def do_update(self, line):
        """
          Updates an instance based on the class name and id by
          adding or updating attribute
        """
        if not line:
            print("** class name missing **")
            return

        arg = line.split()
        if arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1 and arg[0] in self.classes:
            print("** instance id missing **")
        elif arg[0]+"."+arg[1] not in models.storage.all().keys():
            print("** no instance found **")
        elif len(arg) == 2 and arg[0]+"."+arg[1] in models.storage.all().keys():
            print("** attribute name missing **")
        elif len(arg) == 3 and arg[0]+"."+arg[1] in models.storage.all().keys():
            print("** value missing **")
        else:
            key = arg[0]+"."+arg[1]
            name = arg[2]
            val = arg[3]
            obj = models.storage.all().get(key)
            setattr(obj, name, val)
            models.storage.save()

    def emptyline(self):
        """ emptyline is not executed """
        pass

    def do_quit(self, line):
        """ Quit command to exit the interpreter """
        return True

    def do_EOF(self, line):
        """ Quit the interpreter with Ctrl-D"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
