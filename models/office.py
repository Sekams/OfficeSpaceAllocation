from models.room import Room
class Office(Room):

	"""This class describes an instance of Office"""

	#This method takes two arguments in the order name, occupants(list of fellows and staff)
	def __init__(self, name, occupants):
		Room.__init__(self, 'office', name, len(occupants))
		self.occupants = occupants

	def get_occupants(self):
		return self.occupants