def summation(n):
	master = [[1, 1]]
	degree = sum(master[0])
	while degree < n:
		addage = []
		for group in master:
			if group[-1] < group[-2]:
				groupFake = group[:]
				groupFake[-1] += 1
				addage.append(groupFake)
			group.append(1)
		master += addage + [[degree, 1]]
		#print("degree", degree, "\t", "Addage:", addage, "\t", "master:", master)
		degree = sum(master[0])
	return master

print(len(summation(100)))
