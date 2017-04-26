from models.dojo import Dojo
from models.room import Room
from models.office import Office
from models.living_space import LivingSpace
from models.person import Person
from models.fellow import Fellow
from models.staff import Staff

the_dojo = Dojo('Nairobi')


def create_room(room_type, *room_name_arguments):
    if room_name_arguments:
        for room_name in room_name_arguments:
            new_room = Room(room_type, room_name)
            if new_room not in the_dojo.rooms:
                the_dojo.rooms.append(new_room)
                if new_room in the_dojo.rooms:
                    prefix = 'A'
                    if room_type.lower() == 'office':
                        prefix = 'An'
                    output = prefix + ' ' + room_type.lower() + ' called ' + room_name + 'has been successfully ' \
                                                                                         'created! '
                    # print(output)
