a=int(input("Enter A :"))
b=int(input("Enter B :"))
if(a==b or a+b ==5 or a-b==5):
    print(True)
else:
    print(False)
print("----------------------")
a=int(input("Enter A : "))
b=int(input("Enter B : "))

def True_false(a,b):
    if(a==b or a+b ==5 or a-b==5):
        return True
    else:
        return False
#print(True_false(2,5))
print(True_false(a,b))
