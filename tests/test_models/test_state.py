import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_str_method(self):
        state = State()
        state.name = "California"
        self.assertEqual(str(state), "[State] ({}) {}".format(state.id, state.__dict__))

    def test_to_dict_method(self):
        state = State()
        state.name = "New York"
        state_dict = state.to_dict()
        self.assertEqual(state_dict['name'], "New York")
        self.assertEqual(state_dict['__class__'], 'State')

    def test_instance_creation(self):
        state = State(name="Texas")
        self.assertEqual(state.name, "Texas")


if __name__ == '__main__':
    unittest.main()
