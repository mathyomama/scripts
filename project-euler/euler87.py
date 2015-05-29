import time
from primes import listOfPrimes


target = 50000000
maximumSquareArgument = target**.5
maximumCubeArgument = target**(1/3)
maximumFourthArgument = target**.25


goodNumbers = set()
count = 0
for i in listOfPrimes:
	if i > maximumSquareArgument: break
	for j in listOfPrimes:
		if j > maximumCubeArgument: break
		for k in listOfPrimes:
			if k > maximumFourthArgument: break
			test = i**2 + j**3 + k**4
			if test > target: break
			count += 1
			goodNumbers.add(test)


print(count, len(goodNumbers))
print(time.clock())
