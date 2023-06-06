#Write a Python program to check whether an element exists within a tuple

t= (4,6,8,"Python",22,43,"Java",99,16)
print(t)

n= int(input("Enter Tuple Item to Find = "))

result =n in t

print("Does our tuple Contains the ", n, "? ", result)
