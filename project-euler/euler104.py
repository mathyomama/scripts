#!/usr/bin/env python


import sys


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

def check_upper_pandigital(number, digCount):
	if digCount < 9:
		return False
	panSet = set()
	sample = number/(10**(digCount - 9))
	for _ in xrange(9):
		digit = sample%10
		if digit in panSet:
			break
		elif digit != 0:
			panSet.add(digit)
		sample /= 10
	return len(panSet) == 9

def fib_generator():
	a, b = 1, 0
	while True:
		yield a
		a, b = a + b, a

def main():
	fibList = fib_generator()
	number = fibList.next()
	count = 0
	digCount = 1
	digCompare = 10
	while count < 10000:
		count += 1
		if number > digCompare:
			digCount += 1
			digCompare *= 10
		if check_lower_pandigital(number) and check_upper_pandigital(number, digCount):
			print count
			break
		number = fibList.next()
	print digCount

if __name__ == "__main__":
	sys.exit(main())
