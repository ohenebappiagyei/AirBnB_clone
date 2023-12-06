#!/usr/bin/python3
"""Unittests for testing City class."""
import unittest
from models.city import City
import models


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_state_id_is_public_str(self):
        self.assertEqual(str, type(City().state_id))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(City().name))

    def test_str_representation_no_name(self):
        city = City()
        city.id = "123456"
        city.state_id = "state_1"
        city_str = city.__str__()
        self.assertIn("[City] (123456)", city_str)
        self.assertIn("'id': '123456'", city_str)
        self.assertIn("'state_id': 'state_1'", city_str)
        self.assertNotIn("'name'", city_str)

    def test_str_representation_with_name(self):
        city = City()
        city.id = "123456"
        city.state_id = "state_1"
        city.name = "City Name"
        city_str = city.__str__()
        self.assertIn("[City] (123456)", city_str)
        self.assertIn("'id': '123456'", city_str)
        self.assertIn("'state_id': 'state_1'", city_str)
        self.assertIn("'name': 'City Name'", city_str)

    def test_to_dict_method_no_name(self):
        city = City()
        city.id = "123456"
        city.state_id = "state_1"
        city_dict = city.to_dict()
        self.assertEqual(dict, type(city_dict))
        self.assertIn("id", city_dict)
        self.assertIn("state_id", city_dict)
        self.assertNotIn("name", city_dict)
        self.assertEqual("123456", city_dict["id"])
        self.assertEqual("state_1", city_dict["state_id"])
        self.assertEqual("City", city_dict["__class__"])

    def test_to_dict_method_with_name(self):
        city = City()
        city.id = "123456"
        city.state_id = "state_1"
        city.name = "City Name"
        city_dict = city.to_dict()
        self.assertEqual(dict, type(city_dict))
        self.assertIn("id", city_dict)
        self.assertIn("state_id", city_dict)
        self.assertIn("name", city_dict)
        self.assertEqual("123456", city_dict["id"])
        self.assertEqual("state_1", city_dict["state_id"])
        self.assertEqual("City Name", city_dict["name"])
        self.assertEqual("City", city_dict["__class__"])

    def test_args_unused(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())



if __name__ == "__main__":
    unittest.main()

