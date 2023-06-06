"""Write a Python function that takes two lists and returns true if they have 
at least one common member."""

list1=[11,2,3,44,5,6,10]
list2=[1,11,14,6,45]

for x in list1:
    for y in list2:
        if x == y:
            print("True")
