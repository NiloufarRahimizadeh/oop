from tkinter import *
from Insert_into_table import Create



root =Tk()
l1 = Label(root, text="Name")
l1.grid(column=0, row=0)
sv_name = StringVar()
e1 = Entry(root, textvariable=sv_name)
e1.grid(column=1, row=0)

l2 = Label(root, text="Family")
l2.grid(column=0, row=1)
sv_family = StringVar()
e2 = Entry(root, textvariable=sv_family)
e2.grid(column=1, row=1)

l3 = Label(root, text="Age")
l3.grid(column=0, row=2)
sv_age = StringVar()
e3 = Entry(root, textvariable=sv_age)
e3.grid(column=1, row=2)

l4 = Label(root, text="Email")
l4.grid(column=0, row=3)
sv_email = StringVar()
e3 = Entry(root, textvariable=sv_email)
e3.grid(column=1, row=3)

b1 = Button(root, text="Register")
b1.grid(column=0, row=4, columnspan=2, sticky='we')

root.mainloop()