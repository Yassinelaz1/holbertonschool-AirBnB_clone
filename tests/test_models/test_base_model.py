#!/usr/bin/python3
"""Test for BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test environment"""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down test environment"""
        del self.model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """Test BaseModel attributes"""
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_types(self):
        """Test types of BaseModel attributes"""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """Test string representation of BaseModel"""
        string = str(self.model)
        self.assertIn("[BaseModel]", string)
        self.assertIn("'id':", string)
        self.assertIn("'created_at':", string)
        self.assertIn("'updated_at':", string)

    def test_save_method(self):
        """Test save method of BaseModel"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of BaseModel"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_create_new_instance_from_dict(self):
        """Test creating a new instance from dictionary"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)

    def test_save_reload(self):
        """Test saving and reloading from file"""
        self.model.save()
        new_model = BaseModel()
        new_model.reload()
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)


if __name__ == '__main__':
    unittest.main()
