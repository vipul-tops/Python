#l1 and l2 common elements are show in l3

l1=[10,20,30,40,50,60]
l2=[12,40,50,20,35]
l3=[]

for i in l1:
    if i in l2:
        l3.append(i)

print(l3)
