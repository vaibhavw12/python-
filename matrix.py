print("enter elements in matrix for adddition and subtraction")
A=[]
r1=int(input("enter no of rows in matrix A: "))
c1=int(input("enter no of coloumns in matrix A: "))
print("enter entries row wise")
for i in range(r1):
    a=[]
    for j in range(c1):
        a.append(int(input()))
    A.append(a) 
print()
B=[]
r2=int(input("enter no of rows in matrix B: "))
c2=int(input("enter no of coloumns in matrix B: "))
print("enter entries row wise")
for i in range(r2):
    b=[]
    for j in range(c2):
        b.append(int(input()))
    B.append(b) 
print()

#addition of two matrix
print("addition")
C=[]
for i in range(r1):
    c=[]
    for j in range(c1):
        c.append(A[i][j]+B[i][j])
    C.append(c)
print(C)
print()

#subbtraction of two matrix
print("subtraction")
D=[]
for i in range(r1):
    d=[]
    for j in range(c1):
        d.append(A[i][j]-B[i][j])
    D.append(d)
print(D)
print()


#multiplication of two matrix
print("enter elements in matrix for multiplication")
A=[]
r1=int(input("enter no of rows in matrix A: "))
c1=int(input("enter no of coloumns in matrix A: "))
print("enter entries row wise")
for i in range(r1):
    a=[]
    for j in range(c1):
        a.append(int(input()))
    A.append(a) 
print()
B=[]
r2=int(input("enter no of rows in matrix B: "))
c2=int(input("enter no of coloumns in matrix B: "))
print("enter entries row wise")
for i in range(r2):
    b=[]
    for j in range(c2):
        b.append(int(input()))
    B.append(b) 
print()

E=[] 
for i in range(r1):
    e=[]
    for j in range(c2):
        y=0
        for k in range(c1):
            y=y+A[i][k]*B[k][j]
        e.append(y)
    E.append(e)
print(E)
print()

#transpose of a matrix
print("enter elements in matrix to print its transpose")
A=[]
r1=int(input("enter no of rows in matrix : "))
c1=int(input("enter no of coloumns in matrix : "))
print("enter entries row wise")
for i in range(r1):
    a=[]
    for j in range(c1):
        a.append(int(input()))
    A.append(a) 
print()
B=[]
print("enter all the entries zero only")
for i in range(c1):
    b=[]
    for j in range(r1):
        b.append(int(input()))
    B.append(b) 
for i in range(r1):
    for j in range(c1):
        B[j][i]=A[i][j]
print(B)        


