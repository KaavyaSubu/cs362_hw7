import unittest
import q2


class TestCase(unittest.TestCase):
	#Ensures that number is divisible by 4
	def test1(self):
		self.assertEqual(q2.isDivisibleByFour(2024), True)
		self.assertEqual(q2.isLeapYear(2000), "Yes")

if __name__ == '__main__':
	unittest.main()	
