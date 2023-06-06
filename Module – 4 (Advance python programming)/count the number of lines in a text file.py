#Write a Python program to count the number of lines in a text file.


with open(r"abc.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)
