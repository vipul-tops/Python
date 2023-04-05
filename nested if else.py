#greater number using of Nested if else

a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))

if a>b:
    if a>c:
        print(a,"Is Greater Number")
    else:
        print(c,"Is Greater Number")
elif b>c:
    print(b,"Is Greater Number")
else:
    print(c,"Is Greater Number")
