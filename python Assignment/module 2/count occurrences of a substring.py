#Write a Python program to count occurrences of a substring in a string

s=input("Enter String : ")
substring=input("Enter substing : ")
if substring in s:
    print(s.count(substring))
else:
    print("Substring is not available")
