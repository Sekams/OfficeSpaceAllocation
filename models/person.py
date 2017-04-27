class Person(object):
    """This class describes an instance of Person"""

    # This method takes an undefined number of arguments in the order first_name, last_name, type, wants_accomodation
    # all of which are optional
    def __init__(self, *arguments):
        if arguments:
            self.first_name = arguments[0]
            if len(arguments) > 0:
                self.last_name = arguments[1]
            if len(arguments) > 1:
                # The type of the person is set as an integer where 1 = fellow and 2 = staff
                the_type = arguments[2]
                if the_type.lower() == 'fellow':
                    self.type = 1
                elif the_type.lower() == 'staff':
                    self.type = 2
                    self.has_living_space = False
            if len(arguments) > 2:
                wants_accomodation = arguments[3]
                if wants_accomodation and self.type == 1:
                    self.allocate_living_space()

    def allocate_living_space(self):
        if self.type == 1:
            self.has_living_space = True
        return self.has_living_space

    def allocate_office(self):
        self.has_office = True
        return self.has_office
