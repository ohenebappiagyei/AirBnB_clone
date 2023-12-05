#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Define the hbnb command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Handle EOF character to quit the command interpreter."""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
