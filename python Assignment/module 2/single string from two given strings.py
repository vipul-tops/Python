#single string from two given strings,separated by a space and swap the first two characters of each string

s1=input("Enter string 1 :")
s2=input("Enter string 2 :")

news1=s2[0:2]+s1[2:]
news2=s1[0:2]+s2[2:]
newstring=news1+','+news2

#print("newstring : ",news1,"",news2)
print("newstring : ",newstring)
