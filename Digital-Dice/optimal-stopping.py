import numpy as np


#Determine the optimal stopping point for a population of size N

def simulateSearch(populationSize,topNum=1):
    rng = np.random.default_rng()
    population = rng.permutation(populationSize)
    bestChoice = np.zeros(populationSize)
    for sampleSize in range(populationSize):
        sample = population[0:sampleSize]
        selectionPool = population[sampleSize:]
        if sample.size > 0:
            bestSample = sample.max()
        else:
            bestSample = -1
        
        possibleSelections = selectionPool[selectionPool > bestSample]
        if possibleSelections.size > 0:
            bestChoice[sampleSize] = possibleSelections[0]
        else:
            bestChoice[sampleSize] = population[-1]
    return bestChoice >= (populationSize - topNum)
    
    
sampleCount = 10000
populationSize = 50
choices = np.zeros(populationSize)
for i in range(sampleCount):
    choices += simulateSearch(populationSize,1)

print(choices/sampleCount)
print(choices.argmax())