import unittest
import sys

sys.path.append('..')
from room import Room

class TestRoom(unittest.TestCase):

    """Test cases for the room class"""

    # Instantiating objects for using in the tests
    def setUp(self):
        self.blue_office = Room('Office', 'Blue')
        self.pink_living_space = Room('Living Space', 'Pink')

    # Test if the class creates an instance of itself
    def test_room_instance(self):
        self.assertIsInstance(self.blue_office, Room, msg='The object should be an instance of the `Room` class')

    # Test if the class creates a type of itself
    def test_type(self):
        self.assertTrue((type(self.pink_living_space) is Room), msg='The object should be of type `Room`')

    # Test if the class assigns the right attributes to office instances
    def test_office_attributes(self):
        self.assertEqual(6, self.blue_office.capacity, msg='The office room should have 6 spaces')

    # Test if the class assigns the right attributes to living space instances
    def test_living_space_attributes(self):
        self.assertEqual(4, self.pink_living_space.capacity, msg='The living space room should have 4 spaces')

    # Test if the class assigns the 0 occupied_spaces to a new room
    def test_spaces_attribute(self):
        self.assertEqual(0, self.pink_living_space.occupied_spaces, msg='The occupied_spaces for a new room should be 0')

    # Test if the get_vacant_spaces method returns the right value for the given inputs
    def test_vacant_spaces(self):
        self.assertEqual(6, self.blue_office.get_vacant_spaces(), msg='The class has to return 18')


if __name__ == "__main__":
    unittest.main()
