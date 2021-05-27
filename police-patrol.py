import numpy as np

#Simulate police cars on a road to determine the optimal approach

def computeDistances(inputPositions):
    assert inputPositions.size == 3
    accidentPos = inputPositions[0]
    policePos = inputPositions[1]
    policePos2 = inputPositions[2]
    outputDistances = np.zeros(6)
    accidentLane = 0
    if accidentPos > 1:
        accidentPos -= 1
        accidentLane = 1
    policeLane = 0
    if policePos > 1:
        policePos -= 1
        policeLane = 1
    policeLane2 = 0
    if policePos2 > 1:
        policePos2 -= 1
        policeLane2 = 1
    outputDistances[0] = np.abs(0.5 - accidentPos)
    outputDistances[2] = np.abs(policePos - accidentPos)
    outputDistances[4] = np.minimum(np.abs(policePos2 - accidentPos),outputDistances[2])
    if accidentLane == 0:
        outputDistances[1] = (2 - 0.5 + accidentPos) if (accidentPos < 0.5) else (accidentPos - 0.5)
        if policeLane == 0:
            outputDistances[3] = (2 - policePos + accidentPos) if (accidentPos < policePos) else (accidentPos - policePos)
        else:
            outputDistances[3] = policePos + accidentPos
        if policeLane2 == 0:
            policeDistance2 = (2 - policePos2 + accidentPos) if (accidentPos < policePos2) else (accidentPos - policePos2)
        else:
            policeDistance2 = policePos2 + accidentPos
        outputDistances[5] = np.minimum(outputDistances[3],policeDistance2)
    else:
        outputDistances[1] = 2 - 0.5 - accidentPos
        if policeLane == 1:
            outputDistances[3] = (2 + policePos - accidentPos) if (accidentPos > policePos) else (policePos - accidentPos)
        else:
            outputDistances[3] = 2 - policePos - accidentPos
        if policeLane2 == 1:
            policeDistance2 = (2 + policePos2 - accidentPos) if (accidentPos > policePos2) else (policePos2- accidentPos)
        else:
            policeDistance2 = 2 - policePos2 - accidentPos
        outputDistances[5] = np.minimum(outputDistances[3],policeDistance2)
    return outputDistances

def simulatePolicePatrol(sampleCount):
    rng = np.random.default_rng()
    randomPositions = rng.random((sampleCount,3))
    distances = np.apply_along_axis(computeDistances, 1, randomPositions)
    return np.average(distances, 0)


print(simulatePolicePatrol(1000000))
