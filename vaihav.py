setA=set()#students's who play cricket
n1=int(input("enter no of element in setA = "))
for i1 in range(n1):
    element=input("item %i "%(i1+1))
    setA.add(element)
print(setA)    
setB=set()#students's who play badminton
n2=int(input("enter no of element in setB = "))
for i2 in range(n2):
    element=input("item %i "%(i2+1))
    setB.add(element)
print(setB)    
setC=set()#students's who play football
n3=int(input("enter no of element in setC = "))
for i3 in range(n3):
    element=input("item %i "%(i3+1))
    setC.add(element)
print(setC)    

#1.cricket and badminton ,A n B
setAnB=set()
for i in setA:
    if i in setB:
        setAnB.add(i)
print(setAnB)        

#2.cricket or badminton but not both ,A u B - A n B
setAB=set()
for i in setA:
    if i not in setB:
        setAB.add(i)
for i in setB:
    if i not in setA:
        setAB.add(i)
print(setAB)

#3.neither cricket nor badminton ,C - A -  B
setc=set()
for i in setC:
    if i not in setA:
        if i not in setB:
            setc.add(i)
print(setc)

#4.cricket and football but not badminton ,A n C - A n B n C
setAC=set()
for i in setA:
    if i in setC:
        if i not in setB:
            setAC.add(i)
print(setAC)


