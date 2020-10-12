from tkinter import *
def submit():
    n=name.get()
    c=course.get()
    a=address.get()
    p=payment.get()
    d=[f"name:{n}",f"course:{c}",f"address:{a}",f"payment:{p}"]

    with open("t.txt",'a') as f:
        for i in d:
            f.write(i)
            f.write(',\t')
        f.write('\n')
    
    
    

root=Tk()
root.geometry("900x500")
Label(text="Welcome to Python Course Form",font="normal 20 bold").pack()
f1=Frame(root,borderwidth=1)
f1.pack(pady=30)
Label(f1,text="Name:",font="normal 15",padx=50).grid()
Label(f1,text="Course Level:",font="normal 15").grid(row=1,column=0)
Label(f1,text="Address:",font="normal 15").grid(row=2,column=0)
Label(f1,text="Payment:",font="normal 15").grid(row=3,column=0)

name=StringVar()
course=StringVar()
address=StringVar()
payment=StringVar()

e1=Entry(f1,textvariable=name).grid(row=0,column=1)
e2=Entry(f1,textvariable=course).grid(row=1,column=1)
e3=Entry(f1,textvariable=address).grid(row=2,column=1)
e4=Entry(f1,textvariable=payment).grid(row=3,column=1)

b=Button(root,text="Submit",foreground="white",background="grey",command=submit).pack()

root.mainloop()
