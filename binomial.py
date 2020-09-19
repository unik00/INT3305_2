from math import log2

storage = dict() # for memorization, avoid repeated computations.

def C(n, k):
	""" Calculates the k-combinations of a n-element set.
	Params:
		k : non-negative integer.
		n : positive integer. 
	"""
	if (n == k) or (k == 0):
		return 1

	if (n, k) in storage:
		return storage[(n, k)]

	storage[(n, k)] = C(n - 1, k - 1) + C(n - 1, k)
	return storage[(n, k)] 

def prob(n, p, N):
	""" Calculates binomial distribution

	Gives the probability that the number of successes 
	in a sequence of N independent experiments is n,
	each experiment has a success probability p.

	Args:
		n: an positive integer denoting number of successes in a sequence.
		p: a float denoting probability of success in each trial, 0 < p <= 1.
		N: an positive integer, N >=n, denoting the length of the sequence.
	Returns:
		answer: a float, 0 <= answer <= 1.
	Raises:
		exit the program if parameters are not in appropriate range.
	"""
	assert n >= 0
	assert 0 < p <= 1
	assert N >= n
	answer = C(N, n) * p**n * (1 - p)**(N - n)
	assert 0 <= answer and answer <= 1
	return answer

def infoMeasure(n, p, N):
	""" Calculates Shannon information 

	Gives the Shannon information (a.k.a information content)
	of the probability that the number of successes 
	in a sequence of N independent experiments is n,
	each experiment has a success probability p.

	Args:
		n: an positive integer denoting number of successes in a sequence.
		p: a float denoting probability of success in each trial, 0 < p <= 1.
		N: an positive integer, N >=n, denoting the length of the sequence.
	Returns:
		answer: a float, 0 <= answer <= 1.
	Raises:
		exit the program if parameters are not in appropriate range.
	"""
	assert n >= 0
	assert 0 < p <= 1
	assert N >= n
	return -log2(prob(n, p, N))

def sumProb(N, p):
	""" Calculates the sum of binomial distribution.
	
	Given the number of sequence length N and the probability of success in each trial p, 
	the method sums up the probability that there are n successes in a sequence with n 
	in range [0, N].

	We can use sumProb() to verify that the sum of binomial distribution given sequence length N 
	equals to 1 by giving different N.
	
	Args:
		N: a positive intenger denoting the length of the sequence of trials.
		p: a float denoting probability of success in each trial, 0 < p <= 1.
	Returns:
		answer: a float
	Raises:
		exit the program if N or p is not in appropriate range.
	"""
	assert N > 0
	assert 0 < p and p <= 1
		
	answer = 0
	for n in range(0, N + 1):
		answer += prob(n, p, N)
	return answer

def approxEntropy(N, p):
	""" Calculates the Shannon entropy

	Approximates the Shannon entropy of binomial distribution.

	Args:
		N: a positive intenger denoting the length of sequence of trials.
		p: a float denoting probability of success in each trial in geometric distribution, 0 < p <= 1		.
	Returns:
		answer: a float.
	Raises:
		exit the program if N or p is not in appropriate range.
	"""
	assert N > 0
	assert 0 < p and p <= 1
	answer = 0
	for n in range(1, N + 1):
		answer += infoMeasure(n, p, N) * prob(n, p, N)
	return answer

if __name__ == "__main__":
	print("Verify the sum of binomial distribution: ")
	for i in range(1, 100):
		print(sumProb(i, 1/2))

	print("Approximate the entropy of binomial distribution: ")
	print(approxEntropy(1000, 1/2))