import numpy as np
import matplotlib.pyplot as pyplot

#How often will one need to wait for stoplights while traversing a city block?

def simulateTrip(gridSize):
    rng = np.random.default_rng()
    xPos = gridSize
    yPos = gridSize
    numRedLights = 0
    while xPos > 0 and yPos > 0:
        redLightY = rng.choice([True,False])
        if xPos == 0 or yPos == 0:
            if xPos == 0:
                yPos -= 1
                if redLightY:
                    numRedLights += 1
            else:
                xPos -= 1
                if not redLightY:
                    numRedLights +=1
        elif redLightY:
            xPos -= 1
        else:
            yPos -= 1
    return numRedLights
    
numSamples = 1000
averageWaits = np.zeros(1001)

for i in range(1001):
    for j in range(numSamples):
        averageWaits[i] += simulateTrip(i)
    print(i)

averageWaits = averageWaits / numSamples

pyplot.plot(np.arange(1001),averageWaits)
pyplot.show()