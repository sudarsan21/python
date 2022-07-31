n=int(input("Enter the first number in the range:"))
m=int(input("Enter the second number in the range:"))
for i in range(n,m+1):
    if i>2:
        for j in range (2,i):
            r=i%j
            if r==0:
                break
        if r!=0:
                print(i,end="")
    else:
                print(i,end="")