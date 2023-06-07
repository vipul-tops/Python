#Write a Python program to read first n lines of a file

n=int(input("\nEnter Line to read :"))
f=open("abc.txt","r")
for i in range(n):
    print(f.readline())

f.close()    
print("-------------------------------------")
def nlines(f,nline):
    from itertools import islice
    with open(f) as file:
        for i in islice(file,nline):
            print(i)
            
nlines('abc.txt',2)          


