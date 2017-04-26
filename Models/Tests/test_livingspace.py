import unittest
import sys

sys.path.append('..')
from living_space import LivingSpace
from fellow import Fellow

class TestLivingSpace(unittest.TestCase):

    """Test cases for the room class"""

    # Instantiating objects for using in the tests
    def setUp(self):
        self.tom_fellow = Fellow('Tom', 'Soyer', True)
        self.becky_fellow = Fellow('Rebecca', 'Storm', False, 'The Office')
        self.reagan_fellow = Fellow('Reagan', 'West', True, 'The Office', 'The Pad')
        self.fellows = [tom_fellow, becky_fellow, reagan_fellow]
        self.pink_living_space = LivingSpace('Pink Living Space', fellows)

    # Test if the class creates an instance of itself
    def test_living_space_instance(self):
        self.assertIsInstance(self.pink_living_space, LivingSpace, msg='The object should be an instance of the `LivingSpace` class')

    # Test if the class creates an instance of itself
    def test_room_instance(self):
        self.assertIsInstance(self.pink_living_space, Room, msg='The object should be an instance of the `Room` class')

    # Test if the class creates a type of itself
    def test_type(self):
        self.assertTrue((type(self.pink_living_space) is LivingSpace), msg='The object should be of type `LivingSpace`')

    # Test if the class assigns the right attributes to office instances
    def test_object_attributes(self):
        self.assertEqual('Pink Living Space', self.pink_living_space.name, msg='The object name should be `Pink Living Space`')

    # Test if the get_occupants method returns the right value for the given inputs
    def test_get_occupants(self):
        self.assertEqual(3, len(self.pink_living_space.get_occupants()), msg='The class has to return 3 occupants')


if __name__ == "__main__":
    unittest.main()
