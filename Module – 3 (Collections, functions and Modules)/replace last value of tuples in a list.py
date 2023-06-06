#Write a Python program to replace last value of tuples in a list

a=[(1, 2, 3), (4, 5, 6), (7, 8, 9)]

print(a)

b=[(t[0],t[1],) + (100,) for t in a]

print(b)
