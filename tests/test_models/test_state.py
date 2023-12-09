#!/usr/bin/python3
"""Unittests for testing State class."""
import unittest
from models.state import State
from models import storage


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(State().name))

    def test_str_representation_no_name(self):
        state = State()
        state.id = "123456"
        state_str = state.__str__()
        self.assertIn("[State] (123456)", state_str)
        self.assertIn("'id': '123456'", state_str)
        self.assertNotIn("'name'", state_str)

    def test_str_representation_with_name(self):
        state = State()
        state.id = "123456"
        state.name = "State Name"
        state_str = state.__str__()
        self.assertIn("[State] (123456)", state_str)
        self.assertIn("'id': '123456'", state_str)
        self.assertIn("'name': 'State Name'", state_str)

    def test_to_dict_method_no_name(self):
        state = State()
        state.id = "123456"
        state_dict = state.to_dict()
        self.assertEqual(dict, type(state_dict))
        self.assertIn("id", state_dict)
        self.assertNotIn("name", state_dict)
        self.assertEqual("123456", state_dict["id"])
        self.assertEqual("State", state_dict["__class__"])

    def test_to_dict_method_with_name(self):
        state = State()
        state.id = "123456"
        state.name = "State Name"
        state_dict = state.to_dict()
        self.assertEqual(dict, type(state_dict))
        self.assertIn("id", state_dict)
        self.assertIn("name", state_dict)
        self.assertEqual("123456", state_dict["id"])
        self.assertEqual("State Name", state_dict["name"])
        self.assertEqual("State", state_dict["__class__"])

    def test_args_unused(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_save_method(self):
        state = State()
        initial_updated_at = state.updated_at
        state.save()
        self.assertLess(initial_updated_at, state.updated_at)

    def test_save_updates_file(self):
        state = State()
        state.save()
        state_id = "State." + state.id
        with open("file.json", "r") as f:
            self.assertIn(state_id, f.read())


if __name__ == "__main__":
    unittest.main()
