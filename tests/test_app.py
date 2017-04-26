import unittest
from app import app


class TestApp(unittest.TestCase):
    """Test cases for the functions in the app.py file"""

    # Test if the create_room function creates rooms when given input
    def test_create_room(self):
        app.create_room('office', 'The Think Tank')
        app.create_room('livingspace', 'The Man Cave')
        self.assertEqual(2, len(app.the_dojo.rooms),
                         msg='The function should create 2 rooms in the `the-dojo` instance')
