import unittest
import q2


class TestCase(unittest.TestCase):
	#Ensures that just numbers 1 to 100 are printed
	def test1(self):
		self.assertEqual(q2.isDivisibleByFour(2024), True)
	

if __name__ == '__main__':
	unittest.main()	
