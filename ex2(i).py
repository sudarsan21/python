year=int(input("Enter the Year"))
if((year%4==0 and year%100!=0)or year%400==0):
    print("The given year {} is leap ".format(year))
else:
    print("The given year {}  is not leap".format(year))