'''Write a Python program to create a dictionary from a string
Note: Track the count of the letters from the string. 
Sample string: 'w3resource' '''

from collections import defaultdict, Counter

str1 = 'w3resource' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)


#
s=input("Enter a string :")
d={}
for ch in s:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print(d)        



