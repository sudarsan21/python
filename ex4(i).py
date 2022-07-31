n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
print("The numbers which are divisible by 3 but  noot multiple of 5 are:")
for i in range(n1,n2+1):
    if i%5!=0 and i%3==0:
        print(i,'\t',end="")

