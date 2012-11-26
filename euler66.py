from math import *

def infinite_fraction(D):
	alpha = D**.5
	a = floor(alpha)
	DList, DTuple = [a], ()
	for i in range(100):
		alpha = 1/(alpha - a)
		a = floor(alpha)
		DTuple += (a,)
		print(a, alpha)
	DList += DTuple
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

thirteenList = [3, (1, 1, 1, 1, 6)]
for i in range(10):
	print(composition(i, thirteenList))
