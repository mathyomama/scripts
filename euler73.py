import time


N = 12000
fraction, frac = [(1, 3), (1, 2)], (0, 0)
low, high = fraction[0], fraction[1]
length = 0
#finding the second term of the Farey Sequence
while high[1] + low[1] <= N:
	frac = (low[0] + high[0], low[1] + high[1])
	high = frac
fraction.insert(-1, frac)
#Finding the rest of the terms of the Farey Sequence
index = 1
lower, middle = fraction[0][1], fraction[1][1]
while True:
	higher = (N + lower)/middle*middle - lower
	if higher == fraction[-1][1]:
		break
	lower = middle
	middle = higher
	index += 1
print index

print time.clock()