#!/usr/bin/env python3
# console.py
# Michael O Bonyo
"""Implements a command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """implements a commamnd interpreter using the cmd module"""

    prompt = "(hbnb) "

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
