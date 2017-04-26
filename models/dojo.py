class Dojo(object):
    """The class describes the structure of the Dojo object"""

    def __init__(self, *arguments):
        location = 'Nairobi'
        rooms = []
        if arguments:
            location = arguments[0]
            if len(arguments) > 1:
                rooms.extend(arguments[1])
        self.location = location
        self.rooms = rooms

    # This method returns a list of vacant rooms in the Dojo object
    def get_vacant_rooms(self):
        result = []
        if not not self.rooms:
            for a_room in self.rooms:
                if a_room.capacity > a_room.occupied_spaces:
                    result.append(a_room)
        return result
