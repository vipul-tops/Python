#Write a program to demonstrate the Python E-Note Book Console based application

d={}

while True:

    print("\n\t***--Welcome To Python E-Note--***")
    print("\n\t 1. for Generate E-Note \n\t 2. For View E-Note \n\t 3. For Search E-Note \n\t 4. For Delete E-Note \n\t 5. For Exit")

    n=int(input("\nEnter Your Choice : "))

    if n==1:
        print("\n~~Generate Note~~")
        nam=input("Enter Python E-Note Genetator Name : ")
        title=input("Enter Title Of E-Note : ")
        des=input("Enter E-Note Description : ")
        d.setdefault(nam,(title,des))
        print("Generate E-Note Successfully...")

    elif n==2:
        print("\n~~View E-Note~~")
        for i in d:
            print("E-Note Title : ",d[i][0])
            print("E-Note Description : ",d[i][1])
            print("E-Note Generator Name : ",i)
            print("------------------------------\n")

    elif n==3:
        print("\n~~Search E-Note~~")
        nam=input("Enter Generator Name for Search : ")
        if nam in d:
            print("Title : ",d[nam][0])
            print("Description : ",d[nam][1])

    elif n==4:
        print("\n~~Delete E-Note~~")
        nam=input("Enter Generator Name for Search : ")
        d.pop(nam)
        print("Delete E-Note Successfully......")
    elif n==5:
        print("\n~~Exit E-Note~~")
        input("\n press Enter")
        break

    else:
        print("\n\nInvalid Input")
