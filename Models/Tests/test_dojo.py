import unittest
import sys

sys.path.append('..')
from dojo import Dojo


class TestDojo(unittest.TestCase):
    
    """Test cases for the dojo class"""
    
    # Test if the class creates an instance of itself
    def test_dojo_instance(self):
        the_dojo = Dojo('Nairobi', 10)
        self.assertIsInstance(the_dojo, Dojo, msg='The object should be an instance of the `Dojo` class')

    # Test if the class creates a type of itself
    def test_type(self):
        the_dojo = Dojo('Nairobi', 10)
        self.assertTrue((type(the_dojo) is Dojo), msg='The object should be of type `Dojo`')

    # Test if the class creates an accurate default model
    def test_default_model_for_dojo(self):
        default_dojo = Dojo()
        self.assertEqual('Nairobi', default_dojo.location, msg='The default location for the dojo should be `Nairobi`')

    # Test if the properties of the class are arranged in the proper order
    def test_dojo_properties(self):
        kampala = Dojo('Kampala', 20)
        self.assertListEqual(['Kampala', 20], [kampala.location, kampala.number_of_rooms],
                             msg='The location and number_of_rooms of the Dojo should be properties arranged '
                                 'respectively')

    # Test if the get_vacant_rooms method returns the right value for the given inputs
    def test_vacant_rooms(self):
    	a_dojo = Dojo('Nairobi', 20, ['Room 1', 'Room 4'])
    	self.assertEqual(18, a_dojo.get_vacant_rooms(), msg='The class has to return 18')


if __name__ == "__main__":
    unittest.main()
