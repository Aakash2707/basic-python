z=open("test1.txt",'w')
z.writelines("pelllu \n")
z.writelines("elllu \n")
z.writelines("allppplu \n")
z.close()


f=open('test1.txt','r')
l=f.readlines()
f.close()
for x in range (0,len(l)):
   if 'a'in l[x] or 'A' in l[x]:
      f=open('test2.txt','a')
      f.write(l[x])
      f.close()
   elif 'a' not in  l[x] or 'A' not in l[x]:
      f=open('test1.txt','w')
      f.write(l[x])
      f.close()
