import numpy as np


#Given n points along an interval, what is the probability that a point's closest neighbor is mutual?

def mutualNeighbors(n):
    rng = np.random.default_rng()
    points = rng.random(n)
    points.sort()
    neighbors = np.arange(n)
    for index in range(n):
        nearestNeighbor = -1
        distance = 1
        if index > 0:
            nearestNeighbor = index - 1
            distance = points[index] - points[nearestNeighbor]
        if index < n-1:
            if points[index + 1] - points[index] < distance:
                nearestNeighbor = index + 1
        neighbors[index] = nearestNeighbor
        
    mutual = 0
    for point in range(n):
        if neighbors[neighbors[point]] == point:
            mutual += 1
    return mutual/n
    
pointCount = 30
sampleCount = 100000
averageProbability = 0
for i in range(sampleCount):
    averageProbability += mutualNeighbors(pointCount)
print(averageProbability/sampleCount)
