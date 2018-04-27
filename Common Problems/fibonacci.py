# f (n) = f(n-1) + f(n-2) where n >= 0

def fibonacci(n):
	if n < 0:
		return None
	elif n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
	a, b = 0, 1
	for i in range(0, n):
		a, b = b, a + b
	return a;

def fibonacci3(n):
	terms = [0, 1]
	for i in range(2,n+1):
		terms.append(terms[i-1] + terms[i-2])
	return terms[n]
