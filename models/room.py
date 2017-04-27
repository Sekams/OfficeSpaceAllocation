class Room(object):
    """This class describes an instance of Room"""

    # This method takes an undefined number of arguments in the order type, name, occupied spaces
    # all of which are optional
    def __init__(self, *arguments):
        if arguments:
            # The type of the room is set as an integer where 1 = office and 2 = livingspace
            the_type = arguments[0]
            if the_type.lower() == 'office':
                self.type = 1
                self.capacity = 6
            elif the_type.lower() == 'livingspace' or the_type.lower() == 'living space':
                self.type = 2
                self.capacity = 4
            self.type = arguments[0]
        if len(arguments) > 1:
            self.name = arguments[1]
        if len(arguments) > 2:
            self.occupied_spaces = arguments[2]
        else:
            self.occupied_spaces = 0

    def get_vacant_spaces(self):
        result = self.capacity - self.occupied_spaces
        return result
