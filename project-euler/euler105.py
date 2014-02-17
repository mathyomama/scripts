#!/usr/bin/env python


import sys
import itertools


def check_speciality(sortedIterable):
	setA = set(sortedIterable)
	length = len(setA)
	sum1, sum2 = sum(sortedIterable[:(length - 1)/2 + 1]), sum(sortedIterable[length/2 + 1:])
	if sum1 <= sum2:
		return False
	for r in xrange(2, length/2 + 1):
		for com1 in itertools.combinations(setA, r):
			setB = set(com1)
			for com2 in itertools.combinations(setA - setB, r):
				setC = set(com2)
				if sum(setB) == sum(setC):
					return False
	return True

def main():
	print check_speciality([42, 65, 75, 81, 84, 86, 87, 88])
	print check_speciality([79, 119, 139, 150, 157, 158, 159, 161, 164])
	foo = open("sets.txt")
	count = 0
	summation = 0
	for line in foo:
		testList = map(int , line.split(","))
		testList.sort()
		if check_speciality(testList):
			count += 1
			summation += sum(testList)
	print count, summation

if __name__ == "__main__":
	sys.exit(main())
