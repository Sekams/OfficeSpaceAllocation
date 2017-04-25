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

	#Test if the class creates a type of itself
	def test_type(self):
		the_dojo = Dojo({'location' : 'Nairobi', 'number_of_rooms' : 10})
		self.assertTrue((type(the_dojo) is Dojo), msg='The object should be of type `Dojo`')

	#Test if the class creates an accurate default model

if __name__=="__main__":
	unittest.main()