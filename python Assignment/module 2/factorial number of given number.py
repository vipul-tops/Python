#factorial number of given number

n=int(input("Enter Any Number for Factorial : "))
fact = 1

for i in range(1,n+1):
    fact = fact * i

print ("The factorial of given number is : ",end="")
print (fact)
