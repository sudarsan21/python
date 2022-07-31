a=[[1,2,3],[4,5,6]]
b=[[1,2,3],[4,5,6,],[1,3,3]]
c=[[0,0,0],[0,0,0]]
m=len(a)
n=len(b)
for i in range(m):
    for j in range(len(b)):
        for k in range(n):
            c[i][j]+=a[i][k]*b[k][j]
print("The product of the two gien matrix is ")
for i in range(m):
    for j in range(len(b)):
        print(c[i][j],end=" ")
    print()