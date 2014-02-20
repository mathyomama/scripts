#!/usr/bin/env python


import sys


def modifiedInt(str):
	if str == "-" or str == "-\n":
		return 0
	else:
		return int(str)

def findMinimalConnectedSum(network):
	length = len(network)
	touchedNetwork = [[0 for j in xrange(length)] for i in xrange(length)]
	touchedVertices = [0]*length
	touchedVertices[0] = 1
	touchCount = sum(touchedVertices)
	while touchCount < length:
		minVal, minIndex, minRow = 1000, length, length
		badVal, badIndex = 1000, length
		for row, switch in enumerate(touchedVertices):
			if switch == 1:
				for index, val in enumerate(network[row]):
					if val != 0 and touchedVertices[index] == 0 and val < minVal:
						minVal, minIndex, minRow = val, index, row
		touchedVertices[minIndex] = 1
		touchedNetwork[minRow][minIndex], touchedNetwork[minIndex][minRow] = minVal, minVal
		touchCount = sum(touchedVertices)
	return touchedNetwork

def main():
	foo = open("network.txt")
	network = [map(modifiedInt, line.split(",")) for line in foo]
	foo.close()
	touchedNetwork = findMinimalConnectedSum(network)
#	networkFile = open("networkFile.csv", "w")
#	touchedNetworkFile = open("touchedNetwork.csv", "w")
#	for row, touchedRow in zip(network, touchedNetwork):
#		for element, touchedElement in zip(row, touchedRow):
#			networkFile.write(str(element) + ";")
#			touchedNetworkFile.write(str(touchedElement) + ";")
#		networkFile.write("\n")
#		touchedNetworkFile.write("\n")
#	networkFile.close()
#	touchedNetworkFile.close()
	print (sum(map(sum, network)) - sum(map(sum, touchedNetwork)))/2

if __name__ == "__main__":
	sys.exit(main())
