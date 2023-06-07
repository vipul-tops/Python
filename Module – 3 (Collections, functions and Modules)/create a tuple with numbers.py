# Write a Python program to create a tuple with numbers.


t=()
n = int(input("Please enter the Total Tuple Items to store = "))
for i in range(1,n+ 1):
    num= int(input("Please enter %d Tuple Item = " %i))
    t += (num,)

print("Tuple = ",t)
