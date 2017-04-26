import unittest
from models.staff import Staff
from models.person import Person

class TestStaff(unittest.TestCase):

    """Test cases for the staff class"""

    # Instantiating objects for using in the tests
    def setUp(self):
        self.tom_staff = Staff('Tom', 'Soyer')
        self.becky_staff = Staff('Rebecca', 'Storm', 'The Office')

    # Test if the class creates an instance of itself
    def test_staff_instance(self):
        self.assertIsInstance(self.tom_staff, Staff, msg='The object should be an instance of the `Staff` class')
    
    # Test if the class creates an instance of Person
    def test_person_instance(self):
        self.assertIsInstance(self.becky_staff, Person, msg='The object should be an instance of the `Person` class')

    # Test if the class creates a type of itself
    def test_type(self):
        self.assertTrue((type(self.becky_staff) is Staff), msg='The object should be of type `Staff`')

    # Test if reallocate_living_space method returns the right value for the given inputs
    def test_reallocate(self):
        self.assertTrue(self.tom_staff.reallocate('Dope'), msg='Tom should  get a new office')
        self.assertEqual('Dope', self.tom_staff.office_name, msg='Tom should  get a new office')
        
if __name__ == "__main__":
    unittest.main()
