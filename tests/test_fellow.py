import unittest
from models.fellow import Fellow
from models.person import Person

class TestFellow(unittest.TestCase):

    """Test cases for the fellow class"""

    # Instantiating objects for using in the tests
    def setUp(self):
        self.tom_fellow = Fellow('Tom', 'Soyer', True)
        self.becky_fellow = Fellow('Rebecca', 'Storm', False, 'The Office')
        self.reagan_fellow = Fellow('Reagan', 'West', True, 'The Office', 'The Pad')

    # Test if the class creates an instance of itself
    def test_fellow_instance(self):
        self.assertIsInstance(self.tom_fellow, Fellow, msg='The object should be an instance of the `Fellow` class')
    
    # Test if the class creates an instance of Person
    def test_person_instance(self):
        self.assertIsInstance(self.reagan_fellow, Person, msg='The object should be an instance of the `Person` class')

    # Test if the class creates a type of itself
    def test_type(self):
        self.assertTrue((type(self.becky_fellow) is Fellow), msg='The object should be of type `Fellow`')

    # Test if reallocate_living_space method returns the right value for the given inputs
    def test_allocate_living_space(self):
        self.assertTrue(self.tom_fellow.reallocate_living_space('The Man Cave'), msg='Tom should get a new living space')
        
    # Test if reallocate_office method returns the right value for the given inputs
    def test_allocate_office(self):
        self.assertTrue(self.tom_fellow.reallocate_office('The New Office'), msg='Tom should get a new office')
        
if __name__ == "__main__":
    unittest.main()
