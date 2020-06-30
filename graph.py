import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

# we already have the variable modelName
modelName = "model-1570499409"

def createAccLossGraph(modelName):
    contents = open("model.log", "r").read().split('\n')
    
    times = []
    accuarncies = []
    losses = []
    
    valAccs = []
    valLosses = []
    
    for c in contents:
        if modelName in c:
            name, timestamp, acc, loss, valAcc, ValLoss = c.split(",")
            
            times.append(float(timestamp))
            accuarncies.append(float(acc))            
            losses.append(float(loss))
            
            valAccs.append(float(valAcc))            
            valLosses.append(float(ValLoss))
            
    fig = plt.figure() #because we need more than one plot, if we need we would use plt.plot
    ax1 = plt.subplot2grid((2,1), (0,0))
    ax2 = plt.subplot2grid((2,1), (1,0), sharex = ax1)
    
    ax1.plot(times, accuarncies, label="acc")
    ax1.plot(times, valAccs, label="valAcc")
    ax1.legend(loc=2)
    
    ax2.plot(times, losses, label="loss")
    ax2.plot(times, valLosses, label="valLoss")
    ax2.legend(loc=2)
    
    #debug

    plt.show()

    
createAccLossGraph(modelName)
