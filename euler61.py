def ngonal(order, n):
	if order == 3:
		return n*(n + 1)//2
	elif order == 4:
		return n*n
	elif order == 5:
		return n*(3*n - 1)//2
	elif order == 6:
		return n*(2*n - 1)
	elif order == 7:
		return n*(5*n - 3)//2
	elif order == 8:
		return n*(3*n -2)
	else:
		print('Out of order')

ngonalList = []
for i in range(3, 9):
	setOfOrder = []
	number, n = 0, 1
	while number < 10000:
		if number >= 1000:
			setOfOrder.append(number)
		number = ngonal(i, n)
		n += 1
	ngonalList.append(setOfOrder)

while i < len(ngonalList[0]):
	for row in ngonalList:
		if i < len(row):
			print(row[i], end = '\t')
	print()
	i += 1
	