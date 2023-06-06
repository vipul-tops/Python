
#Write a Python program to write a list to a file.

l=["One","Two","Three","Four","Five","Six","Seven","Eigth","Nine","Ten"]

with open("abc.txt","w") as file:
    for i in l:
        
        file.write(f"{i}\n")
        

f=open("abc.txt")
print(f.read())
