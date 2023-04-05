from tkinter import *

root=Tk()
root.title("MY TKINTER TITLE")
root.geometry("420x450")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="First Name")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="Last Name")
l_lname.place(x=50,y=150)

l_email=Label(root,text="Email")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="Mobile")
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text="Insert",fg="white",bg="black")
insert.place(x=50,y=300)

insert=Button(root,text="Search",fg="white",bg="black")
insert.place(x=100,y=300)

insert=Button(root,text="Submit",fg="white",bg="black")
insert.place(x=156,y=300)

insert=Button(root,text="Delete",fg="white",bg="black")
insert.place(x=214,y=300)
