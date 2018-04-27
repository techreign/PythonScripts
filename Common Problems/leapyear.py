def is_leap_year(n):
	if n < 0:
	 return False
	if n % 100 == 0:
		if n % 400 == 0:
			return True
		return False
	if n % 4 == 0:
		return True
	return False

def is_leap_year2(n):
	if n % 4 == 0:
		if % 100 == 0:
			if n % 400 == 0:
				return True
			return False
		return True
	return False

def is_leap_year3(year):
	if n % 400:
		return True
	elif n % 100:
		return False
	elif n % 4 == 0:
		return True
	return False
