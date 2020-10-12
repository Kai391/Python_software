from tkinter import *
from PIL import Image,ImageTk
root=Tk()

root.geometry("1000x600")
root.title("NewsPaper")
root.wm_minsize(900,500)

f_r1=Frame(root,background="black",borderwidth=3)
f_r1.pack()
Label(f_r1,text="Krishna's Newspaper", foreground="red",font="normal 20 bold",padx=250).pack()
Label(f_r1,text="July 26-2020",font="normal 10 bold").pack()

f_r2=Frame(root,background="black",borderwidth=1)
f_r2.pack(side="top",anchor="n",pady=30,padx=50)
im = Image.open("1.png")
Im=im.resize((170,170))
image=ImageTk.PhotoImage(Im)
Label(f_r2,image=image).pack(side="left")
with open('1.txt') as f:
    t=f.read()
Label(f_r2,text=t,pady=55,padx=200).pack(side="top")

f_r3=Frame(root,background="black",borderwidth=1)
f_r3.pack(side="top",anchor="n",pady=0,padx=50)
im1 = Image.open("2.png")
Im1=im1.resize((170,170))
image1=ImageTk.PhotoImage(Im1)
Label(f_r3,image=image1).pack(side="right")
with open('2.txt') as f:
    t=f.read()
Label(f_r3,text=t,pady=55,padx=190).pack(side="top")

f_r4=Frame(root,background="black",borderwidth=1)
f_r4.pack(side="top",anchor="n",pady=30,padx=50)
im3 = Image.open("3.png")
Im3=im3.resize((170,170))
image3=ImageTk.PhotoImage(Im3)
Label(f_r4,image=image3).pack(side="left")
with open('3.txt') as f:
    t=f.read()
Label(f_r4,text=t,pady=55,padx=210).pack(side="top")

root.mainloop()