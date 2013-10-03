from time import clock
from fractions import gcd


N = 1500000
LList = [0]*(N + 1)
n = int((-1 + (1 + 4*N)**.5)/2)
for x in range(1, n + 1):
	for y in range(1, x):
		if ~(x - y)&1 or gcd(x, y) > 1:
			continue
		L = 2*x*(x + y)
		if L <= N:
			for i in range(1, N/L + 1):
				LList[L*i] += 1

count = LList.count(1)
print count


print clock()