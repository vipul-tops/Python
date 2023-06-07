#Write a Python program to remove duplicates from a list

l = [1,3,15,6,3,5,26,6,1]
print(l)

res = []
[res.append(x) for x in l if x not in res]

print (str(res))
