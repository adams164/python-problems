import numpy as np


#When waiting at the 2nd floor in a 7 story building, what is the probability that the first elevator to arrive comes from above?

#Simulate waiting for an elevator, returning true if it arrives from above.
def fromAbove(numFloors,numElevators):
    rng = np.random.default_rng()
    elevatorPositions = rng.random((numElevators,2))
    elevatorDistances = np.zeros(numElevators)
    for eIndex in range(numElevators):
        if elevatorPositions[eIndex,0] < 1/(numFloors-1):
            if elevatorPositions[eIndex,1] < 0.5:
                elevatorDistances[eIndex] = 1/(numFloors-1) + elevatorPositions[eIndex,0]
            else:
                elevatorDistances[eIndex] = 1/(numFloors-1) - elevatorPositions[eIndex,0]
        else:
            if elevatorPositions[eIndex,1] < 0.5:
                elevatorDistances[eIndex] = elevatorPositions[eIndex,0] - 1/(numFloors-1)
            else:
                elevatorDistances[eIndex] = 2 - elevatorPositions[eIndex,0] - 1/(numFloors-1)
    closestElevator = np.argmin(elevatorDistances)
    return elevatorPositions[closestElevator,0]>(1/(numFloors-1))
        
elevatorCount = 3
sampleCount = 100000
floorCount = 7
aboveCount = 0
for i in range(sampleCount):
    if fromAbove(floorCount,elevatorCount):
        aboveCount += 1
print(aboveCount/sampleCount)
