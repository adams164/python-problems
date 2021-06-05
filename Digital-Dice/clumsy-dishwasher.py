import numpy as np
import random

#Given a kitchen with 5 dishwashers, what is the probability that out of 5 broken dishes 4 of them are broken by one individual?

def simulateBreaks(dishwashers, breaks):
    breakCounts = np.zeros(dishwashers);
    for i in range(breaks):
        index = random.randint(0,dishwashers-1)
        breakCounts[index] += 1
    return breakCounts

fourBreakCount = 0

for i in range(100000):
    numBreaks = simulateBreaks(5,5)
    if numBreaks[0] >= 4:
        fourBreakCount += 1

probability = fourBreakCount/100000

print("Probability that one dishwasher breaks at least 4 of 5 dishes: ", probability);