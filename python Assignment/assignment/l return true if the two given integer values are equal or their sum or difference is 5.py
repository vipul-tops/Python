'''Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5 '''


a=int(input("Enter A : "))
b=int(input("Enter B : "))

if a==b or a+b==5 or a-b==5 or b-a==5:
    print("True ")

else:
    print("False")
