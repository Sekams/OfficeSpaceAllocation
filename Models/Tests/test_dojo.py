import unittest
import sys 

sys.path.append('..')
from dojo import Dojo

class TestDojo(unittest.TestCase):
	"""
		Test cases for the dojo class
	"""

	#Test if the class creates an instance of itself
	def test_dojo_instance(self):
		the_dojo = Dojo({'location' : 'Nairobi', 'number_of_rooms' : 10})
		self.assertIsInstance(the_dojo, Dojo, msg='The object should be an instance of the `Dojo` class')



if __name__=="__main__":
	unittest.main()