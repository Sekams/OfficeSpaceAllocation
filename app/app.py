import random
from models.dojo import Dojo
from models.room import Room
from models.office import Office
from models.living_space import LivingSpace
from models.person import Person
from models.fellow import Fellow
from models.staff import Staff

the_dojo = Dojo('Nairobi')
total_number_of_rooms = 100


def get_all_office_occupants():
    all_office_occupants = []
    if the_dojo.rooms:
        for room in [a_room for a_room in the_dojo.get_vacant_rooms().values() if isinstance(a_room, Office)]:
            all_office_occupants.extend(room.occupants.keys())
    return all_office_occupants


def get_all_livingspace_occupants():
    all_livingspace_occupants = []
    if the_dojo.rooms:
        for room in [a_room for a_room in the_dojo.get_vacant_rooms().values() if isinstance(a_room, LivingSpace)]:
            all_livingspace_occupants.extend(room.occupants.keys())
    return all_livingspace_occupants


def create_room(room_type, *room_name_arguments):
    output = ''
    if room_name_arguments and room_type:
        for room_name in room_name_arguments:
            if room_name not in the_dojo.rooms.keys():
                new_room = Room(room_type, room_name)
                if room_type.lower() == 'office':
                    new_room = Office(room_name, {})
                elif room_type.replace(' ', '').lower() == 'livingspace':
                    new_room = LivingSpace(room_name, {})
                if len(the_dojo.rooms) <= total_number_of_rooms and room_name not in the_dojo.rooms.keys() and (
                            isinstance(new_room, Office) or isinstance(new_room, LivingSpace)):
                    the_dojo.rooms[room_name] = new_room
                    if room_name in the_dojo.rooms.keys():
                        prefix = 'A'
                        if room_type.lower() == 'office':
                            prefix = 'An'
                        output += prefix + ' ' + room_type.lower() + ' called ' + room_name + " has been successfully created! \n"

    return output


def add_person(first_name, last_name, person_type, wants_accomodation=False):
    name = first_name + ' ' + last_name
    if name and person_type:
        if name and name not in get_all_office_occupants():
            output = ''
            if not [a_room for a_room in the_dojo.get_vacant_rooms().values() if isinstance(a_room, Office)]:
                initial_room_count = len(the_dojo.rooms)
                final_room_count = 0
                while initial_room_count >= final_room_count:
                    appendix = random.choice(range(0, total_number_of_rooms + 1))
                    create_room('office', 'Office ' + str(appendix))
                    final_room_count = len(the_dojo.rooms)

            an_office = random.choice(
                [a_room for a_room in the_dojo.get_vacant_rooms().values() if isinstance(a_room, Office)])
            if person_type.lower() == 'fellow':
                if not wants_accomodation and name not in get_all_office_occupants():
                    a_fellow = Fellow(first_name, last_name, wants_accomodation, an_office.name)
                    an_office.occupants[name] = a_fellow

                    if name in get_all_office_occupants():
                        output += 'Fellow ' + name + ' has been successfully added. \n ' + \
                        first_name + ' has been assigned the office ' + an_office.name
                elif wants_accomodation and name not in get_all_livingspace_occupants() and name not in get_all_office_occupants():
                    if not [a_room for a_room in the_dojo.get_vacant_rooms().values() if isinstance(a_room, LivingSpace)]:
                        initial_room_count = len(the_dojo.rooms)
                        final_room_count = 0
                        while initial_room_count >= final_room_count:
                            appendix = random.choice(range(0, total_number_of_rooms + 1))
                            create_room('livingspace', 'Livingspace ' + str(appendix))
                            final_room_count = len(the_dojo.rooms)

                    a_livingspace = random.choice(
                        [a_room for a_room in the_dojo.get_vacant_rooms().values() if isinstance(a_room, LivingSpace)])
                    a_fellow = Fellow(first_name, last_name, wants_accomodation, an_office.name, a_livingspace.name)
                    a_livingspace.occupants[name] = a_fellow
                    an_office.occupants[name] = a_fellow
                    if name in get_all_office_occupants() and name in get_all_livingspace_occupants():
                        output += 'Fellow ' + name + ' has been successfully added. \n ' + \
                                  first_name + ' has been assigned the office ' + an_office.name + '\n' + \
                                  first_name + ' has been assigned the livingspace ' + a_livingspace.name

            elif person_type.lower() == 'staff':
                a_staff = Staff(first_name, last_name, an_office.name)
                an_office.occupants[name] = a_staff
                if name in get_all_office_occupants():
                    output += 'Staff ' + name + ' has been successfully added. \n ' + \
                              first_name + ' has been assigned the office ' + an_office.name
            return output


