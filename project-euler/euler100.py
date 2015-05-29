import time


def is_perfect_square(n):
	high, low = n, 1
	mid = (high + low)//2
	while True:
		mid = (high + low)//2
		midSquare = mid*mid
		if low > high:
			return False
		elif midSquare == n:
			return True
		elif midSquare > n:
			high = mid - 1
		elif midSquare < n:
			low = mid + 1
		elif low + 1 == high:
			return False


for i in range(100):
	print(i, is_perfect_square(i))

smallFactor, blue, total = 3, 3, 4
while total < 10**12:
	bigFactor = smallFactor + 1 
	while True:
		testBlue = smallFactor*bigFactor
		testTotal = (1 + (1 + 8*(testBlue**2 - testBlue))**.5)/2
		testTestBlue = (1 + (1 + testTotal**2 - testTotal)**.5)/2
		if is_perfect_square(1 + 8*(testBlue**2 - testBlue)):
			smallFactor, blue, total = bigFactor, testBlue, testTotal
			print(blue, total, smallFactor, testTestBlue)
			break
		bigFactor += 1

print(blue, total, smallFactor)
print(time.clock())
