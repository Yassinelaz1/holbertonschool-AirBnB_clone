#!/usr/bin/python3
"""Unit tests for Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_attributes(self):
        """Test instantiation with attributes"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_attribute_types(self):
        """Test attribute types"""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_empty_string_attributes(self):
        """Test instantiation with empty string attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_str_method(self):
        """Test __str__ method"""
        review = Review()
        string = str(review)
        self.assertIn("[Review]", string)
        self.assertIn("'id':", string)
        self.assertIn("'created_at':", string)
        self.assertIn("'updated_at':", string)

    def test_to_dict_method(self):
        """Test to_dict method"""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], review.place_id)
        self.assertEqual(review_dict['user_id'], review.user_id)
        self.assertEqual(review_dict['text'], review.text)


if __name__ == '__main__':
    unittest.main()
