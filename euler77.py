from primes import listOfPrimes


N = 1000
pri = listOfPrimes[0:N]
dp = [0]*(N + 1)
dp[0] = 1
for p in pri:
	for j in range(len(dp)):
		if j + p < len(dp):
			dp[j + p] += dp[j]

for i in range(len(dp)):
	if dp[i] > 5000:
		print i
		break