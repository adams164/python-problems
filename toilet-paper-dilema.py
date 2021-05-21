import numpy as np
import matplotlib.pyplot as plt


# For two toilet paper rolls of equal length, given two types of users who select either the larger or the smaller roll compute the length of paper left on the other roll when one is emptied.

def computeLength(p,length):
    lengthRemaining = np.zeros((length,length))
    for i in range(length):
        for j in range(length):
            if i == 0:
                lengthRemaining[i,j] = j
            elif j == 0:
                lengthRemaining[i,j] = i
            elif i == j:
                lengthRemaining[i,j] = lengthRemaining[i,j-1]
            elif j > i:
                lengthRemaining[i,j] = p*lengthRemaining[i,j-1] + (1-p)*lengthRemaining[i-1,j]
            elif i > j:
                lengthRemaining[i,j] = lengthRemaining[j,i]
    return lengthRemaining[length-1,length-1]

probability = np.arange(100)/100
finalLength = np.zeros(100)
for i in range(100):
    finalLength[i] = computeLength(probability[i],200)
plt.plot(probability,finalLength)
plt.show()