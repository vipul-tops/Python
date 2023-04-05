#sum of three given integers. However, if two values are equal sum will be zero

a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))

if a==b and b==c and a==c:
    print("Addition : ",a+b+c)
else:
    print("0")
