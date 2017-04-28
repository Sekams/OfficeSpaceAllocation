from models.person import Person


class Staff(Person):
    """This class describes an instance of Staff"""

    # This method takes 2 required arguments in the order first_name, last_name, office_name
    def __init__(self, first_name, last_name, office_name=''):
        Person.__init__(self, first_name, last_name, 'staff', False)
        self.office_name = office_name

    def reallocate(self, new_office_name):
        self.office_name = new_office_name
        if self.office_name == new_office_name:
            return True
        return False
