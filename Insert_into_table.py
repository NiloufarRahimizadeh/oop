import pymysql
from tkinter import *


def Register(a, b, c):
    data = (a.get(), b.get(), c.get())
    with connection.cursor() as cr:
        cr.execute(sql, data)
        connection.commit()

    

connection = pymysql.connect(host='localhost', user='poulstar', password='poulstar', database='gpn')

sql = "INSERT INTO `users` (`id`, `email`, `password`) VALUES (%s, %s, %s)"

root = Tk()

l1 = Label(root, text='ID')
l1.grid(row=0, column=0)

var1 = StringVar()
e1 = Entry(root, textvariable=var1)
e1.grid(row=0, column=1)

l2 = Label(root, text='Name')
l2.grid(row=1, column=0)

var2 = StringVar()
e2 = Entry(root, textvariable=var2)
e2.grid(row=1, column=1)

l3 = Label(root, text='Name')
l3.grid(row=2, column=0)

var3 = StringVar()
e3 = Entry(root, textvariable=var3)
e3.grid(row=2, column=1)


b1 = Button(root, text='Register', command= lambda: Register(var1, var2, var3))
b1.grid(row=3, column=0, columnspan=2)
root.mainloop()



