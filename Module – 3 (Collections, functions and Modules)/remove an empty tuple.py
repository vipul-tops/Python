#Write a Python program to remove an empty tuple(s) from a list of tuples. 



tuples= [(), ('Aksh','15'), (), ('Vihol', 'sita'),
          ('krishna', 'Manav', '45'), ('',''),()]

tuples=[t for t in tuples if t]
print(tuples)


#

def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
 
tuples = [(), ('ram','15'), (), ('laxman', 'sita'),
          ('krishna', '45'), ('',''),()]

print(Remove(tuples))
