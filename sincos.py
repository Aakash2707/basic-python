import matplotlib.pyplot as plt
from numpy import sin,cos,arange
from math import inf
import random
x=arange(0,10,0.1)
a=cos(x)
b=sin(x)
plt.plot(x,a,linewidth=2)
plt.plot(x,b,linewidth=2)
plt.show()
