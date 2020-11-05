# calculate sin taylor series by using for loop in python
from math import*

print ("sine taylor series is=")

x=float(input("enter value of x="))

for k in range(0,10,1):
    y=((-1)**k)*(x**(1+2*k))/factorial(1+2*k)

    print (y)
