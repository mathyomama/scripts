import sys
sys.path.append("/home/mathyomama/Scripts/Spoj/")
from primes import listOfPrimes

def factorization(n):
	if n < 2: return (1,)
	factors, test, index, exp = [], n, 0, 0
	while test > 1:
		if test%listOfPrimes[index] == 0:
			test /= listOfPrimes[index]
			exp += 1
		elif exp == 0:
			index += 1
		else:
			factors.append((listOfPrimes[index], exp))
			index += 1
			exp = 0
	factors.append((listOfPrimes[index], exp))
	return factors


def gcd(a, b):
    if a == b or b == 0:
        return a
    elif a == 0:
        return b
    if ~a & 1:
        if b & 1:
            return gcd(a >> 1, b)
        else:
            return gcd(a >> 1, b >> 1) << 1
    if ~b & 1:
        return gcd(a, b >> 1)

    if a > b:
        return gcd((a - b) >> 1, b)
    return gcd((b - a) >> 1, a)


marker = 3/float(7)
quot = 1000000/7
numerator, denominator = 3*quot, 7*quot
print numerator, denominator
maxRatio = 0
while denominator > 3:
    denominator -= 1
    ratio = numerator/float(denominator)
    while ratio > marker:
        numerator -= 1
        ratio = numerator/float(denominator)
    if ratio > maxRatio and ratio < marker:
        maxRatio, num, den = ratio, numerator, denominator


print maxRatio, num, den
divisor = gcd(num, den)
print num/divisor