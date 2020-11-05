s=input("enter a string ")
length=len(s)
a=0
end=length
s2=''
while a<length :
    if a == 0:
        s2+=s[0].upper()
        a+=1
    elif(s[a]=='' and s[a+1]!=''):
        s2+=[a]
        s2+=s[a+1].upper()
        a+=1
print ("capitalised string",s2)
