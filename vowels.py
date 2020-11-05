f=open("aakashgupta.txt",'w')
f.write('''my name is lakhan yo yo honey singh''')
f.close()
a=open("aakashgupta.txt",'r')
vowels = "AEIOUaeiou"


text = a.readline()

countV = 0
for V in text:
    if V in vowels:
        countV += 1


print("The number of Vowels is: ",countV)
a.close()
