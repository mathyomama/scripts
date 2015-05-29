import math
import time


foo = open("base_exp.txt")
testCases = []
for line in foo:
	testCases.append(list(map(int, line.split(','))))
foo.close()

digits = []
maximum = 0
for i, pair in enumerate(testCases):
	digits.append((pair[1]*math.log10(pair[0])) + 1)
	if digits[i] > maximum:
		maximum = digits[i]
		print("This is the maximum", i, maximum)
	elif digits[i] > int(maximum):
		print(i, digits[i])

print(time.clock())
