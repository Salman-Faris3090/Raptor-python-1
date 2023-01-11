# Time Conversion

t=int(input("Enter time in Seconds="))
import math
h=math.floor(t/3600)
m=math.floor((t%3600)/60)
s=math.floor((t%3600)%60)
print("Time=",h,"hr",m,"min",s,"sec")