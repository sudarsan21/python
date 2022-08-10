l=[]
n=int(input("Enter the number of words in the list:"))
print("Enter the words one by one:")
for i in range(n):
    w=input()
    l.append(w)
    x=l[0]
l1=len(x)
for j in l:
    l2=len(l)
    if l2 > l1:
        l1=12
        x=i
print("The longest word in the list {} is {}".format(l,x))