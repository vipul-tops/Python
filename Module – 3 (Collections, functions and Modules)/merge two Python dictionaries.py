#Write a Python script to merge two Python dictionaries


d={"Ankit":2,"Hello":3}
d1={"Good":4,"moorning":5}

print(d | d1)


d={"A":1,"B":2}
d.update(d1)
print(d)
