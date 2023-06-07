# Write a Python program to append text to a file and display the text.


def file(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Python Developer\n")
                myfile.write("File Handling")
        txt = open(fname)
        print(txt.read())
        
file('abc.txt')
