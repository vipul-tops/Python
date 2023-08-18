#  swap two number with temp variable and without temp variable.

a=10
b=20

a,b=b,a

print("A : ",a)
print("B : ",b)

print("")
# without using temp

num1=10
num2=20

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("num1 : ",num1)
print("num2 : ",num2)

print("")

# with temp variable
a=5
b=10

temp=a
a=b
b=temp

print("a : ",a)
print("b : ",b)
