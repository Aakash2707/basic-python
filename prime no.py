# program for prime number
num= int (input("enter number"))
lim=int(num/2)+1
for i in rnge (2,lim):
    rem=num%i
    if rem== 0:
        print (num, "isnot prime ")
        break
    else :
        print (num," is prime ")
        
