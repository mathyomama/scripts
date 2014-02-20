#!/usr/bin/env python


import sys
import itertools


def check_speciality(sortedIterable):
	setA = set(sortedIterable)
	length = len(setA)
	sum1, sum2 = sum(sortedIterable[:(length - 1)/2 + 1]), sum(sortedIterable[length/2 + 1:])
	count = 0
	for r in xrange(length/2, length/2 + 1):
		for com1 in itertools.combinations(setA, r):
			setB = set(com1)
			for com2 in itertools.combinations(setA - setB, r):
				setC = set(com2)
				count += 1
	print count

def count_equalities(sortedIterable):
	length = len(sortedIterable)
	count = 0
	for r in xrange(4, length + 1, 2):
		preCount = 0
		for com in itertools.combinations(sortedIterable, r):
			comList = list(com)
			setA = set(com)
			initial = [comList.pop(0)]
			#print "the comList:", comList
			for smallerCom in itertools.combinations(comList, r/2 - 1):
				testComB = initial + list(smallerCom)
				setB = set(testComB)
				testComC = sorted(list(setA - setB))
				#print smallerCom, testComB, testComC
				for a, b in zip(testComB, testComC):
					if a > b:
						preCount += 1
						#print "1st set:", testComB, "2nd set:",  testComC
						break
		print preCount
	print count

def main():
	testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	count_equalities(testList)

if __name__ == "__main__":
	sys.exit(main())
