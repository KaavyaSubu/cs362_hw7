



def printNumbers():
	nums = [x for x in range(1,101)]
	output = ""
	for x in nums: output += str(x)
	return output

def printFizzBuzz():
	nums = [x for x in range(1,101)]
	output = ""
	for x in nums:
		if x % 15 == 0: output += "FizzBuzz"
		elif x % 5 == 0: output += "Buzz"
		elif x % 3 == 0: output += "Fizz"
		else: output += str(x)

	
	
	return output	
