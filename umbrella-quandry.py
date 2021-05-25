import numpy as np
import matplotlib.pyplot as pyplot

#How many dry trips can a man take when only carrying an umbrella while it is raining?

def countDryDays(homeUmbrellas, workUmbrellas, rainChance):
    rng = np.random.default_rng()
    dryDays = 0
    currentLocation = "home"
    while homeUmbrellas >= 0 and workUmbrellas >= 0:
        dryDays += 1
        rainy = rng.random() < rainChance
        if currentLocation == "home":
            currentLocation = "work"
            if rainy:
                homeUmbrellas -= 1
                workUmbrellas += 1
        elif currentLocation == "work":
            currentLocation = "home"
            if rainy:
                workUmbrellas -= 1
                homeUmbrellas += 1
    return dryDays
    
sampleCount = 10000
probabilities = np.linspace(0.01,0.99,50)
dryDays_1_1 = np.zeros(50)
dryDays_2_2 = np.zeros(50)
for p in range(probabilities.size):
    for i in range(sampleCount):
        dryDays_1_1[p] += countDryDays(1,1,probabilities[p])
        dryDays_2_2[p] += countDryDays(2,2,probabilities[p])

avgDryDays_1_1 = dryDays_1_1/sampleCount
avgDryDays_2_2 = dryDays_2_2/sampleCount

pyplot.plot(probabilities,avgDryDays_1_1)
pyplot.plot(probabilities,avgDryDays_2_2)
pyplot.show()
