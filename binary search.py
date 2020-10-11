def binsearch(ar,key,low,high):
    if low>high:
        return-999
    mid = int((low+high)/2)

    if key==ar[mid]:
        return mid
    elif key<ar[mid]:
        high=mid-1
        return binsearch(ar,key,low,high)
    else:
        low=mid+1
        return binsearch(ar,key,low,high)

#main
ary=[12,15,21,25,28,32,33,36,43,45]
item=int(input("enter search item:"))
res=binsearch(ary,item,0,len(ary)-1)
if res>=0:
    print(item,"found at index",res)
else:
    print("sorry!",item,"not found in array")
