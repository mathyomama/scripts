import sys
sys.path.append("/home/mathyomama/Scripts/Spoj/")
from primes import listOfPrimes


def permutation(a, b):
    if len(a) != len(b): return False
    for i in a:
        x = a.count(i)
        if x != b.count(i): return False
    return True


def totient(tup):
    product, tot, ratio = 1, 1, 1
    for i in tup:
        product *= i[0]**i[1]
        tot *= i[0]**(i[1] - 1)*(i[0] - 1)
        ratio /= (1 - 1/float(i[0]))
    return (product, tot, ratio)


k, x, istart = 0, 0, 0
prime = listOfPrimes[k]
while prime < 10**7/float(3):
    k += 1
    prime = listOfPrimes[k]
    if prime**2 < 10**7:
        x, istart = prime, k
limit = listOfPrimes[k - 1]


minRatio = 1000
#for i in range(istart):
    #for j in range(istart - i):
        #tup = [(listOfPrimes[istart - i], 1), (listOfPrimes[istart - i - j], 1)]
        #triple = totient(tup)
        #if permutation(str(triple[0]), str(triple[1])) and triple[2] < minRatio:
            #minRatio = triple[2]
            #print triple, listOfPrimes[istart - i], istart - i, listOfPrimes[istart - i - j], istart - i - j


a = k - 1
while a > 0:
    b = 0
    while True:
        prime1, prime2 = listOfPrimes[a], listOfPrimes[b]
        prod = prime1*prime2
        if prod > 10**7:
            break
        tot = (prime1 - 1)*(prime2 - 1)
        ratio = prod/float(tot)
        if permutation(str(prod), str(tot)) and ratio < minRatio:
            minRatio = ratio
            print prime1, prime2, prod, tot, ratio
        b += 1
    a -= 1