#Factorial number of given number

n=int(input("Enter Number : "))
fact=1

for i in range(1,n+1):
    
    fact=fact*i
print("factorial : ",fact)
    
