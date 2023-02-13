#!/usr/bin/env python3
# console.py
# Michael O Bonyo
"""Implements a command interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models
import sys
from shlex import split


class HBNBCommand(cmd.Cmd):
    """implements a commamnd interpreter using the cmd module"""

    prompt = "(hbnb) "
    __classes = {"BaseModel", "User"}

    def do_create(self, line):
        """Creates a new BaseModel instance and saves it to a JSON file
        and prints the id"""
        command = self.parseline(line)[0]
        if command is None:
            print("** class name missing **")
        elif command not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_base = eval(command)()
            new_base.save()
            print(new_base.id)

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id"""

        command = self.parseline(line)[0]
        arg1 = self.parseline(line)[1]
        if command is None:
            print("** class name missing **")
        elif command not in self.__classes:
            print("** class doesn't exist **")
        elif arg1 == '':
            print("** instance id missing **")
        else:
            data = models.storage.all().get(command + '.' + arg1)
            if data is None:
                print("** no instance found **")
            else:
                print(data)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        command = self.parseline(line)[0]
        arg1 = self.parseline(line)[1]
        if command is None:
            print("** class name missing **")
        elif command not in self.__classes:
            print("** class doesn't exist **")
        elif arg1 == '':
            print("** instance id missing **")
        else:
            data = models.storage.all()[command + '.' + arg1]
            if data is None:
                print("** no instance found **")
            else:
                del models.storage.all()[command + '.' + arg1]
                models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        command = self.parseline(line)[0]
        if command not in self.__classes:
            print("** class doesn't exist **")
        else:
            data = models.storage.all()
            objlist = []
            for v in data.values():
                objlist.append(str(v))
            print(objlist)

    def do_update(self, line):
        """ Updates an instance based on the class name and id
        by adding or updating attribute"""
        args = split(line)
        arg_size = len(args)
        if arg_size == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif arg_size == 1:
            print("** instance id missing **")
        else:
            data = models.storage.all().get(args[0] + '.' + args[1])
            if data is None:
                print("** no instance found **")
            elif arg_size == 2:
                print("** attribute name missing **")
            elif arg_size == 3:
                try:
                    type(eval(arg[2])) != dict
                except NameError:
                    print("** value missing **")
            elif arg_size == 4:
                setattr(data, args[2], args[3])
                models.storage.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Won't repeat the last non-empty comman when an empty line
           is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
