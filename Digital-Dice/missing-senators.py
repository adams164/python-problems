import numpy as np
import random

#For a given bill where A out of 100 senators oppose the bill and M senators are missing, what are the odds the bill does not pass?

def simulateVotes(oppositionCount, missingCount):
    senatorList = np.ones(100)
    senatorList[0:oppositionCount] = -1
    missingSenators = random.sample(range(100),missingCount)
    senatorList[missingSenators] = 0
    return senatorList.sum() < 0
    
sampleCount = 100000
failures = 0
for i in range(sampleCount):
    if simulateVotes(49,4):
        failures += 1
        
print(failures/sampleCount)