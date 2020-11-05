def lsearch(ar,item):
    i=0
    while i<len(ar) and ar[i]!=item:
        i+=1
    if i<len(ar):
        return i
    else:
        return false

#main
n=int(input("enter desired linear-list size(max. 50)...."))
print("\nenter element for linear list\n")
ar=[0]*n            #initialising list of size n with zeros
for i in range(n):
    ar[i]=int(input("element"+str(i)+":"))

item = int(input("\nenter element to be searched for..."))
index=lsearch(ar,item)

if index:
    print("\nelement found at index :",index,",position :",(index+1))
else:
          print("\nsorry!! given element could not be found.\n")
