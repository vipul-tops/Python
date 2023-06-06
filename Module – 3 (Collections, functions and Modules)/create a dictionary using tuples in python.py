
#How will you create a dictionary using tuples in python



t=(("Python",1),("Java",2),("Flutter",3))
print(type(t))

d = dict((key, value) for value,key in t)
print(d)
print(type(d))

    
