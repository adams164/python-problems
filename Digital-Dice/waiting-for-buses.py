import numpy as np


#How long to wait for hourly bus lines at a stop?

def waitForBus(numLines):
    rng = np.random.default_rng()
    busStopTimes = rng.random(numLines-1)
    busStopTimes = np.append(busStopTimes,1.0)
    busStopTimes.sort()
    arrivalTime = rng.random()
    waitTimes = busStopTimes - arrivalTime
    firstArrival = np.nonzero(waitTimes > 0)[0][0]
    return waitTimes[firstArrival]
    
    
numSamples = 10000
totalWait = 0.0
busLines = 58
for i in range(numSamples):
    totalWait += waitForBus(busLines)
print(60*totalWait/numSamples)