#almost equilateral triangle: third side differs by no more than one, perimeter is less than one billion
#a, a, b: a^2 - (b/2)^2 = c^2, Area = bc/2, b = a +- 1, (a^2)*3/4 -+ a/2 - 1/4 = c^2, c = sqrt(3*a^2 -+ 2a - 1)/2

def area(base, height):
	return base*height//2

target, summation, P, i = 1000000000, 0, 1, 2
while P < target:
	cpositive, cnegative = (3*i*i + 2*i - 1)**.5, (3*i*i - 2*i - 1)**.5
	if cpositive%1 == 0:
		summation += 3*i - 1
		print(i, i - 1)
		i = int(i*3.39)
	elif cnegative%1 == 0:
		summation += 3*i + 1
		print(i, i + 1)
		i = int(i*3.39)
	P = 3*i
	i += 1
print(summation)

