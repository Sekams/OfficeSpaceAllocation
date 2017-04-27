import unittest
from models.office import Office
from models.room import Room
from models.fellow import Fellow
from models.staff import Staff

class TestOffice(unittest.TestCase):

    """Test cases for the room class"""

    # Instantiating objects for using in the tests
    def setUp(self):
        self.tom_fellow = Fellow('Tom', 'Soyer', True)
        self.joe_staff = Staff('Joe', 'Swanson')
        self.becky_staff = Staff('Rebecca', 'Storm', 'The Office')
        self.occupants = {self.tom_fellow.first_name + ' ' + self.tom_fellow.last_name: self.tom_fellow,
                          self.joe_staff.first_name + ' ' + self.joe_staff.last_name: self.joe_staff,
                          self.becky_staff.first_name + ' ' + self.becky_staff.last_name: self.becky_staff}
        self.blue_office = Office('Blue Office', self.occupants)

    # Test if the class creates an instance of itself
    def test_office_instance(self):
        self.assertIsInstance(self.blue_office, Office, msg='The object should be an instance of the `Office` class')

    # Test if the class creates an instance of itself
    def test_room_instance(self):
        self.assertIsInstance(self.blue_office, Room, msg='The object should be an instance of the `Room` class')

    # Test if the class creates a type of itself
    def test_type(self):
        self.assertTrue((type(self.blue_office) is Office), msg='The object should be of type `Office`')

    # Test if the class assigns the right attributes to office instances
    def test_object_attributes(self):
        self.assertEqual('Blue Office', self.blue_office.name, msg='The object name should be `Blue Office`')

    # Test if the get_occupants method returns the right value for the given inputs
    def test_get_occupants(self):
        self.assertEqual(3, len(self.blue_office.get_occupants()), msg='The class has to return 3 occupants')


if __name__ == "__main__":
    unittest.main()
