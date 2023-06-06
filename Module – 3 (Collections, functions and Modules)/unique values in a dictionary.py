#Write a Python program to print all unique values in a dictionary. 


l =[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI": "S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
print("List: ",l)
uni= set(val for dic in l for val in dic.values())
print("Unique Values: ",uni)


#
d= {'a': 1, 'b': 2, 'c': 3, 'd': 2,'e':4,'f':3}

uni_values= set()

for value in d.values():
  uni_values.add(value)
  
print(uni_values)
