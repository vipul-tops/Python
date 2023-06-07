#Write a Python program to unzip a list of tuples into individual lists.


l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))


l = [("Vipul",30), ("Nandan",90), ("Raj",50)]
print(list(zip(*l)))
