from room import Room
class LivingSpace(Room):

	"""This class describes an instance of LivingSpace"""

	#This method takes two arguments in the order name, occupants(list of fellows)
	def __init__(self, name, occupants):
		Room.__init__(self, 'living space', name, len(occupants))
		self.occupants = occupants

	def get_occupants(self):
		return self.occupants