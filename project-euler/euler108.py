#!/usr/bin/env python

import sys
# incase you forget, the way to solve this problem is by realizing that 
# f(n) = floor(number_of_factors(n^2)/2) + 1


def main():
	limit = int(sys.argv[1])
	n_dict = dict()
	x = 3
	running = True
	while running:
		for y in range(2, x + 1):
			if x*y%(x + y) == 0:
				test = x*y/(x + y)
				try:
					n_dict[test] += 1
					if n_dict[test] > limit:
						print test, x, y
						running = False
						break
				except KeyError:
					n_dict[test] = 1
		x += 1

if __name__ == "__main__":
	sys.exit(main())
