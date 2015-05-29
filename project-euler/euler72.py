from primes import listOfPrimes
from bisect import bisect_left

n = 1000000
phi = {1: 1}
Sum = 0
for i in range(2, n + 1):
	#finding divisors of i
	placement = bisect_left(listOfPrimes, i)
	if listOfPrimes[placement] == i:
		phi[i] = i - 1
		Sum += phi[i]
		continue
	a, b = 0, 0
	for j in listOfPrimes:
		if i%j == 0:
			a, b = j, int(i/float(j))
			break
	#finding gcd of divisors
	d = 0
	if b%a == 0:
		d = a
	else:
		d = 1
	p = phi[a]*phi[b]*d/phi[d]
	phi[i] = p
	Sum += phi[i]
print Sum
