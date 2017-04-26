from models.person import Person
class Staff(Person):

    """This class describes an instance of Staff"""

    #This method takes an undefined number of arguments in the order first_name, last_name, office_name
    def __init__(self, *arguments):
        if arguments:
            first_name = arguments[0]
            last_name = ''
            if len(arguments) > 1:
                last_name = arguments[1]
            if len(arguments) > 2:
                self.office_name = arguments[2]
        Person.__init__(self, first_name, last_name, 'staff', False)

    def reallocate(self, new_office_name):
        self.office_name = new_office_name
        if self.office_name == new_office_name:
            return True
        return False