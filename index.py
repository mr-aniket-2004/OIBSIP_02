from tkinter import *
from tkinter.ttk import *
import sqlite3
# import tkMessageBox

def cal():
    result=Label(root,text="")
    result.grid(row=12,column=1,columnspan=3)
    frist = fname.get()
    last = lname.get()
    heigth =float(heigthentry.get())
    heigthlist = str(heigth)
    weigth = float(widthentry.get())
    widthlist = str(weigth)
    sum = weigth/(heigth*heigth)
    final = round(sum,2)
    finallist =str(final)
    def status():
        if final < 18.4:
            value = "UNDER WEIGTH"
            return value

        elif (final>18.5 and final<24.9):
            value = "NORMAL"
            return value

        elif (final>25.0 and final<39.9):
            value = "OVER WEIGTH"
            return value

        elif final>=40:
            value = "OBSESE"
            return value

    value = status()
    valuelast = str(value)
    result =Label(root,text=f"{frist} {last} BMI : {final} It's {value}")
    result.grid(row=12,column=1,columnspan=3)

    # this is quary for insert in table

    conn = sqlite3.connect("BMIData.db")
    c= conn.cursor()
    c.execute("INSERT INTO users VALUES('"+frist+"','"+last+"','"+heigthlist+"','"+widthlist+"','"+finallist+"','"+valuelast+"')")
    conn.commit()
    conn.close()
    


    
def show():
    new =Tk()
    new.title("BMI CALCULATOR HISTOR")
    new.geometry("600x500")

    l1 = Label(new, text="RECORDS OF BMI CALCULATIONS.. " ,font=" time 20 bold", background="red")
    l1.grid(row=1, column= 1,columnspan=6,padx=50)

    row = Label(new, text="FRIST_NAME ",font=" time 10 bold")
    row.grid(row=2,column=1,pady=20)

    row = Label(new, text="LAST_NAME ",font=" time 10 bold")
    row.grid(row=2,column=2)

    row = Label(new, text="HEIGTH ",font=" time 10 bold")
    row.grid(row=2,column=3)

    row = Label(new, text="WEIGTH ",font=" time 10 bold")
    row.grid(row=2,column=4)

    row = Label(new, text="BMI_VALUE",font=" time 10 bold")
    row.grid(row=2,column=5)

    row = Label(new, text="STATUS",font=" time 10 bold")
    row.grid(row=2,column=6)

    # this is quary for delete the rows

   


    conn = sqlite3.connect("BMIData.db")
    c= conn.cursor()
    c.execute("SELECT * FROM users")
    r = c.fetchall()
    num =3
    for i in r:
        FRIST_NAME = Label(new, text=i[0])
        FRIST_NAME.grid(row=num,column=1)

        LAST_NAME = Label(new, text=i[1])
        LAST_NAME.grid(row=num,column=2)

        HEIGTH = Label(new,text=i[2])
        HEIGTH.grid(row=num, column=3)

        WEIGTH = Label(new,text=i[3])
        WEIGTH.grid(row=num, column=4)

        BMI_VALUE = Label(new, text=i[4])
        BMI_VALUE.grid(row=num,column=5)

        STATUS = Label(new, text=i[5])
        STATUS.grid(row=num,column=6)
        num = num+1

    new.mainloop()

root = Tk()
root.title("BMI CALCULATOR")
root.geometry("500x500")
h =IntVar()
w=IntVar()
r=IntVar()

# THIS IS QUARY FOR CREATE TABLE

# conn = sqlite3.connect("BMIData.db")
# c= conn.cursor()
# c.execute("CREATE TABLE users(first_name TEXT,last_name TEXT, heigth INT, weigth INT,BMI INT , value INT)")
# # tkMessageBox.showinfo("Information","Your details is save !")
# conn.commit()
# conn.close()



title = Label(root,text="SEE YOUR BMI",background="red",font="time 10 bold")
title.grid(row=2,column=1,pady=20,padx=20,columnspan=2)

width =Label(root,text="First_name :",font="time 10 bold")
width.grid(row=3,column=1,padx=30,pady=5)
fname = Entry(root,width=40)
fname.grid(row=3,column=2)

width =Label(root,text="Last_name :",font="time 10 bold")
width.grid(row=4,column=1,padx=30,pady=10)
lname = Entry(root ,width=40)
lname.grid(row=4,column=2)


width =Label(root,text="Enter your Width (in KG) :",font="time 10 bold")
width.grid(row=5,column=1,padx=30,)
widthentry = Entry(root,width=40)
widthentry.grid(row=5,column=2)

width =Label(root,text="Enter your Heigth (in Meter):",font="time 10 bold")
width.grid(row=6,column=1,padx=30,)
heigthentry = Entry(root,width=40)
heigthentry.grid(row=6,column=2,pady=10)

btn =Button(root,text="Calculate",width=30,command=cal)
btn.grid(row=9,column=1,columnspan=2)

show =Button(root,text="Show",width=30,command=show)
show.place(x=150, y=300)




root.mainloop()