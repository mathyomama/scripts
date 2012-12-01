import sys
sys.path.append("/home/mathyomama/Scripts/Spoj/")
from primes import listOfPrimes

n, maximum, maximumi = 1000000, 0, 0
#for i in range(2, n + 1):
#	#Prime factorization
#	factors, test, index, exp = [], i, 0, 0
#	while test > 1:
#		if test%listOfPrimes[index] == 0:
#			test /= listOfPrimes[index]
#			exp += 1
#		else:
#			factors.append((listOfPrimes[index], exp))
#			index += 1
#			exp = 0
#	func = 1
#	for j in factors:
#		func *= 1/(1 - 1/j[0])
#	if func > maximum:
#		maximum = func
#		maximumi = i
#print(maximum, maximumi)

number, index, factors = 1, 0, []
while number < 1000000:
	number *= listOfPrimes[index]
	factors.append(listOfPrimes[index])
	index += 1
number /= listOfPrimes[index - 1]
print(number, listOfPrimes[index - 1])
