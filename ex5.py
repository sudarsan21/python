s=input("Enter a string :")
s1=s
s2=len(s)
if s2>=3:
    if s[-3:]=="ing":
        s=s+"ly"
    else:
        s=s+"ing"
print("The given string is :",s1)
print("The modified string is:",s)
