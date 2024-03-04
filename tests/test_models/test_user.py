import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up a user instance before each test."""
        self.user = User()

    def test_attributes(self):
        """Test if user instance has the correct attributes."""
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_initial_attributes(self):
        """Test if initial attributes are set correctly."""
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')

    def test_to_dict_method(self):
        """Test if to_dict method returns the expected dictionary."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], '')
        self.assertEqual(user_dict['password'], '')
        self.assertEqual(user_dict['first_name'], '')
        self.assertEqual(user_dict['last_name'], '')

    def test_str_representation(self):
        """Test if str method returns the expected string."""
        user_str = str(self.user)
        self.assertTrue('[User]' in user_str)
        self.assertTrue('id' in user_str)
        self.assertTrue('created_at' in user_str)
        self.assertTrue('updated_at' in user_str)
        self.assertTrue('email' in user_str)
        self.assertTrue('password' in user_str)
        self.assertTrue('first_name' in user_str)
        self.assertTrue('last_name' in user_str)

if __name__ == '__main__':
    unittest.main()
