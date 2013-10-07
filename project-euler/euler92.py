import random
import numpy as np
import matplotlib.plot as plt

#parameters
kp, kn = 5/6/1000, 5/24/1000
stepSize, timeStep = 8, 100
forward = kp*timeStep
backward = forward + kn*timeStep

numberOfSteps = 1000
numberOfTrials = 100
totalDisplacement = numberOfSteps*[0]
for i in range(numberOfTrials):
	displacement = numberOfSteps*[0]
	for j in range(numberOfSteps):
		number = random.random()
		if number < forward:
			displacement[j] = displacement[j - 1] + stepSize
		elif number > forward and number < backward:
			displacement[j] = displacement[j - 1] - stepSize
		else:
			displacement[j] = displacement[j - 1]
		totalDisplacement[j] += displacement[j]

averageDisplacement = []
for i in range(numberOfSteps):
	averageDisplacement[i] = totalDisplacement[i]/numberOfTrials


