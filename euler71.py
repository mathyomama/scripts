import sys
sys.path.append("/home/mathyomama/Scripts/Spoj/")
from primes import listOfPrimes

def factorization(n):
	if n < 2: return (1,)
	factors, test, index, exp = [], n, 0, 0
	while test > 1:
		if test%listOfPrimes[index] == 0:
			test /= listOfPrimes[index]
			exp += 1
		elif exp == 0:
			index += 1
		else:
			factors.append((listOfPrimes[index], exp))
			index += 1
			exp = 0
	factors.append((listOfPrimes[index], exp))
	return factors

print(factorization(428567))
print(factorization(999990))
