import math

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
    return (p**n) * (p ** (N-n)) * C(N,n)

def infoMeasure(n, p, N):
    return - math.log2(prob(n, p, N))

def sumProb(N, p):
    "k biet viet j ca"
    sum = 0
    for x in range(1, N + 1):
        sum += prob(x, p, N)
    return sum

def approxEntropy(N, p):
    sum = 0
    for x in range(1, N + 1):
        sum += infoMeasure(x, p, N) * prob(x, p, N)
    return sum

for i in range(1, 100):
	print(sumProb(i, 1/2))
print(C(1000, 100))