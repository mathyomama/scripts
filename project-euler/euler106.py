#!/usr/bin/env python


import sys
import itertools


def check_speciality(sortedIterable):
	setA = set(sortedIterable)
	length = len(setA)
	sum1, sum2 = sum(sortedIterable[:(length - 1)/2 + 1]), sum(sortedIterable[length/2 + 1:])
	if sum1 <= sum2:
		return False
	count = 0
	for r in xrange(2, length/2 + 1):
		for com1 in itertools.combinations(setA, r):
			setB = set(com1)
			for com2 in itertools.combinations(setA - setB, r):
				setC = set(com2)
				count += 1
				if sum(setB) == sum(setC):
					return False
	print count
	return True

def main():
	print check_speciality([20, 31, 38, 39, 40, 42, 45])

if __name__ == "__main__":
	sys.exit(main())
