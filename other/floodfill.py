def adjacentSpots(pos):
	x, y = pos
	yield (x+1, y)
	yield (x, y+1)
	yield (x-1, y)
	yield (x, y-1)

def square(x, y, width, height):
	westEdge = [(x, y+b) for b in range(height)]
	eastEdge = [(x+width, y+b) for b in range(height)]
	southEdge = [(x+a, y) for a in range(width)]
	northEdge = [(x+a, y+height) for a in range(width)]

	return westEdge+eastEdge+southEdge+northEdge

outsideBoundary = set(square(0, 0, 20, 20))

insideEdge = set(square(5, 5, 3, 4))

goodSpots = set([startingPoint])
edge = set([startingPoint])

while edge:
	tempEdge = edge.copy()
	edge = set()
	for spot in tempEdge:
		print "Looking at" + str(spot)
		for aSpot in adjacentSpots(spot):
			if aSpot in insideEdge or aSpot in outsideBoundary or aSpot in goodSpots:
				continue
			edge.add(aSpot)
			goodSpots.add(aSpot)
			print "Added position %s" % str(aSpot)

#while True:
#	tempGoodSpots = goodSpots.copy()
#	for spot in tempGoodSpots:
#		print "Looking at" + str(spot)
#		for aSpot in adjacentSpots(spot):
#			if aSpot in insideEdge or aSpot in outsideBoundary:
#				continue
#			goodSpots.add(aSpot)
#			print "Added position %s" % str(aSpot)
#	print "Compare: %d v %d" % (len(tempGoodSpots), len(goodSpots))
#	if len(tempGoodSpots) == len(goodSpots):
#		break

print "DONE with"
print goodSpots
	
