#!/usr/bin/env python


def foo_polynomial(k, n):
	number = 0
	for order in range(n + 1):
		number += (-1)**order*(k)**(n - order)
	return number

def difference(array):
	if len(array) < 1:
		return []
	newArray = []
	for i in range(len(array) - 1):
		newArray.append(array[i + 1] - array[i])
	return newArray

def fip(array):
	arrayOfDifferences = []
	copyOfArray = array[:]
	while len(copyOfArray) > 0:
		arrayOfDifferences.append(copyOfArray)
		copyOfArray = difference(copyOfArray)
	number = 0
	for a in reversed(arrayOfDifferences):
		number += a[-1]
	return number

def main():
	maxOrder = 10
	yArray = [foo_polynomial(i, maxOrder) for i in xrange(1, maxOrder + 2)]
	answer = 0
	for i in xrange(1, maxOrder + 1):
		subArray = yArray[:i]
		something = fip(subArray)
		answer += something
	print answer

if __name__ == "__main__":
	main()
	
	
