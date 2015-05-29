#!/usr/bin/env python

import sys
import itertools
import primes

import random
 
_mrpt_num_trials = 5 # number of bases to test
 
def is_probable_prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
 
    >>> is_probable_prime(1)
    Traceback (most recent call last):
        ...
    AssertionError
    >>> is_probable_prime(2)
    True
    >>> is_probable_prime(3)
    True
    >>> is_probable_prime(4)
    False
    >>> is_probable_prime(5)
    True
    >>> is_probable_prime(123456789)
    False
 
    >>> primes_under_1000 = [i for i in range(2, 1000) if is_probable_prime(i)]
    >>> len(primes_under_1000)
    168
    >>> primes_under_1000[-10:]
    [937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
 
    >>> is_probable_prime(6438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
    True
 
    >>> is_probable_prime(7438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
    False
    """
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

listOfPrimes = []
def isPrime(number):
    n = 0
    prime = listOfPrimes[n]
    while prime < number**.5:
        if number%prime == 0:
            return False
        n += 1
        prime = listOfPrimes[n]
    return True

def digitCombinationGenerator(n, d):
    digitIndex = range(n)
    if d == 0:
        for i in range(n - 2):
            for j in itertools.combinations(digitIndex[1:-1], i):
                yield [0] + list(j) + [n - 1]
    elif d%2 == 0:
        for i in range(n - 1):
            for j in itertools.combinations(digitIndex[0:-1], i):
                yield list(j) + [n - 1]
    else:
        for i in range(1, n):
            for j in itertools.combinations(digitIndex, i):
                yield list(j)

def intFormat(number):
    ans = 0
    for digit in number:
        ans *= 10
        ans += digit
    return ans

def changeDigit(number, indices):
    index = indices.pop(0)
    if index == 0:
        values = range(1, 10) # 1 to 9 for most significant digit
    elif index == len(number) - 1:
        values = range(1, 10, 2) # odds for the least significant digit
    else:
        values = range(10) # all the digits
    for value in values:
        number[index] = value
        if not indices:
            yield intFormat(number)
        else:
            for i in changeDigit(number[:], indices[:]):
                yield i

def S(n, d):
    """
    This function will determine the sum of the n-digit primes with the max number
    of repeats of digit, d. For example, for n = 4 and d = 1, the primes in this
    set are 1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111 and so S(4, 1) = 
    22275. The max number of repeats is for S(4, 1) is 3. 

    For the implementation, we will use a list to hold the digits of the number
    being tested for primality. We wil initially test for n digits repeated and
    then n-1 and so on. Once a number is found to be prime with m repeats, all 
    the primes of m repeats will be found and subsequently summed. The loop will
    break and the sum will be returned.
    """
    number = [d for i in range(n)]
    primeFound = False
    ans, minChange = 0, n
    for i in digitCombinationGenerator(n, d):
        if len(i) > minChange and primeFound:
            break
        for j in changeDigit(number[:], i[:]):
            if is_probable_prime(j):
                primeFound = True
                minChange = len(i)
                ans += j
    return ans

def main():
    ans = 0
    print(sum(S(10, d) for d in range(10)))

if __name__ == "__main__":
    sys.exit(main())
