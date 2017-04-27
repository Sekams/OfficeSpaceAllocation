class Dojo(object):
    
    """The class describes the structure of the Dojo object"""

    def __init__(self, *arguments):
        location = 'Nairobi'
        rooms = {}
        if arguments:
            location = arguments[0]
            if len(arguments) > 1:
                rooms = arguments[1]
        self.location = location
        self.rooms = rooms

    # This method returns a dictionary of vacant rooms in the Dojo object
    def get_vacant_rooms(self):
        result = {}
        if self.rooms:
            for room_name in self.rooms.keys():
                if self.rooms[room_name].capacity > self.rooms[room_name].occupied_spaces:
                    result[room_name] = self.rooms[room_name]
        return result
