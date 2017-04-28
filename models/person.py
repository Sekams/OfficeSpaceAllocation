class Person(object):
    """This class describes an instance of Person"""

    # This method takes 2 required arguments in the order; first_name, last_name and 2 optional arguments in the order;
    #  the_type, wants_accomodation
    def __init__(self, first_name, last_name, the_type='', wants_accomodation=False):
        self.first_name = first_name
        self.last_name = last_name
        # The type of the person is set as an integer where 1 = fellow and 2 = staff
        if the_type.lower() == 'fellow':
            self.type = 1
        elif the_type.lower() == 'staff':
            self.type = 2
            self.has_living_space = False
        if wants_accomodation and self.type == 1:
            self.allocate_living_space()

    def allocate_living_space(self):
        if self.type == 1:
            self.has_living_space = True
        return self.has_living_space

    def allocate_office(self):
        self.has_office = True
        return self.has_office
