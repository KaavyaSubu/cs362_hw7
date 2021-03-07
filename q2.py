

def isDivisibleByFour(x):
	if x % 4 == 0: return True
	else: return False


def isLeapYear(x):

	if isDivisibleByFour(x):
		if x % 100 == 0:
			if x % 400 == 0: return "Yes"
			else : return "No"
		else: return "Yes"
	else:
		return "No"
