from primes import factorization, totient

for j in range(1, 6):
	Sum = 0
	for i in range(2, 10**j + 1):
		Sum += totient(factorization(i))[1]
	print Sum
