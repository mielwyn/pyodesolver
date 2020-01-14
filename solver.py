import numpy as np
import matplotlib.pyplot as plt
#bounds are inclusive
def integrate(lower,upper,dvar,func):
    x = np.arange(lower,upper+dvar,dvar)
    y = []
    sum = 0
    for val in x:
        sum = sum + func(val)*dvar
        y.append(sum)
    y = np.asarray(y)
    return x, y
def plot(x,y):
    plt.plot(x,y)
    plt.xticks(np.arange(x[0],x[len(x)-1]+x[1]-x[0],(x[len(x)-1]-x[0])/10))
    plt.yticks(np.arange(y[0],y[len(y)-1],(y[len(y)-1]-y[0])/10))
    plt.show()
twox = lambda x: 2*x
x,y = integrate(0,2,.00001,twox)
plot(x,y)
etothex = lambda x: np.power(np.e,x)
x,y = integrate(0,1,.00001,etothex)
plot(x,y)
