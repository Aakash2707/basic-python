f=open("aakashgupta.txt",'w')
f.write('''my name is lakhan yo yo honey singh''')
f.close()

num=words=num_words=0
with open ("aakashgupta.txt",'r')as p:
    for line in p:
        words=line.split()
        num_words=len(words)
print ("there are ",num_words,"words")        
