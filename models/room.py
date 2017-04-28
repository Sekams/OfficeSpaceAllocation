class Room(object):
    """This class describes an instance of Room"""

    # This method takes 2 required arguments in the order: the_type, name and an optional argument occupied spaces
    def __init__(self, the_type, name, occupied_spaces=0):
        # The type of the room is set as an integer where 1 = office and 2 = livingspace
        if the_type.lower() == 'office':
            self.type = 1
            self.capacity = 6
        elif the_type.lower() == 'livingspace' or the_type.lower() == 'living space':
            self.type = 2
            self.capacity = 4
        self.name = name
        self.occupied_spaces = occupied_spaces

    def get_vacant_spaces(self):
        result = self.capacity - self.occupied_spaces
        return result
