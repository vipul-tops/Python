#function to reverses a string if its length is a multiple of 4

def reverse(string):
    if len(string)%4==0:
        string=''.join(reversed(string))
        print(string)
       
    else:
        print(string)
        
s=input("Enter a string :")
reverse(s)
