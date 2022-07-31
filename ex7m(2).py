L=[]
N=int(input("Enter the total number of list elements:"))
print("Enter the elements one by one:")
for i in range(N):
    x=int(input())
    L.append(x)
print("The original list is:",L)
print("The reversed list is:",end="")
for i in range (N-1,-1,-1):
    print(L[i],"\t",end="")