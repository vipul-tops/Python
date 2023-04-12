#list comprehensive

#task=1
l=[]
for i in range(100):
    if i%3==0:
        l.append(i)
print(l)

l2=[i for i in range(100) if i%3==0]
print(l2)

print("--------")
#task=2
l=[i for i in range(100) if i%2==0]
l1=[i for i in range(100) if i%2!=0]
print("Even :",l)
print("Odd :",l1)

print("--------")
#task=3
l=[c for c in "vipul memakiya"]
print(l)

print("--------")
#task=4

l=[i*10 for i in range(1,6)]
print(l)

print("--------")
#task=5
l=["Aksh","Manav","Yash","Vipul","Kishor"]
l2=[c for c in l if "s" in c]
print(l2)

