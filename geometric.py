from math import log2

def prob(n, p):
	""" Calculates geometric distribution

	Gives the probability that the first occurrence of success requires n independent trials, 
	each with success probability p.

	Args:
		n: an positive integer denoting number of independent trials need.
		p: a float denoting probability of success in each trial, 0 < p <= 1.
	Returns:
		answer: a float, 0 <= answer <= 1.
	Raises:
		exit the program if n or p is not in appropriate range.
	"""
	assert n > 0
	assert 0 < p <= 1
	answer = ((1 - p) ** (n - 1)) * p
	assert 0 <= answer and answer <= 1
	return answer

def infoMeasure(n, p):
	""" Calculates Shannon information 

	Gives the Shannon information (a.k.a information content)
	of the probability that the first occurrence of success requires n independent trials, 
	each with success probability p.

	Args:
		n: an integer denoting number of independent trials need
		p: a float denoting probability of success in each trial, 0 < p <= 1		
	Returns:
		answer: a float
	Raises:
		exit the program if n or p is not in appropriate range.
	"""
	assert n > 0
	assert 0 < p <= 1
	return -log2(prob(n, p))

def sumProb(N, p):
	""" Calculates the sum of geometric distribution  

	Gives the sum of geometric distribution of all i not greater than N. 

	We can use sumProb() to verify that the sum of geometric distribution equals to 1
	by giving different N from a small (say 1) to a large integer (say 1000) and observe 
	how the results converge to 1.
	
	Args:
		N: a positive intenger
		p: a float denoting probability of success in each trial, 0 < p <= 1		
	Returns:
		answer: a float
	Raises:
		exit the program if N or p is not in appropriate range.
	"""
	assert N > 0
	assert 0 < p and p <= 1
		
	answer = 0
	for i in range(1, N + 1):
		answer += prob(i, p)
	return answer

def approxEntropy(N, p):
	""" Calculates the Shannon entropy

	Approximates the Shannon entropy of geometric distribution with a very large N.

	Args:
		N: a positive intenger
		p: a float denoting probability of success in each trial in geometric distribution, 0 < p <= 1		
	Returns:
		answer: a float
	Raises:
		exit the program if N or p is not in appropriate range.
	"""
	assert N > 0
	assert 0 < p and p <= 1
	answer = 0
	for i in range(1, N + 1):
		answer += infoMeasure(i, p) * prob(i, p)
	return answer

if __name__ == "__main__":
	print("Verify the sum of geometric distribution: ")
	for i in range(1, 1000):
		print(sumProb(i, 1/2))

	print("Approximate the entropy of geometric distribution: ")
	print(approxEntropy(1000, 1/2))