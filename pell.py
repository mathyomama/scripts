for D in range(2, 50):
	if D**.5%1 == 0: continue
	x, y = 0, 1
	while True:
		x = (1 + D*y**2)**.5
		if x%1 == 0:
			break
		y += 1
	print(D, x, y)
