import time


digFac = [1]*10
for i in range(1, 10):
	digFac[i] = i*digFac[i - 1]

def factorial_loop(n):
	Sum = 0
	while n > 0:
		digit = n%10
		Sum += digFac[digit]
		n /= 10
	return Sum


terminationDict = dict()
N, maxLength, count = 1000000, 0, 0
for i in range(N + 1):
	someList = [i]
	n = 0
	while True:
		nextNumber = factorial_loop(someList[n])
		n += 1
		try:
			terminationDict[i] = terminationDict[nextNumber] + n
			break
		except KeyError:
			if nextNumber in someList:
				terminationDict[i] = n
				break
			someList.append(nextNumber)
	if n > 1:
		for j in range(1, n):
			terminationDict[someList[j]] = terminationDict[i] - j
	if terminationDict[i] > maxLength:
		maxLength = terminationDict[i]
		count = 1
	elif terminationDict[i] == maxLength:
		count += 1
print maxLength, count

print time.clock()