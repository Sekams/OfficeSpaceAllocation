import unittest
from app import app


class TestCreateRoom(unittest.TestCase):
    """Test cases for the create_room function"""

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


class TestAddPerson(unittest.TestCase):
    """Test cases for the add_person function"""

    # Test if the function adds a staff member to an office and not a livingspace
    def test_add_staff(self):
        initial_office_occupant_count = len(app.get_all_office_occupants())
        initial_livingspace_occupant_count = len(app.get_all_livingspace_occupants())
        app.add_person('Peter', 'Griffin', 'Staff')
        final_office_occupant_count = len(app.get_all_office_occupants())
        final_livingspace_occupant_count = len(app.get_all_livingspace_occupants())
        self.assertEqual(final_office_occupant_count - initial_office_occupant_count, 1,
                         msg='The function should add a member of staff to an office')
        self.assertEqual(initial_livingspace_occupant_count, final_livingspace_occupant_count,
                         msg='The function should not add a member of staff to a livingspace')

    # Test if the function adds a staff member wanting accomodation to an office and not a livingspace
    def test_add_staff_with_accomodation(self):
        initial_office_occupant_count = len(app.get_all_office_occupants())
        initial_livingspace_occupant_count = len(app.get_all_livingspace_occupants())
        app.add_person('Louis', 'Griffin', 'Staff', True)
        final_office_occupant_count = len(app.get_all_office_occupants())
        final_livingspace_occupant_count = len(app.get_all_livingspace_occupants())
        self.assertEqual(final_office_occupant_count - initial_office_occupant_count, 1,
                         msg='The function should add a member of staff to an office')
        self.assertEqual(initial_livingspace_occupant_count, final_livingspace_occupant_count,
                         msg='The function should not add a member of staff to a livingspace')

    # Test if the function adds a fellow who doesnt want accomodation to an office and not a livingspace
    def test_add_fellow(self):
        initial_office_occupant_count = len(app.get_all_office_occupants())
        initial_livingspace_occupant_count = len(app.get_all_livingspace_occupants())
        app.add_person('Stewie', 'Griffin', 'Fellow', False)
        final_office_occupant_count = len(app.get_all_office_occupants())
        final_livingspace_occupant_count = len(app.get_all_livingspace_occupants())
        self.assertEqual(final_office_occupant_count - initial_office_occupant_count, 1,
                         msg='The function should add a fellow to an office')
        self.assertEqual(initial_livingspace_occupant_count, final_livingspace_occupant_count,
                         msg='The function should not add a member of staff to a livingspace')

    # Test if the function adds a fellow who wants accomodation to an office and a livingspace
    def test_add_fellow_with_accomodation(self):
        initial_office_occupant_count = len(app.get_all_office_occupants())
        initial_livingspace_occupant_count = len(app.get_all_livingspace_occupants())
        app.add_person('Chris', 'Griffin', 'Fellow', True)
        final_office_occupant_count = len(app.get_all_office_occupants())
        final_livingspace_occupant_count = len(app.get_all_livingspace_occupants())
        self.assertEqual(final_office_occupant_count - initial_office_occupant_count, 1,
                         msg='The function should add a fellow to an office')
        self.assertEqual(final_livingspace_occupant_count - initial_livingspace_occupant_count, 1,
                         msg='The function should add a fellow to a livingspace')


