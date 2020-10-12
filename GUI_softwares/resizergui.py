from tkinter import *
import tkinter.messagebox as k
root=Tk()

def take():
    width=w.get()
    height=h.get()
    # print(width,height)
    Label(f,text="updated",font="normal 15").grid(row=0,column=1)
    root.geometry(f"{width}x{height}")
    

root.geometry("500x400")
root.wm_minsize(400,400)
Label(text="Welcome To GUI Resizer",font="normal 20 bold").pack()
f=Frame(root)
f.pack(pady=100,fill=Y)
Label(f,text="Width:",font="normal 13",padx=10,pady=20).grid(row=1,column=0)
Label(f,text="Height:",font="normal 13").grid(row=2,column=0)

w=StringVar()
h=StringVar()
Entry(f,textvariable=w,width=25).grid(row=1,column=1)
Entry(f,textvariable=h,width=25).grid(row=2,column=1)

Button(f,text="Apply",font="normal 13",command=take).grid(column=1,pady=15)

root.mainloop()