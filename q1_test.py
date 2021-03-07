import unittest
import q1


class TestCase(unittest.TestCase):
	#Ensures that just numbers 1 to 100 are printed
	def test1(self):
		expectedString = "123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100"
		self.assertEqual(q1.printNumbers(), expectedString)
	
	#Prints Fizz,Buzz, and FizzBuzz at the right times
	def test2(self):
		expectedString = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617Fizz19BuzzFizz2223FizzBuzz26Fizz2829FizzBuzz3132Fizz34BuzzFizz3738FizzBuzz41Fizz4344FizzBuzz4647Fizz49BuzzFizz5253FizzBuzz56Fizz5859FizzBuzz6162Fizz64BuzzFizz6768FizzBuzz71Fizz7374FizzBuzz7677Fizz79BuzzFizz8283FizzBuzz86Fizz8889FizzBuzz9192Fizz94BuzzFizz9798FizzBuzz"
		self.assertEqual(q1.printNumbers(), expectedString)

if __name__ == '__main__':
	unittest.main()	
