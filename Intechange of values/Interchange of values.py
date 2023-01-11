# interchanging two numbers

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("The two numbers are:",a,",",b)
a=a+b
b=a-b
a=a-b
print("The numbers after interchanging=",a,",",b)