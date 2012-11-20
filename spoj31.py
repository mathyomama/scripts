import cmath

def bigM(a, b):
	small = min(a, b)
	if small < 2**320:
		return a*b
	else:
		m = int((cmath.log10(small, 2) + 1)/2) + 1
		M = 2**m
		a0, a1 = a%M, a>>m
		b0, b1 = b%M, b>>m
		z0 = bigM(a0, b0)
		z2 = bigM(a1, b1)
		z1 = bigM((a1 + a0), (b1 + b0)) - z0 - z2
		ans = z2<<(2*m) + z1<<m + z0
		return ans


n = int(input())
for i in range(n):
	a, b = map(int, input().split())
	ans = bigM(a, b)
	print(ans)

