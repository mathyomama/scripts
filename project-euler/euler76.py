def summation(n):
	master = [[1, 1]]
	degree = sum(master[0])
	while degree < n:
		addage = []
		for group in master:
			if group[-1] < group[-2]:
				groupFake = group[:]
				groupFake[-1] += 1
				addage.append(groupFake)
			group.append(1)
		master += addage + [[degree, 1]]
		#print("degree", degree, "\t", "Addage:", addage, "\t", "master:", master)
		degree = sum(master[0])
	return master


coins = range(1, 101)
target = 100
dp = [0]*(target + 1)
dp[0] = 1
for c in coins:
	for j in range(len(dp)):
		if j + c < len(dp):
			dp[j + c] += dp[j]

print dp[target]