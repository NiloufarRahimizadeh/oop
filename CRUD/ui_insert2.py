from tkinter import *
import pymysql


con = pymysql.connect(host="localhost", user="poulstar", password="poulstar", database="my_db_n")

def add():
    sql = "INSERT INTO users1(name, family, age) VALUES(%s,%s,%s)"
    data =(var1.get(), var2.get(), var3.get())
    try:
        with con.cursor() as cr:
            cr.execute(sql, data)
            con.commit()
    except:
        print("Access denied!")

def update(n,f,a,i):
    sql = "UPDATE users1 SET name=%s, family= %s, age=%s WHERE id=%s"
    with con.cursor() as cr:
        data= (f,n,a,i)
        cr.execute(sql,data)
        con.commit()
 

def delete(i):
    sql = "DELETE from users1 WHERE id=%s"
    with con.cursor() as cr:
        data= (i)
        cr.execute(sql,data)
        con.commit()
       

def select(i):
    sql = "SELECT * from users1 WHERE id=%s"
    with con.cursor() as cr:
        data = (i)
        cr.execute(sql, data)
        result = cr.fetchall()
        print(result)

root = Tk()

l1 = Label(root, text="Name: ")
l1.grid(row=0, column=0)

var1 = StringVar()
e1 = Entry(root, textvariable=var1)
e1.grid(row=0, column=1)

l2 = Label(root, text="Family: ")
l2.grid(row=1, column=0)

var2 = StringVar()
e2 = Entry(root, textvariable=var2)
e2.grid(row=1, column=1)

l3 = Label(root, text="Age: ")
l3.grid(row=2, column=0)

var3 = StringVar()
e3 = Entry(root, textvariable=var3)
e3.grid(row=2, column=1)

b1 = Button(root, text="Register", command=add)
b1.grid(row=3, column=0, columnspan=2, sticky='we')

b2 = Button(root, text="Update", command= lambda: update(var1.get(), var2.get(), var3.get(), int(var7.get())))
b2.grid(row=4, column=0, columnspan=2, sticky='we')

b3 = Button(root, text="Delete", command= lambda: delete(int(var7.get())))
b3.grid(row=5, column=0, columnspan=2, sticky='we')

b4 = Button(root, text="Select", command= lambda: select(int(var7.get())))
b4.grid(row=6, column=0, columnspan=2, sticky='we')

l7 = Label(root, text="Id: ")
l7.grid(row=7, column=0)
var7 = StringVar()
e7 = Entry(root, textvariable=var7)
e7.grid(row=7, column=1)
root.mainloop()