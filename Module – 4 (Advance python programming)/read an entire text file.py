#Write a Python program to read an entire text file.


f = open("demo1.txt", "w")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demo1.txt", "r")
print(f.read())
