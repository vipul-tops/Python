
#Write a python program to find the longest words

f=open("abc.txt","r")
s=f.read()
l=s.split()

print(s)
print(l)

n=int(input("Enter the value :"))

for i in l:
    if len(i)>n:
        print((i))
