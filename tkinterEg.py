from tkinter import *

root=Tk()
root.title("Billing Software")
root.geometry("1250x750")
root.resizable(width=False,height=False)
bg_color="blue"

title=Label(root,text="Billing Software",bg="Blue",fg="Red",font=("Arial",20,"bold"),relief="groove",bd="12")
title.pack(fill=X)

#product detail
F1=LabelFrame(root,text='Product Details',font=("Arial",20,'bold'),fg='gold',bg=bg_color,relief=RIDGE,bd=15)
F1.place(x=5,y=90,width=800,height=600)

item=Label(F1,text='Items',font=('Halvetic',25,'bold','underline'),fg='black',bg=bg_color)
item.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1,text='Number of Items',font=('Halvetic',25,'bold','underline'),fg='black',bg=bg_color)
n.grid(row=0,column=1,padx=20,pady=15)

cost=Label(F1,text='Cost of Items',font=('Halvetic',25,'bold','underline'),fg='black',bg=bg_color)
cost.grid(row=0,column=2,padx=20,pady=15)

#product
bread=Label(F1,text='Bread',font=('times new roman',20,'bold','underline'),fg='lawngreen',bg=bg_color)
bread.grid(row=1,column=0,padx=20,pady=15)
b_text=Entry(F1,font=('arial',15,'bold'),relief=SUNKEN,bd=7,justify=CENTER)
b_text.grid(row=1,column=1,padx=20,pady=15)
cb_text=Entry(F1,font=('arial',15,'bold'),relief=SUNKEN,bd=7,justify=CENTER)
cb_text.grid(row=1,column=2,padx=20,pady=15)


puff=Label(F1,text='Puff',font=('times new roman',20,'bold','underline'),fg='lawngreen',bg=bg_color)
puff.grid(row=2,column=0,padx=20,pady=15)
p_text=Entry(F1,font=('arial',15,'bold'),relief=SUNKEN,bd=7,justify=CENTER)
p_text.grid(row=2,column=1,padx=20,pady=15)
cp_text=Entry(F1,font=('arial',15,'bold'),relief=SUNKEN,bd=7,justify=CENTER)
cp_text.grid(row=2,column=2,padx=20,pady=15)

dabeli=Label(F1,text='Dabeli',font=('times new roman',20,'bold','underline'),fg='lawngreen',bg=bg_color)
dabeli.grid(row=3,column=0,padx=20,pady=15)
d_text=Entry(F1,font=('arial',15,'bold'),relief=SUNKEN,bd=7,justify=CENTER)
d_text.grid(row=3,column=1,padx=20,pady=15)
cd_text=Entry(F1,font=('arial',15,'bold'),relief=SUNKEN,bd=7,justify=CENTER)
cd_text.grid(row=3,column=2,padx=20,pady=15)

sandwitch=Label(F1,text='Sandwitch',font=('times new roman',20,'bold','underline'),fg='lawngreen',bg=bg_color)
sandwitch.grid(row=4,column=0,padx=20,pady=15)
s_text=Entry(F1,font=('arial',15,'bold'),relief=SUNKEN,bd=7,justify=CENTER)
s_text.grid(row=4,column=1,padx=20,pady=15)
cs_text=Entry(F1,font=('arial',15,'bold'),relief=SUNKEN,bd=7,justify=CENTER)
cs_text.grid(row=4,column=2,padx=20,pady=15)

vadapav=Label(F1,text='Vadapav',font=('times new roman',20,'bold','underline'),fg='lawngreen',bg=bg_color)
vadapav.grid(row=5,column=0,padx=20,pady=15)
v_text=Entry(F1,font=('arial',15,'bold'),relief=SUNKEN,bd=7,justify=CENTER)
v_text.grid(row=5,column=1,padx=20,pady=15)
cv_text=Entry(F1,font=('arial',15,'bold'),relief=SUNKEN,bd=7,justify=CENTER)
cv_text.grid(row=5,column=2,padx=20,pady=15)


t=Label(F1,text='Total Price',font=('times new roman',20,'bold','underline'),fg='lawngreen',bg=bg_color)
t.grid(row=7,column=0,padx=20,pady=15)
t_text=Entry(F1,font=('arial',15,'bold'),relief=SUNKEN,bd=7,justify=CENTER)
t_text.grid(row=7,column=1,padx=20,pady=15)
ct_text=Entry(F1,font=('arial',15,'bold'),relief=SUNKEN,bd=7,justify=CENTER)
ct_text.grid(row=7,column=2,padx=20,pady=15)

#Bill Area

F2=Frame(root,relief=GROOVE,bd=18)
F2.place(x=820,y=90,width=430,height=600)
bill_title=Label(F2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack()









