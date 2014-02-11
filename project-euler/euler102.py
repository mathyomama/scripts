#!/usr/bin/env python


import sys

def check_origin_in_triangle(coordinates):
	count = 0
	for index, pair in enumerate(coordinates):
		a, b = coordinates[(index + 1)%3], coordinates[(index + 2)%3]
		if b[0] != a[0]:
			xDiff = b[0] - a[0]
			f = lambda x: (b[1] - a[1])*(x - a[0]) + a[1]*xDiff
			if (f(pair[0]) > pair[1]*xDiff and f(0) >= 0) or (f(pair[0]) < pair[1]*xDiff and f(0) <= 0):
				count += 1
		elif (pair[0] > a[0] and 0 >= a[0]) or (pair[0] < a[0] and 0 <= a[0]):
			count += 1
	if count == 3:
		return True
	else:
		return False

def main():
	foo = open("triangles.txt")
	count = 0
	for line in foo:
		array = map(int, line.split(','))
		coordinates = [(array[2*j], array[2*j + 1]) for j in xrange(3)]
		if check_origin_in_triangle(coordinates):
			count += 1
	print count

if __name__ == "__main__":
	sys.exit(main())
