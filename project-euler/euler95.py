#!/usr/bin/env python

import primes
import bisect


def binarySearch(array, element, low=0, high=None):
	high = high or len(array)
	pos = bisect.bisect_left(array, element, low, high)
	return (pos if pos != high and array[pos] == element else -1)


def factorFirstFactor(n):
	if binarySearch(primes.listOfPrimes, n) > -1:
		return n, 1, 1
	prime = 1
	count = 0
	for prime in primes.listOfPrimes:
		if n%prime == 0:
			while n%prime == 0:
				count += 1
				n /= prime
			break
	return prime, count, n


def primeSumOfDivisors(prime, count):
	summation, product = 0, 1
	for i in xrange(count + 1):
		summation += product
		product *= prime
	return summation


def getElement(array, index):
	return array[index - 1]

def setElement(array, index, number):
	try:
		array[index - 1] = number
	except IndexError:
		pass

limit = 1000000
sumOfProperDivisors = [0]*limit
for i in xrange(2, limit):
	prime, count, quotient = factorFirstFactor(i)
	multiplier = primeSumOfDivisors(prime, count)
	setElement(sumOfProperDivisors, i, multiplier*(getElement(sumOfProperDivisors, quotient) + quotient) - i)

maxLength = 0
minimum = 0
#cycle = [0]*limit
for i in xrange(1, limit):
	number = getElement(sumOfProperDivisors, i)
	count = 1
	while number > i and number < limit and count < 100:
		count += 1
		number = getElement(sumOfProperDivisors, number)
	if number == i and count > maxLength:
		maxLength = count
		minimum = i

print minimum, maxLength
