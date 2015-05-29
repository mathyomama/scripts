foo = open("./primes1.txt")
listOfPrimes = []
for line in foo:
	aList = line.split()
	for number in aList:
		listOfPrimes.append(int(number))
foo.close()


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


def totient(tup):
    product, tot, ratio = 1, 1, 1
    for i in tup:
        product *= i[0]**i[1]
        tot *= i[0]**(i[1] - 1)*(i[0] - 1)
        ratio /= (1 - 1/float(i[0]))
    return (product, tot, ratio)

def binary_search(aList, n):
	low, high = 0, len(aList) - 1
	while True:
		if high <= low:
			return -1
		mid = (low + high)/2
		if aList[mid] > n:
			high = mid - 1
		elif aList[mid] < n:
			low = mid + 1
		else:
			return mid
