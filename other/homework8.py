import random
import numpy as np
import matplotlib.pyplot as plt

#parameters
kp, kn = float(5)/6/1000, float(5)/24/1000
stepSize, timeStep = 8, 100
forward = kp*timeStep
backward = forward + kn*timeStep

numberOfSteps = 1000
numberOfTrials = 100
totalDisplacement = numberOfSteps*[0]
dwellTimes = []
for i in range(numberOfTrials):
	displacement = numberOfSteps*[0]
	dwellTimer = 0
	for j in range(numberOfSteps):
		number = random.random()
		if number < forward:
			displacement[j] = displacement[j - 1] + stepSize
			if dwellTimer > 0:
				dwellTimes.append(dwellTimer)
				dwellTimer = 0
		elif number > forward and number < backward:
			displacement[j] = displacement[j - 1] - stepSize
			if dwellTimer > 0:
				dwellTimes.append(dwellTimer)
				dwellTimer = 0
		else:
			displacement[j] = displacement[j - 1]
			dwellTimer += 1
		totalDisplacement[j] += displacement[j]

averageDisplacement = []
for i in range(numberOfSteps):
	averageDisplacement[i] = totalDisplacement[i]/numberOfTrials

#print dwellTimes[0]
#limit = max(dwellTimes)
#plt.hist(range(limit), weights = dwellTimes, bins = limit)
#plt.show()


