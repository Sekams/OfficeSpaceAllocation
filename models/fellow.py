from models.person import Person


class Fellow(Person):
    """This class describes an instance of Fellow"""

    # This method takes 2 required arguments in the order; first_name, last_name and 3 optional arguments in the
    # order; wants_accomodation, office_name, living_space_name
    def __init__(self, first_name, last_name, wants_accomodation=False, office_name='', living_space_name=''):
        Person.__init__(self, first_name, last_name, 'fellow', wants_accomodation)
        self.office_name = office_name
        self.living_space_name = living_space_name

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
