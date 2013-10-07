import primes
import time

target = 1000000
sumOfDivisors = dict()
for i in primes.listOfPrimes:
	if i >= target: break
	test, prevTest = i, 0
	subDict = dict()
	while test < target:
		if test == i:
			subDict[test] = test + 1
		else:
			subDict[test] = subDict[prevTest] + test
		prevTest = test
		test *= i
	sumOfDivisors[i] = subDict




print(time.clock())
