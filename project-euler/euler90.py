import time

#0 is on one cube, then 1, 4, 9/6 should be on the other
#if 1 in on one cube, then 0, 6, 8 should be on the other
#2 and 5 should be on separate cubes (can be flipped)
#if 6 is on one cube, then 1, 3, 4 should be on the other
#7 is not required
#{0, 2, 6, 8, _, _} and {1, 3, 4, 5, 9, _}

def check_cubes(a ,b):
	if len(a) != 6 and len(b) != 6:
		return false
	if 0 in a or 0 in b:
		