import time
from primes import listOfPrimes

def find_k(factoring):
	length = len(factoring)
	summation, product = 0, 1
	for i in factoring:
		summation += i
		product *= i

	difference = product - summation
	k = difference + length
	return k

def generator_of_factors(primeFactors):



tup = (3, 7)
print(find_k(tup))