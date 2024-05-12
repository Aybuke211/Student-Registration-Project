import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

def submitdata():
    stdname = e1.get()
    stdsurname = e2.get()
    stdbirth = e3.get()
    stdgender = e4.get()
    stdclass = e5.get()
    #stdcourse = e6.get()
    mysqldb = mysql.connector.connect(host="localhost",user="root",password="0651Aybuke0651",database="student_course")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO Students (first_name,last_name,birth_date,gender,class) VALUES (%s,%s,%s,%s,%s)"
        val = (stdname,stdsurname,stdbirth,stdgender,stdclass)
        mycursor.execute(sql,val)
        mysqldb.commit()
        messagebox.showinfo("information", "Record inserted successfully :)")

    except Exception as e:
        print (e)
        mysqldb.rollback()
        mysqldb.close()




root = Tk()
root.title("Student Registration System")
root.geometry("400x300")
global e1
global e2
global e3
global e4
global e5
#global e6

label1 = Label(root, text= "First Name")
label1.grid(row=0, column=0)
label2 = Label(root, text= "Last Name")
label2.grid(row=1, column=0)
label3= Label(root, text= "Birth Date")
label3.grid(row=2, column=0)
label4= Label(root, text= "Gender")
label4.grid(row=3, column=0)
label5= Label(root, text= "Class")
label5.grid(row=4, column=0)
#label6= Label(root, text= "Course")
#label6.grid(row=5, column=0)


e1 = Entry(root)
e1.grid(row=0, column=1)
e2 = Entry(root)
e2.grid(row=1, column=1)
e3 = Entry(root)
e3.grid(row=2, column=1)
e4 = Entry(root)
e4.grid(row=3, column=1)
e5 = Entry(root)
e5.grid(row=4, column=1)
#e6 = Entry(root)
#e6.grid(row=5, column=1)

Button(root, text="ADD", command=submitdata, height=3, width=13).place(x=10, y=180)
root.mainloop()