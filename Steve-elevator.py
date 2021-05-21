import numpy as np

#While riding an elevator the the (n-2)th floor of an n story building with k passengers, how many stops will you expect?

def simulateStops(floorCount,passengerCount):
    rng = np.random.default_rng()
    passengerStops = rng.integers(0,floorCount,passengerCount-1)
    numStops = 1 + np.sum(np.unique(passengerStops) < (floorCount - 3))
    return numStops


sampleCount = 10000
numFloors = 11
numPassengers = 6
totalStops = 0
for i in range(sampleCount):
    totalStops += simulateStops(numFloors,numPassengers)
print(totalStops/sampleCount)