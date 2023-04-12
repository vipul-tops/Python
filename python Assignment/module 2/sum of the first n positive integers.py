#sum of the first n positive integers

num=int(input("Enter number : "))
sum=0

i=1

while (i<=num):
   sum=sum+i
   i=i+1
   
print("The sum of the first",num,"positive integers",sum)   

print("-------------------------------------------")

num = int(input("Enter a positive integer: "))
 
total = num * (num+1)/2
 
print("The sum of the first",num,"positive integers",total)
