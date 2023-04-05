#swap two number with temp variable and without temp variable

x = input("Enter value of x: ")
y = input("Enter value of y: ")

temp = x
x = y
y = temp

print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))

a=int(input("Enter A : "))
b=int(input("Enter B : "))

a, b = b, a
print("a = ", a)
print("b = ", b)
