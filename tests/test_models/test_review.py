#!/usr/bin/python3
"""Unittests for testing Review class."""
import unittest
from models.review import Review
from models import storage


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_place_id_is_public_str(self):
        self.assertEqual(str, type(Review().place_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Review().user_id))

    def test_text_is_public_str(self):
        self.assertEqual(str, type(Review().text))

    def test_str_representation_no_text(self):
        review = Review()
        review.id = "123456"
        review.place_id = "789"
        review.user_id = "101112"
        review_str = review.__str__()
        self.assertIn("[Review] (123456)", review_str)
        self.assertIn("'id': '123456'", review_str)
        self.assertIn("'place_id': '789'", review_str)
        self.assertIn("'user_id': '101112'", review_str)
        self.assertNotIn("'text'", review_str)

    def test_str_representation_with_text(self):
        review = Review()
        review.id = "123456"
        review.place_id = "789"
        review.user_id = "101112"
        review.text = "Review Text"
        review_str = review.__str__()
        self.assertIn("[Review] (123456)", review_str)
        self.assertIn("'id': '123456'", review_str)
        self.assertIn("'place_id': '789'", review_str)
        self.assertIn("'user_id': '101112'", review_str)
        self.assertIn("'text': 'Review Text'", review_str)

    def test_to_dict_method_no_text(self):
        review = Review()
        review.id = "123456"
        review.place_id = "789"
        review.user_id = "101112"
        review_dict = review.to_dict()
        self.assertEqual(dict, type(review_dict))
        self.assertIn("id", review_dict)
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertNotIn("text", review_dict)
        self.assertEqual("123456", review_dict["id"])
        self.assertEqual("789", review_dict["place_id"])
        self.assertEqual("101112", review_dict["user_id"])
        self.assertEqual("Review", review_dict["__class__"])

    def test_to_dict_method_with_text(self):
        review = Review()
        review.id = "123456"
        review.place_id = "789"
        review.user_id = "101112"
        review.text = "Review Text"
        review_dict = review.to_dict()
        self.assertEqual(dict, type(review_dict))
        self.assertIn("id", review_dict)
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)
        self.assertEqual("123456", review_dict["id"])
        self.assertEqual("789", review_dict["place_id"])
        self.assertEqual("101112", review_dict["user_id"])
        self.assertEqual("Review Text", review_dict["text"])
        self.assertEqual("Review", review_dict["__class__"])

    def test_args_unused(self):
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_save_method(self):
        review = Review()
        initial_updated_at = review.updated_at
        review.save()
        self.assertLess(initial_updated_at, review.updated_at)

    def test_save_updates_file(self):
        review = Review()
        review.save()
        review_id = "Review." + review.id
        with open("file.json", "r") as f:
            self.assertIn(review_id, f.read())


if __name__ == "__main__":
    unittest.main()
