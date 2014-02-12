#!/usr/bin/env python


import math
from primes import listOfPrimes, factorization

def find_k(factoring):
	length = len(factoring)
	summation, product = 0, 1
	for i in factoring:
		summation += i
		product *= i

	difference = product - summation
	k = difference + length
	return k

def pop_factor(prime_factorization):
	length = len(prime_factorization)
	limit = 1
	number = 1
	for i in xrange(len(prime_factorization)):
		limit *= prime_factorization[i][1] + 1
		number *= prime_factorization[i][0]**prime_factorization[i][1]

	candidates = [prime_factorization[i][0] for i in xrange(length)]
	candidates_indices = [0 for _ in xrange(length)]
	nums = [1]*limit
	for i in xrange(1, limit):
		nextn = min(candidates)
		nums[i] = nextn
		if nextn == number:
			break
		yield nextn

		for index, val in enumerate(candidates):
			if val == nextn:
				try:
					candidates_indices[index] += 1
					while prime_factorization[index][0]*nums[candidates_indices[index]]%(prime_factorization[index][0]**(prime_factorization[index][1] + 1)) == 0:
						candidates_indices[index] += 1
					candidates[index] = prime_factorization[index][0]*nums[candidates_indices[index]]
					if candidates_indices[index] > i:
						candidates[index] = number
				except IndexError:
					candidates[index] = number
	yield number

limit = 12000
minNValues = [0]*(limit + 1)
setMinNValues = set()
NToKList = [set(), set(), set(), set()]
N = 4
count = 1
while count < limit:
	kValues = set()
	prime_factorization = factorization(N)
	factors = pop_factor(prime_factorization)
	factor = factors.next()
	root = N**.5
	while factor <= root:
		k = find_k((factor, N/factor))
		if k > N:
			break
		kValues.add(k)
		kSet = NToKList[N/factor]
		if len(kSet) == 0:
			break
		for i in kSet:
			kValues.add(k + i - 1)
		factor = factors.next()
	NToKList.append(kValues)
	for val in kValues:
		try:
			if minNValues[val] == 0:
				minNValues[val] = N
				setMinNValues.add(N)
				count += 1
		except IndexError:
			continue
	N += 1

print sum(setMinNValues), N

#for index, s in enumerate(NToKList):
#	print index, s

#k_list = []
#maximum, counter = 0, 0
#summation = 0
#limit = 12000
#for number in xrange(4, 14000):
#	prime_factors = factorization(number)
#	factoring = []
#	for (prime, exp) in prime_factors:
#		for i in xrange(exp):
#			factoring.append(prime)
#	short_factoring = (prime_factors[0][0], number/prime_factors[0][0])
#	tup = (find_k(factoring), number, find_k(short_factoring))
#	k_list.append(tup)
#	if tup[0] > maximum and counter == 0:
#		maximum = tup[0]
#		summation += tup[1]
#		if tup[0] >= limit:
#			counter += 1
#		print(tup)
#
#print summation
