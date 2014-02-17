#!/usr/bin/env python


import sys
import itertools


def check_speciality(iterable):
	length = len(iterable)
	if length < 3:
		print "Not enough elements."
		return False
	A = set(iterable)
	for i in xrange(1, length/2):
		for j in xrange(i, length - i):
			if  i == 1 and j == 1:
				continue
			for com1 in itertools.combinations(A, i):
				B = set(com1)
				for com2 in itertools.combinations(A - B, j):
					C = set(com2)
					if (i > j and sum(B) <= sum(C)) or (i < j and sum(B) >= sum(C)) or (sum(B) == sum(C)):
						return False
	return True

def check_seven(iterable):
	setA = set(iterable)
	length = len(setA)
	if length != 7:
		print "Not seven elements."
		return False
	A = list(iterable)
	A.sort()
	largeSum = A[0]
	smallSum = 0
	if A[0] + A[1] + A[2] + A[3] <= A[4] + A[5] + A[6]:
		return False
#	for i in range(1, 4):
#		largeSum += A[i]
#		smallSum += A[length - i]
#		if largeSum <= smallSum:
#			return False
	for i in range(2, 4):
		for com1 in itertools.combinations(setA, i):
			setB = set(com1)
			for com2 in itertools.combinations(setA - setB, i):
				setC = set(com2)
				if sum(setB) == sum(setC):
					return False
	return True

def main():
	print check_seven([19, 27, 30, 31, 33, 35, 40])
	minSum = 1000
	for com in itertools.combinations(xrange(20, 50), 7):
		A = set(com)
		if check_seven(A) and sum(A) < minSum:
			print A
			break


if __name__ == "__main__":
	sys.exit(main())
