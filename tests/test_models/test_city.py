import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up a city instance before each test."""
        self.city = City()

    def test_attributes(self):
        """Test if city instance has the correct attributes."""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_initial_attributes(self):
        """Test if initial attributes are set correctly."""
        self.assertEqual(self.city.state_id, '')
        self.assertEqual(self.city.name, '')

    def test_to_dict_method(self):
        """Test if to_dict method returns the expected dictionary."""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['state_id'], '')
        self.assertEqual(city_dict['name'], '')

    def test_str_representation(self):
        """Test if str method returns the expected string."""
        city_str = str(self.city)
        self.assertTrue('[City]' in city_str)
        self.assertTrue('id' in city_str)
        self.assertTrue('created_at' in city_str)
        self.assertTrue('updated_at' in city_str)
        self.assertTrue('state_id' in city_str)
        self.assertTrue('name' in city_str)

if __name__ == '__main__':
    unittest.main()
