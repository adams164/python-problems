import numpy as np

#For 3 players with l,m, and n coins each, how many rounds does it take on average for one player to go broke?


def playGame(l,m,n,p):
    rng = np.random.default_rng()
    rounds = 0
    playerState = np.array([l,m,n])
    while np.all(playerState > 0):
        flips = rng.random(3) > p
        if flips.any() and not flips.all():
            if flips.sum() == 1:
                winner = np.argwhere(flips)
            else:
                winner = np.argwhere(~flips)
            playerState -= 1
            playerState[winner] += 3
        rounds += 1
    return rounds


l = 4
m = 7
n = 9
p = 0.5
sampleCount = 10000
roundCount = 0
for i in range(sampleCount):
    roundCount += playGame(l,m,n,p)
print(roundCount/sampleCount)