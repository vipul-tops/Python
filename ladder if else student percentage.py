#ladder if else

rno=int(input("Enter Roll No.: "))
sname=(input("Student Name : "))
s1=int(input("Subject 1 : "))
s2=int(input("Subject 2 : "))
s3=int(input("Subject 3 : "))

total=s1+s2+s3
per=total/3

print("Student Name : ",sname)
print("Roll No. : ",rno)
print("Toatl : ",total)
print("Percentage : ",per)

if per>=70:
    print("Distiction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second class")
elif per>=40:
    print("Pass")
else:
    print("Fail")
