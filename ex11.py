n=int(input("Enter the number"))
a=[]
for i in range(n):
    x=int(input("Enter the next data:"))
    a.append(x)
print("The original list is:",a)
for  i in range(n):
    min=a[i]
    t=i
    for j in range(i+1,n):
        if min>a[j]:
            min=a[j]
            t=j
            a[t]=a[i]
            a[i]=min
print("The sorted list is :",a)
