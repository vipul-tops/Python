#Write a Python program to find the repeated items of a tuple.

t=(1,2,3,4,5,6,1,1,1,1,3,4,8,9,0)
print("Tuple : ",t)
#print("Enter the items you will count : ",t.count(1))
l=int(input("Enter element items you will count :"))
count=t.count(l)
print(l,"appears",count,"times in tuple")



unique_edges=[('SLT2', 'SDP1'),('GCD7', 'ATG34'),('MTH1', 'MTH1'),('ADY2', 'ADY2')]
homo_dimers = list(map(tuple,unique_edges))
homo_dimers = [(a, b) for a, b in unique_edges if a == b]
print(homo_dimers)


t=("Sl","Sd","Gc","At","Mt","Sl","Gc")
t1=(map(tuple,t))
t1=[a for a in t if a==a]
print(t1)
