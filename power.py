def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)

#main
print("enter only the positive number below")
num=int(input("enter base number:"))
p=int(input("enter raise to power of :"))
result=power(num,p)
print(num,"raise to poer of",p,"is",result)
