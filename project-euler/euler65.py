def comp(x, y, z):
	return (z, x*z + y)

def frac_comp_of_e(n):
	x = n - 1
	arg = (2*(x//3 + 1))**((x%3)%2)
	denum = (1, arg)
	while x > 0:
		x -= 1
		arg = (2*(x//3 + 1))**((x%3)%2)
		denum = comp(arg, *denum)
	denum = (2*denum[1] + denum[0], denum[1])
	return denum

for i in range(1, 11):
	print(frac_comp_of_e(i), (2*(i//3 + 1))**((i%3)%2))

numerator = frac_comp_of_100(e)[0]
sum = 0
while numerator > 0:
	sum += numerator%10
	numerator //= 10
print(sum)
