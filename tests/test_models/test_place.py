#!/usr/bin/python3
"""Unittests for testing Place class."""
import unittest
from models.place import Place
from models import storage


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_city_id_is_public_str(self):
        self.assertEqual(str, type(Place().city_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Place().user_id))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(Place().name))

    def test_description_is_public_str(self):
        self.assertEqual(str, type(Place().description))

    def test_number_rooms_is_public_int(self):
        self.assertEqual(int, type(Place().number_rooms))

    def test_max_guest_is_public_int(self):
        self.assertEqual(int, type(Place().max_guest))

    def test_price_by_night_is_public_int(self):
        self.assertEqual(int, type(Place().price_by_night))

    def test_latitude_is_public_float(self):
        self.assertEqual(float, type(Place().latitude))

    def test_longitude_is_public_float(self):
        self.assertEqual(float, type(Place().longitude))

    def test_amenity_ids_is_public_list(self):
        self.assertEqual(list, type(Place().amenity_ids))

    def test_str_representation_no_name(self):
        place = Place()
        place.id = "123456"
        place.city_id = "789"
        place.user_id = "101112"
        place_str = place.__str__()
        self.assertIn("[Place] (123456)", place_str)
        self.assertIn("'id': '123456'", place_str)
        self.assertIn("'city_id': '789'", place_str)
        self.assertIn("'user_id': '101112'", place_str)
        self.assertNotIn("'name'", place_str)

    def test_str_representation_with_name(self):
        place = Place()
        place.id = "123456"
        place.city_id = "789"
        place.user_id = "101112"
        place.name = "Place Name"
        place_str = place.__str__()
        self.assertIn("[Place] (123456)", place_str)
        self.assertIn("'id': '123456'", place_str)
        self.assertIn("'city_id': '789'", place_str)
        self.assertIn("'user_id': '101112'", place_str)
        self.assertIn("'name': 'Place Name'", place_str)

    def test_to_dict_method_no_name(self):
        place = Place()
        place.id = "123456"
        place.city_id = "789"
        place.user_id = "101112"
        place_dict = place.to_dict()
        self.assertEqual(dict, type(place_dict))
        self.assertIn("id", place_dict)
        self.assertIn("city_id", place_dict)
        self.assertIn("user_id", place_dict)
        self.assertNotIn("name", place_dict)
        self.assertEqual("123456", place_dict["id"])
        self.assertEqual("789", place_dict["city_id"])
        self.assertEqual("101112", place_dict["user_id"])
        self.assertEqual("Place", place_dict["__class__"])

    def test_to_dict_method_with_name(self):
        place = Place()
        place.id = "123456"
        place.city_id = "789"
        place.user_id = "101112"
        place.name = "Place Name"
        place_dict = place.to_dict()
        self.assertEqual(dict, type(place_dict))
        self.assertIn("id", place_dict)
        self.assertIn("city_id", place_dict)
        self.assertIn("user_id", place_dict)
        self.assertIn("name", place_dict)
        self.assertEqual("123456", place_dict["id"])
        self.assertEqual("789", place_dict["city_id"])
        self.assertEqual("101112", place_dict["user_id"])
        self.assertEqual("Place Name", place_dict["name"])
        self.assertEqual("Place", place_dict["__class__"])

    def test_args_unused(self):
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_save_method(self):
        place = Place()
        initial_updated_at = place.updated_at
        place.save()
        self.assertLess(initial_updated_at, place.updated_at)

    def test_save_updates_file(self):
        place = Place()
        place.save()
        place_id = "Place." + place.id
        with open("file.json", "r") as f:
            self.assertIn(place_id, f.read())


if __name__ == "__main__":
    unittest.main()
