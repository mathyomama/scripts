#!/usr/bin/env python


import sys
import math


def check_lower_pandigital(number):
	panSet = set()
	for _ in xrange(9):
		digit = number%10
		if digit in panSet:
			break
		elif digit != 0:
			panSet.add(digit)
		number /= 10
	return len(panSet) == 9

def check_upper_pandigital(number):
	panSet = set()
	sample = number
	for _ in xrange(9):
		digit = sample%10
		if digit in panSet:
			break
		elif digit != 0:
			panSet.add(digit)
		sample /= 10
	return len(panSet) == 9

def fib_generator_mod_billion():
	a, b = 1, 0
	while True:
		yield a
		a, b = a + b, a
		a %= 1000000000

def fib_generator():
	a, b = 1, 0
	while True:
		yield a
		a, b = a + b, a

def fib_approximation(n):
	try:
		return math.floor(((1 + math.sqrt(5))/2)**n/math.sqrt(5) + .5)
	except OverflowError:
		print "Overflow error, count was at", n
		sys.exit(0)

def fib_approximation_upper(n):
	phi = (1 + math.sqrt(5))/2
	multiplier = phi
	product = 1/math.sqrt(5)
	for i in xrange(n):
		product *= multiplier
		if product > 1000000000:
			product /= 10
	return  int(product)

def main():
	fibList = fib_generator_mod_billion()
	number = fibList.next()
	count = 1
	approx, phi = 1/math.sqrt(5), (1 + math.sqrt(5))/2
	while count < 1000000:
		approx *= phi
		if approx > 1000000000:
			approx /= 10
		test = int(approx)
		if check_lower_pandigital(number):
			if check_upper_pandigital(test):
				print count
				break
		number = fibList.next()
		count += 1

if __name__ == "__main__":
	sys.exit(main())
