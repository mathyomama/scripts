#!/usr/bin/env python

import sys
import time


# simple factoring function, simply starts at 2 and divides out and then moves
# to 3 and continues (to the next integers, so all composites are essentially
# a waste of computation--simple to implement)
# Returns a list of factors
def factor(number):
    test = number
    factor = 2
    listOfFactors = list()
    while test > 1 and factor < number**.5:
        if test%factor == 0:
            listOfFactors.append(factor)
            test /= factor
        else:
            factor += 1
    if test > 1:
        listOfFactors.append(test)
    return listOfFactors

def main():
    start = time.time()
    listOfPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 51]
    test = 2001
    while True:
        factors = factor(test)
        if max(factors) < 10:
            print test, factors, "%s seconds" % (time.time() - start)
            break
        test += 2


if __name__ == "__main__":
    sys.exit(main())
