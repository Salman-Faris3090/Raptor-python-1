a=int(input("Enter First side="))
b=int(input("Enter Second side="))
c=int(input("Enter Third side="))
per=a+b+c
s=per/2
import math
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of a triangle=",area)
print("Perimeter of a triangle=",per)