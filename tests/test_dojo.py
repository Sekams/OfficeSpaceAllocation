import unittest
from models.dojo import Dojo
from models.room import Room


class TestDojo(unittest.TestCase):
    
    """Test cases for the dojo class"""

    # Instantiating objects for using in the tests
    def setUp(self):
        self.blue_office = Room('Office', 'Blue')
        self.pink_living_space = Room('Living Space', 'Pink')
        self.rooms = [self.blue_office, self.pink_living_space]
        self.the_dojo = Dojo('Nairobi', self.rooms)
    
    # Test if the class creates an instance of itself
    def test_dojo_instance(self):
        self.assertIsInstance(self.the_dojo, Dojo, msg='The object should be an instance of the `Dojo` class')

    # Test if the class creates a type of itself
    def test_type(self):
        self.assertTrue((type(self.the_dojo) is Dojo), msg='The object should be of type `Dojo`')

    # Test if the class creates an accurate default model
    def test_default_model_for_dojo(self):
        default_dojo = Dojo()
        self.assertEqual('Nairobi', default_dojo.location, msg='The default location for the dojo should be `Nairobi`')

    # Test if the properties of the class are arranged in the proper order
    def test_dojo_properties(self):
        kampala = Dojo('Kampala', self.rooms)
        self.assertListEqual(['Kampala', 2], [kampala.location, len(kampala.rooms)],
                             msg='The location and rooms of the Dojo should be properties arranged '
                                 'respectively')

    # Test if the get_vacant_rooms method returns the right value for the given inputs
    def test_vacant_rooms(self):
    	self.assertEqual(2, len(self.the_dojo.get_vacant_rooms()), msg='The class has to return a list of 2 rooms')


if __name__ == "__main__":
    unittest.main()
