from tkinter import *
root = Tk()
root.geometry("500x350")
root.wm_minsize(500,350)
root.wm_maxsize(500,350)
root.title("Calculator")
root.configure(bg="grey")
def click(event):
    global scvalue
    text=event.widget.cget('text')
    if text =="=":
        t=scvalue.get()
        if '+' in t:
            T=t.split("+")
            n1=int(T[0])
            n2=int(T[1])
            value=n1+n2
        elif '-' in t:
            T=t.split("-")
            n1=int(T[0])
            n2=int(T[1])
            value=n1-n2
        elif '*' in t:
            T=t.split("*")
            n1=int(T[0])
            n2=int(T[1])
            value=n1*n2
        elif '/' in t:
            T=t.split("/")
            n1=int(T[0])
            n2=int(T[1])
            value=n1//n2
        elif '^' in t:
            T=t.split("^")
            n1=int(T[0])
            n2=int(T[1])
            value=n1**n2
        elif '%' in t:
            T=t.replace("%","")
            T=int(T)
            value=T/100

        scvalue.set(value)
        screen.update()
    
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update
    
scvalue=StringVar()
scvalue.set("")
screen = Entry(root,textvariable=scvalue,font='lucida 30 bold')
screen.pack(fill=X,ipady=10,pady=15,padx=10)
f1=Frame(root,bg="red")

b=Button(f1,text='9',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,)

b=Button(f1,text='8',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=0,column=1)

b=Button(f1,text='7',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=0,column=2)
b=Button(f1,text='6',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=1,column=0)
b=Button(f1,text='5',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=1,column=1)
b=Button(f1,text='4',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=1,column=2)
b=Button(f1,text='3',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=2,column=0)
b=Button(f1,text='2',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=2,column=1)
b=Button(f1,text='1',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=2,column=2)
b=Button(f1,text='0',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=3,column=1)
b=Button(f1,text='C',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=3,column=0)
b=Button(f1,text='=',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=3,column=2)



f1.pack(side='left',anchor='s')

f2=Frame(root,bg="yellow")

b=Button(f2,text='+',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(row=0,column=0)

b=Button(f2,text='-',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=0,column=1)

b=Button(f2,text='*',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=1,column=0)

b=Button(f2,text='/',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=1,column=1)

b=Button(f2,text='(',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=2,column=0)

b=Button(f2,text=')',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=2,column=1)

b=Button(f2,text='^',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=3,column=0)

b=Button(f2,text='%',font='normal 10',padx=30,pady=7)
b.bind('<Button-1>',click)
b.grid(padx=10,pady=10,row=3,column=1)

f2.pack(side='right',anchor='s')


root.mainloop()