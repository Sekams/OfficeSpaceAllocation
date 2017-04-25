class Dojo(object):
    def __init__(self, *arguments):
    	self.location = 'Nairobi'
    	if not not arguments:
    		self.location = arguments[0]
    		if len(arguments) > 1:
		        self.number_of_rooms = arguments[1]
    		if len(arguments) > 2:
		        self.occupied_rooms = arguments[2]

    def get_vacant_rooms(self):
        result = 0
        if not not self.number_of_rooms: 
            result = self.number_of_rooms - len(self.occupied_rooms)
        return result
