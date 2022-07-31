n=int(input("Enter the number of data to sort:"))
a=[]
for i in range(n):
    x=int(input("Enter the next data:"))
    a.append(x)
x=int(input("Enter the element to search"))
for i in range (n):
    if a[i]==x:
        print("The element {} is present in position {}".format(x,i))
    else:
        print("The element is not present in list")
        break
if i==n-1:
    print("search failed")