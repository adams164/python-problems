import numpy as np
import random

#What is the probability that a burglar revisits a house after 1<k<7 random walk steps?

def simulateBurgalry(numSteps):
    stops = np.zeros(numSteps+1)
    for i in range(numSteps):
        stepChoice = random.randint(0,3)
        if stepChoice == 0:
            stops[i+1] = stops[i] - 2
        elif stepChoice == 1:
            stops[i+1] = stops[i] - 1
        elif stepChoice == 2:
            stops[i+1] = stops[i] + 1
        elif stepChoice == 3:
            stops[i+1] = stops[i] + 2
    _, uniqueStops = np.unique(stops, return_counts = True)

    return uniqueStops.size == stops.size
    
    
sampleCount = 10000
for k in range(1,8):
    noRepeatVisits = 0
    for i in range(sampleCount):
        if simulateBurgalry(k):
            repeatVisits += 1
    print(k,repeatVisits/sampleCount)