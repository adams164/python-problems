import numpy as np


# What is the probability that Bill and Lil's meeting times overlap?

sampleCount = 1000000;
rng = np.random.default_rng()

billArrival = rng.random(sampleCount)*30
lilArrival = rng.random(sampleCount)*30

overlap = billArrival - lilArrival
meetUpCondition = np.logical_and(overlap > -7, overlap < 5)

probability = meetUpCondition.sum()/sampleCount
print(probability)