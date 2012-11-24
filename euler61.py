def ngonal(order, n):
	"formula for nth n-gonal with some order"
	if order == 3: return n*(n + 1)//2
	elif order == 4: return n*n
	elif order == 5: return n*(3*n - 1)//2
	elif order == 6: return n*(2*n - 1)
	elif order == 7: return n*(5*n - 3)//2
	elif order == 8: return n*(3*n -2)
	else: print('Out of order')

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

def cyclic(remainingOrders, answer):
	"recursive function for finding a cycle, in this case for n-gonal numbers"
	if len(answer) == 6:
		return answer
	test = None
	if len(answer) > 0:
		test = answer[-1]%100
	i = 0
	while i < len(remainingOrders):
		currentOrder = remainingOrders.pop(i)
		currentIndex = 0
		while currentIndex < len(ngonalList[currentOrder]):
			if currentOrder == 0:
				answer.append(ngonalList[currentOrder][currentIndex])
				cyclic(remainingOrders, answer)
			elif test == ngonalList[currentOrder][currentIndex]//100:
				answer.append(ngonalList[currentOrder][currentIndex])
				cyclic(remainingOrders, answer)
			currentIndex += 1
		remainingOrders.insert(i, currentOrder)
		i += 1
	answer.pop()

remainingOrders, answer = list(range(6)), []
cyclic(remainingOrders, answer)
print(answer)
