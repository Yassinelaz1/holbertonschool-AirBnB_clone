import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up an amenity instance before each test."""
        self.amenity = Amenity()

    def test_attributes(self):
        """Test if amenity instance has the correct attributes."""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_initial_attributes(self):
        """Test if initial attributes are set correctly."""
        self.assertEqual(self.amenity.name, '')

    def test_to_dict_method(self):
        """Test if to_dict method returns the expected dictionary."""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], '')

    def test_str_representation(self):
        """Test if str method returns the expected string."""
        amenity_str = str(self.amenity)
        self.assertTrue('[Amenity]' in amenity_str)
        self.assertTrue('id' in amenity_str)
        self.assertTrue('created_at' in amenity_str)
        self.assertTrue('updated_at' in amenity_str)
        self.assertTrue('name' in amenity_str)

if __name__ == '__main__':
    unittest.main()