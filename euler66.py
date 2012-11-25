maxTuple = (0, 0)
tuples = []
for D in range(1, 1001):
	if D**.5%1 == 0: continue
	y, x = 1, 0
	while True:
		x = (D*y**2 + 1)**.5
		if x%1 == 0:
			break
		y += 1
	tuples.append((D, x))
	print((D, x, y))
	#if tuples[-1][1] > maxTuple[1]:
	#	maxTuple = (D, x)
	#	print(maxTuple)

