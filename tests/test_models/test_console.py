#!/usr/bin/python3

import unittest
from console import HBNBCommand
from models import storage
from io import StringIO
from unittest.mock import patch
import os


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HHBNCommand()

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_create_instance(self):
        """Test creating instances using create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show_instance(self):
        """Test showing instances using show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.cmd("create BaseModel")
            obj_id = f.getvalue().strip()


            self.console.onecmd("show BaseModel {}".format(obj_id))
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_destroy_instance(self):
        """Test destroying instances using destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 0)

    def test_all_instances(self):
        """Test retrieving all instances using all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

            self.console.onecmd("update BaseModel {} name 'New Name'".format(obj_id))
            self.console.onecmd("show BaseModel {}".format(obj_id))
            output = f.getvalue().strip()
            self.assertTrue("New Name" in output)

    def test_count_instances(self):
        """Test counting instances using count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(int(output) == 1)

    def test_quit_command(self):
        """Test quitting the console using quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_non_interactive_mode(self):
        with patch('sys.stdout', new=StringIO()) as f:
            os.system('echo "create BaseModel" | ./console.py')
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

if __name__ == '__main__':
    unittest.main()
