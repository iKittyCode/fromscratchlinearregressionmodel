import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("data.csv")


print(len(data.bx))
print(data.by[0])
def loss(m: float, b:float, data): 
    n = len(data.bx)
    aggregate = 0
    for i in range(0, len(data.by)): 
        aggregate += (data.by[i] - (m*data.bx[i] + b))^2
    return aggregate/len(data.by)
def gradient(m, b, data, learningrate):
    pb = 0
    pm = 0
    for i in range(0, len(data.bx)):
        pb += (data.by[i] - (m*data.bx[i] + b))
    pb = pb * (-2 / len(data.bx))
    for i in range(0, len(data.bx)):
        pm += data.bx[i] * (data.by[i] - (m * data.bx[i] + b))
    pm = pm* (-2 / len(data.bx))
    m = m - learningrate * pm
    b = b - learningrate * pb
    return m, b
epoch = 300
currentm = 1
currentb = 0
completed = False
for i in range(0, epoch):
    if i % 50 == 0: 
        print(i)
    if i % 300 == 0: 
        completed = True
    
    m, b = gradient(currentm, currentb, data, .0001)
    currentm = m
    currentb = b
if completed == True:

    print(currentb, currentm)


    



    
# print(loss(3, 2, data))
def linearfunc (m, b, x): 
    return m*x+b
xvalues = []
yvalues = []
for i in range(0,20): 
    xvalues.append(i)

    yvalues.append(linearfunc(currentm, currentb, xvalues[i]))

    
plt.scatter(data.bx, data.by)
plt.plot(xvalues, yvalues)
plt.show()




plt.scatter(data.bx, data.by)
plt.show()

