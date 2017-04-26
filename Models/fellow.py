from person import Person
class Fellow(Person):

    """This class describes an instance of Fellow"""

    #This method takes an undefined number of arguments in the order first_name, last_name, wants_accomodation,
    #office_name, living_space_name all of which are optional
    def __init__(self, *arguments):
        if arguments:
            first_name = arguments[0]
            last_name = ''
            wants_accomodation = False
            if len(arguments) > 1:
                last_name = arguments[1]
            if len(arguments) > 2:
                wants_accomodation = arguments[2]
            if len(arguments) > 3:
                self.office_name =  arguments[3]
            if len(arguments) > 4:
                self.living_space_name = arguments[4]
        Person.__init__(self, first_name, last_name, 'fellow', wants_accomodation)

    def reallocate_office(self, new_office_name):
        self.office_name = new_office_name
        if self.office_name == new_office_name:
            return True
        return False

    def reallocate_living_space(self, new_living_space_name):
        self.living_space_name = new_living_space_name
        if self.living_space_name == new_living_space_name:
            return True
        return False
