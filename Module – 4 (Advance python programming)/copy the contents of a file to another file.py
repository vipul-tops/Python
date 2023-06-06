#Write a Python program to copy the contents of a file to another file

with open("abc.txt","r") as firstfile,open("s.txt","a") as secondfile:
    for i in firstfile:
        
        secondfile.write(i)
