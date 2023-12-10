#!/usr/bin/python3
"""
This module defines the HBNBCommand class for the command interpreter.
"""


import cmd
from models import storage
from models.base_model import BaseModel
import shlex
import json


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print("")
        return True

    def emptyline(self):
        """
        Empty line + Enter shouldn't execute anything
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing ***")
        elif arg not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in storage.all():
                print(storage.all()[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in storage.all():
                del storage.all()[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        args = arg.split()
        if args and args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            print([str(instances[key]) for key in instances])

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            instance = storage.all()["{}.{}".format(args[0], args[1])]
            setattr(instance, args[2], eval(args[3]))
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
