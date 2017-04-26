import unittest
import sys

sys.path.append('..')
from person import Person

class TestPerson(unittest.TestCase):

    """Test cases for the person class"""

    # Instantiating objects for using in the tests
    def setUp(self):
        self.tom_fellow = Person('Tom', 'Soyer', 'fellow', True)
        self.becky_staff = Person('Rebecca', 'Storm', 'staff', False)
        self.reagan_staff_acc = Person('Reagan', 'West', 'staff', True)

    # Test if the class creates an instance of itself
    def test_person_instance(self):
        self.assertIsInstance(self.tom_fellow, Person, msg='The object should be an instance of the `Person` class')

    # Test if the class creates a type of itself
    def test_type(self):
        self.assertTrue((type(self.becky_staff) is Person), msg='The object should be of type `Person`')

    # Test if the class assigns the right attributes to person instances
    def test_firstname_attribute(self):
        self.assertEqual('Tom', self.tom_fellow.first_name, msg='The person first_name attribute should be `Tom`')

    # Test if the class assigns the right attributes to person instances
    def test_lastname_attribute(self):
        self.assertEqual('Soyer', self.tom_fellow.last_name, msg='The person last_name attribute should be `Soyer`')

    # Test if the class the right attribute type
    def test_type_attribute(self):
        self.assertEqual(1, self.tom_fellow.type, msg='Tom should be a fellow')
        self.assertEqual(2, self.becky_staff.type, msg='Becky should be staff')
        self.assertEqual(2, self.reagan_staff_acc.type, msg='Reagan should be staff')

    # Test wants accomodation
    def test_wants_accomodation(self):
        self.assertTrue(self.tom_fellow.has_living_space, msg='Tom should get accomodation')
        self.assertFalse(self.becky_staff.has_living_space, msg='Becky should not get accomodation')
        self.assertFalse(self.reagan_staff_acc.has_living_space, msg='Reagan should not get accomodation')

    # Test if allocate_living_space method returns the right value for the given inputs
    def test_allocate_living_space(self):
        self.assertTrue(self.tom_fellow.allocate_living_space(), msg='Tom should get accomodation')
        self.assertFalse(self.becky_staff.allocate_living_space(), msg='Becky should not get accomodation')
        self.assertFalse(self.reagan_staff_acc.allocate_living_space(), msg='Reagan should not get accomodation')

    # Test if allocate_office method returns the right value for the given inputs
    def test_allocate_office(self):
        self.assertTrue(self.tom_fellow.allocate_office(), msg='Tom should get an office')
        self.assertTrue(self.becky_staff.allocate_office(), msg='Becky should get an office')
        self.assertTrue(self.reagan_staff_acc.allocate_office(), msg='Reagan should get an office')


if __name__ == "__main__":
    unittest.main()
