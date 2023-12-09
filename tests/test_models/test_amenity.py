#!/usr/bin/python3
"""Unittests for testing Amenity class."""
import unittest
from models.amenity import Amenity
from models import storage


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(Amenity().name))

    def test_str_representation_no_name(self):
        amenity = Amenity()
        amenity.id = "123456"
        amenity_str = amenity.__str__()
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertNotIn("'name'", amenity_str)

    def test_str_representation_with_name(self):
        amenity = Amenity()
        amenity.id = "123456"
        amenity.name = "Amenity Name"
        amenity_str = amenity.__str__()
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'name': 'Amenity Name'", amenity_str)

    def test_to_dict_method_no_name(self):
        amenity = Amenity()
        amenity.id = "123456"
        amenity_dict = amenity.to_dict()
        self.assertEqual(dict, type(amenity_dict))
        self.assertIn("id", amenity_dict)
        self.assertNotIn("name", amenity_dict)
        self.assertEqual("123456", amenity_dict["id"])
        self.assertEqual("Amenity", amenity_dict["__class__"])

    def test_to_dict_method_with_name(self):
        amenity = Amenity()
        amenity.id = "123456"
        amenity.name = "Amenity Name"
        amenity_dict = amenity.to_dict()
        self.assertEqual(dict, type(amenity_dict))
        self.assertIn("id", amenity_dict)
        self.assertIn("name", amenity_dict)
        self.assertEqual("123456", amenity_dict["id"])
        self.assertEqual("Amenity Name", amenity_dict["name"])
        self.assertEqual("Amenity", amenity_dict["__class__"])

    def test_args_unused(self):
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_save_method(self):
        amenity = Amenity()
        initial_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(initial_updated_at, amenity.updated_at)

    def test_save_updates_file(self):
        amenity = Amenity()
        amenity.save()
        amenity_id = "Amenity." + amenity.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


if __name__ == "__main__":
    unittest.main()
