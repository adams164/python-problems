import numpy as np
import random
#Given two matchbooks with 40 matches each, how many matches can be lit by selecting a match from one book at random until one of the matchbooks is empty?

def simulateMatchUse():
    matchbooks = np.array([40,40])
    matchesLit = 0
    while np.all(matchbooks > 0):
        matchesLit += 1
        matchbooks[random.randint(0,1)] -= 1
    return matchesLit

sampleCount = 1000
totalMatches = 0
for i in range(sampleCount):
    totalMatches += simulateMatchUse()
print(totalMatches/sampleCount)