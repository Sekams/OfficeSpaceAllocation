import unittest
from app import app


class TestApp(unittest.TestCase):
    """Test cases for the functions in the app.py file"""

    # Test if the create_room function creates rooms when given input
    def test_create_room(self):
        room_count_before = len(app.the_dojo.rooms)
        app.create_room('office', 'The Think Tank')
        app.create_room('livingspace', 'The Man Cave')
        room_count_after = len(app.the_dojo.rooms)
        self.assertEqual(2, room_count_after - room_count_before,
                         msg='The function should create 2 rooms in the `the-dojo` instance')

    # Test if the create_room function creates multiple rooms in one call
    def test_create_room_multiple_rooms(self):
        room_count_before = len(app.the_dojo.rooms)
        app.create_room('office', 'Round', 'Square')
        room_count_after = len(app.the_dojo.rooms)
        self.assertEqual(2, room_count_after - room_count_before,
                         msg='The function should create 2 rooms in the `the-dojo` instance')

    # Test if create_room function does not create rooms when inputs are invalid
    def test_create_room_invalid_inputs(self):
        room_count_before = len(app.the_dojo.rooms)
        app.create_room('book', 'Round', 'Square')
        room_count_after = len(app.the_dojo.rooms)
        self.assertEqual(room_count_after, room_count_before,
                         msg='The function should not create any room in the `the-dojo` instance')

    # Test if create_room function does not create rooms when inputs are inadequate
    def test_create_room_inadequate_inputs(self):
        room_count_before = len(app.the_dojo.rooms)
        app.create_room('office')
        room_count_after = len(app.the_dojo.rooms)
        self.assertEqual(room_count_after, room_count_before,
                         msg='The function should not create any room in the `the-dojo` instance')
