# normal palidrome
s= input("enter a string ")
l= len (s)
mid= l/2
rrev=-1
for a in range (mid):
    if s[a] ==s[rev]:
        a+=1
        rev-=1
    else:
        print("not pali..")
        break
else:
    print("palidrome")
