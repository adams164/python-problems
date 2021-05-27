import numpy as np
import matplotlib.pyplot as pyplot

#Parrando's Paradox
epsilon = 0.005
rng = np.random.default_rng()

def gameA():
    return rng.random() < 0.5 - epsilon
    
def gameB(money):
    if (money % 3) == 0:
        return rng.random() < 0.1 - epsilon
    else:
        return rng.random() < 0.75 - epsilon

def simulatePlay(numFlips):
    money = np.zeros(numFlips)
    for i in range(1,numFlips):
        if rng.random() > 0.5:
            money[i] = money[i-1] + (1 if gameA() else -1)
        else:
            money[i] = money[i-1] + (1 if gameB(money[i-1]) else -1)
    return money
    
sampleCount = 10000
flipCount = 100
money = np.zeros((sampleCount,flipCount))
for i in range(sampleCount):
    money[i,:] = simulatePlay(flipCount)
avgMoney = np.average(money,0)

pyplot.plot(np.arange(100),avgMoney)
pyplot.show()