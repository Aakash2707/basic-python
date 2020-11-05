def compute(num):
    if (num==1):
        return 1
    else:
        return(num+compute(num-1))

#main
last=4

ssun=compute(last)

print("the sum of the series from 1...",last,"is",ssun)
