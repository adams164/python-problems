import numpy as np

#How long on average will you wait at a deli counter?

def simulateDeli(customerRate,serviceRate):
    rng = np.random.default_rng()
    customerIntervals = np.cumsum(np.ceil(-3600*np.log(rng.random((30*customerRate)))/customerRate))
    serviceIntervals = np.ceil(-3600*np.log(rng.random((30*customerRate)))/serviceRate)
    queue = np.zeros((200,2))
    clerk1Busy = False
    clerk1TaskTime = 0
    clerk1IdleTime = 0
    clerk2Busy = False
    clerk2TaskTime = 0
    clerk2IdleTime = 0
    queueLength = 0
    totalQueueLength = 0
    maxQueueLength = 0
    totalTime = 0
    maxTotalTime = 0
    customerNumber = 0
    for sec in range(36000):
        if clerk1TaskTime > 0:
            clerk1TaskTime -= 1
        if clerk2TaskTime > 0:
            clerk2TaskTime -= 1
        if (not clerk1Busy or not clerk2Busy) and queueLength > 0:
            if not clerk1Busy:
                clerk1TaskTime = queue[0,1]
                clerk1Busy = True
            else:
                clerk2TaskTime = queue[0,1]
                clerk2Busy = True
            customerWaitTime = queue[0,0] + queue[0,1]
            totalTime = totalTime + customerWaitTime
            maxTotalTime = max(maxTotalTime,customerWaitTime)
            queueLength -= 1
            for index in range(199):
                queue[index,:] = queue[index+1,:]
        if sec == customerIntervals[customerNumber]:
            if clerk1Busy and clerk2Busy:
                queue[queueLength,0] = 0
                queue[queueLength,1] = serviceIntervals[customerNumber]
                queueLength += 1
                maxQueueLength = max(maxQueueLength,queueLength)
            else:
                if not clerk1Busy:
                    clerk1TaskTime = serviceIntervals[customerNumber]
                    clerk1Busy = True
                else:
                    clerk2TaskTime = serviceIntervals[customerNumber]
                    clerk2Busy = True
                totalTime += serviceIntervals[customerNumber]
                maxTotalTime = max(maxTotalTime, serviceIntervals[customerNumber])
            customerNumber += 1
        totalQueueLength += queueLength
        if not clerk1Busy:
            clerk1IdleTime += 1
        if not clerk2Busy:
            clerk2IdleTime += 1
        queue[:,0] += 1
        if clerk1TaskTime <= 0:
            clerk1Busy = False
        if clerk2TaskTime <= 0:
            clerk2Busy = False
    averageTotalTime = totalTime/(customerNumber - queueLength)
    averageQueueLength = totalQueueLength / 36000
    print("Average Wait Time: ",averageTotalTime)
    print("Max Wait Time: ",maxTotalTime)
    print("Average Queue Length: ", averageQueueLength)
    print("Max Queue Length: ",maxQueueLength)
    print("Clerk 1 idle time: ", clerk1IdleTime)
    print("Clerk 2 idle time: ", clerk2IdleTime)
    print("Total Customers Served: ", customerNumber - queueLength)
    print("Total Service Time: ", np.sum(serviceIntervals[0:(customerNumber-queueLength)]))

simulateDeli(30,40)