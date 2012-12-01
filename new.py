import sys
sys.path.append("/home/mathyomama/Scripts/Spoj/")
from primes import listOfPrimes

prod = 1
for i in listOfPrimes:
	prod *= i
	if prod > listOfPrimes[-1]: break
	test = prod + 1
	if test in listOfPrimes: continue
	else: print(test)

