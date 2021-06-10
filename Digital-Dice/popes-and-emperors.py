import numpy as np

# Compute the probability that a leader is elected from N people where M votes are needed, when votes are only cast for a subset of size n

def runElection(numVoters,votesNeeded,numElectable,selfVoting=True):
    rng = np.random.default_rng()
    candidates = np.zeros(numElectable)
    #votes = rng.integers(0,numElectable,numVoters)
    for index in range(numVoters):
        if (index < numElectable) and not selfVoting:
            vote = (rng.integers(1,numElectable) + index) % numElectable
        else:
            vote = rng.integers(0,numElectable)
        candidates[vote] += 1
    return np.any(candidates >= votesNeeded)
    
numSamples = 100000
totalElections = 0
for i in range(numSamples):
    if runElection(25,17,2,False):
        totalElections += 1
    
print(totalElections/numSamples)
    