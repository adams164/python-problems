import numpy as np
import matplotlib.pyplot as pyplot

#Investigate the behavior of estimate the total population size N based on a sample of size next

def estimatePopluationSize(samplePercentage):
    rng = np.random.default_rng()
    populationSize = rng.integers(100,1000)
    population = np.arange(populationSize)
    sampleSize = int(np.floor(samplePercentage*populationSize))
    sample = rng.choice(population,sampleSize,False)
    sizeEstimate = (sample.max()*(sampleSize+1)/sampleSize) - 1
    return (sizeEstimate-populationSize)/populationSize
    
sampleCount = 10000
percentage = 0.2
errors = np.zeros(sampleCount)
for i in range(sampleCount):
    errors[i] = estimatePopluationSize(percentage)

pyplot.hist(errors,100)
pyplot.show()