#!/usr/bin/env python


import sys


def modifiedInt(str):
	if str == "-" or str == "-\n":
		return "-"
	else:
		return int(str)

def findMinimalConnectedSum(network):
	length = len(network)
	touchedNetwork = [[0]*length]*length
	touchedVertices = [0]*length
	touchCount = sum(touchedVertices)
	minSum = 0
	while touchCount < length:
		minPath, minIndex = 1000, length
		if totalSum == 0:
			for index, val in enumerate(network[0]):
				if val < minPath:
					minPath = val
					minIndex = index
			minSum += minPath
		else:
			pass

def main():
	foo = open("network.txt")
	network = [map(modifiedInt, line.split(",")) for line in foo]
	for row in network:
		for element in row:
			print element, "\t",
		print ""

if __name__ == "__main__":
	sys.exit(main())
