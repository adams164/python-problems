import numpy as np

#What is the probability that 5 judges make the correct decision (3/5), given their individual error rates of 95%,95%,90%,90%, and 80%?

def simulateJudges(accuracyRates, numSamples, lastJudgeCopies=False):
    rng = np.random.default_rng()
    numJudges = accuracyRates.size
    judgeVotes = rng.random((numSamples,numJudges)) < accuracyRates
    if lastJudgeCopies:
        judgeVotes[:,numJudges-1] = judgeVotes[:,0]
    successCount = np.sum(judgeVotes.sum(1) > (numJudges/2))
    overallAccuracy = successCount/numSamples
    return overallAccuracy
    
print(simulateJudges(np.array([0.95,0.95,0.9,0.9,0.8]),100000,True))
    