import sys
sys.path.append("/home/mathyomama/Scripts/Spoj/")
from primes import listOfPrimes

def permutation(a, b):
	if a/b >= 10 or a/b <= .1: return False
	aList, bList = [], []
	while a > 0:
		aList.append(a%10)
		bList.append(b%10)
		a //= 10
		b //= 10
	for i in aList:
		if i in bList:
			bList.remove(i)
		else: break
	if bList == []: return True
	else: return False

i = 0
while listOfPrimes[i] < 10000000:
	i += 1
print(listOfPrimes[i - 1])

