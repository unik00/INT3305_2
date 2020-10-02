from math import log2

""" Pre-calculate combinations"""
storage = dict() # for memorization, avoid repeated computations.
MAX_N = 1000
storage[0, 0] = 1
for i in range(1, MAX_N + 1):
    storage[(i, 0)] = 1
    storage[(i, i)] = 1
    for j in range(1, i):
        storage[(i, j)] = storage[(i - 1,j - 1)] + storage[(i - 1, j)]

def C(n, k):
    """ Calculates the k-combinations of a n-element set.
    Params:
        n : positive integer. 
        k : non-negative integer.
    Returns:
        an intenger.
    """
    return storage[(n, k)]

def prob(n, p, r):
    """ Calculates negative binomial distribution

    Gives the probability that r successes requires n independent trials, 
	each with success probability p.

    Args:
        n: an positive integer denoting number of independent trials required.
        p: a float denoting probability of success in each trial, 0 < p <= 1.
        r: an positive integer denoting the number of successes in n trials.
    Returns:
        answer: a float, 0 <= answer <= 1.
    Raises:
        exit the program if parameters are not in appropriate range.
    """
    assert r >= 1
    assert 0 < p <= 1
    assert n >= r
    answer = C(n - 1, r - 1) * p**r * (1 - p)**(n - r)
    assert 0 <= answer and answer <= 1
    return answer

def infoMeasure(n, p, r):
    """ Calculates Shannon information 

    Gives the Shannon information (a.k.a information content)
    of the probability that r successes requires n independent trials, 
	each with success probability p.
    
    Args:
        n: an positive integer denoting number of independent trials required.
        p: a float denoting probability of success in each trial, 0 < p <= 1.
        r: an positive integer denoting the number of successes in n trials.
    Returns:
        answer: a float, 0 <= answer <= 1.
    Raises:
        exit the program if parameters are not in appropriate range.
    """
    assert r >= 1
    assert 0 < p <= 1
    assert n >= r
    return -log2(prob(n, p, r))

def sumProb(N, p, r):
    """ Calculates the sum of negative-binomial distribution.
    
    Gives the sum of negative-binomial distribution of all postive integer i not greater than N. 

    We can use sumProb() to verify that the sum of negative-binomial distribution given sequence length N 
    equals to 1 by giving different N from a small (say 1) to a large integer (say 1000) and observe 
	how the results converge to 1.
    
    Args:
        N: an positive integer.
        p: a float denoting probability of success in each trial, 0 < p <= 1.
        r: an positive integer denoting the number of successes in n trials.
    Returns:
        answer: a float, 0 <= answer <= 1.
    Raises:
        exit the program if parameters are not in appropriate range.
    """
    assert r >= 1
    assert 0 < p <= 1
    assert N >= r

    answer = 0
    for n in range(r, N + 1):
        answer += prob(n, p, r)
    return answer

def approxEntropy(N, p, r):
    """ Calculates the Shannon entropy

    Approximates the Shannon entropy of negative-binomial distribution with a large N.

    Args:
        N: a positive intenger.
        p: a float denoting probability of success in each trial in geometric distribution, 0 < p <= 1		.
        r: an positive integer denoting the number of successes in a sequence.
    Returns:
        answer: a float.
    Raises:
        exit the program if N or p is not in appropriate range.
    """
    assert r >= 1
    assert 0 < p <= 1
    assert N >= r
    answer = 0
    for n in range(r, N + 1):
        answer += infoMeasure(n, p, r) * prob(n, p, r)
    return answer

if __name__ == "__main__":
    print("Verify the sum of negative-binomial distribution: ")

    start = 25
    end = 50
    for i in range(start, end + 1):
        print(sumProb(i, 1/2, start))

    print("Approximate the entropy of negative-binomial distribution: ")
    print(approxEntropy(1000, 1/2, 26))