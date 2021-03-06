def infinite_fraction(D):
	m, d, a = 0, 1, int(D**.5)
	DList = [a]
	#for the first iteration
	m = d*a - m
	d = (D - m**2)/d
	a = int((D**.5 + m)/d)
	initial, tup, DTuple = (m, d, a), tuple(), tuple()
	while tup != initial:
		DTuple += (a,)
		m = d*a - m
		d = (D - m**2)/d
		a = int((D**.5 + m)/d)
		tup = (m, d, a)
	DList.append(DTuple)
	return DList

def comp(x, y, z):
	return (z, x*z + y)

def composition(n, DList):
	tries = n - 1
	period = len(DList[1])
	arg = DList[1][tries%period]
	denum = (1, arg)
	while tries > 0:
		tries -= 1
		arg = DList[1][tries%period]
		denum = comp(arg, *denum)
	denum = (DList[0]*denum[1] + denum[0], denum[1])
	return denum

max = 0
for D in range(2,10000):
	if D**.5%1 == 0: continue
	i = 1
	DList = infinite_fraction(D)
	while True:
		tup = composition(i, DList)
		x, y = tup[0], tup[1]
		if x**2 - D*y**2 == 1:
			if x > max:
				max = x
				print(D)
			break
		i += 1


print(max)
