#Write a Python program to convert a list of tuples into a dictionary


l=[("Nimesh",15),("Sanjay",35),("Yash",38),("Vihl",50), ("Prakash",25)]

d= dict()
 
for name, age in l:
    d.setdefault(name, []).append(age)
print(d)


#

l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)
