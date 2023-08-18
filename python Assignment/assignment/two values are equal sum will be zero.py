''' Write a Python program to sum of three given integers. However, if 
two values are equal sum will be zero'''


a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))

if a==b or b==c or c==a:
      print("0")
else:
    d=a+b+c
    print(d)
