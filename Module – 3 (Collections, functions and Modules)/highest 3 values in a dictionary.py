#Write a Python program to find the highest 3 values in a dictionary


s={1:15,2:28,3:31,4:75,5:50}

d=list(s.values())
n=d.sort(reverse=True)

print(d)

print("Max high 3 value: ",d[0:3])



