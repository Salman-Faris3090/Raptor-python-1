# years from days

n=int(input("Enter the number of days: "))
y=n//365
m=(n-(y*365))//30
d=n-(y*365)-(m*30)
print(n,"days is:",y,"year",m,"month",d,"day")