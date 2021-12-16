from tkinter import *
oyna=Tk()
oyna.title("HISOBLASH")
e=Entry(oyna,width=35,borderwidth=5,font=14)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
def ADD(son):
    s=e.get()
    e.delete(0,END)
    e.insert(0,s+str(son))
def butun_F():
    s = str(e.get())
    if len(s)==0:
        e.insert(0, "0.")
    elif '.' in s:
        pass
    else:
        e.delete(0, END)
        e.insert(0, s + ".")


def qushish_F():
    global amal
    global son1
    amal=0
    son1=float(e.get())
    e.delete(0,END)
def ayirish_F():
    global amal
    global son1
    amal=1
    son1=float(e.get())
    e.delete(0,END)
def kupaytirish_F():
    global amal
    global son1
    amal=2
    son1=float(e.get())
    e.delete(0,END)
def bulish_F():
    global amal
    global son1
    amal=3
    son1=float(e.get())
    e.delete(0,END)
def TENGLIK_F():
    son2=float(e.get())
    e.delete(0, END)
    if amal==0:
        e.insert(0,str(son1+son2))
    elif amal==1:
        e.insert(0, str(son1 - son2))
    elif amal == 2:
        e.insert(0, str(son1 * son2))
    else:
        e.insert(0, str(son1 / son2))
button1=Button(oyna,text="1",padx=40,pady=20,bg="yellow",font=14,command=lambda :ADD(1)) #command=lambda :ADD(1)
button2=Button(oyna,text="2",padx=40,pady=20,bg="yellow",font=14,command=lambda :ADD(2)) #command=lambda :ADD(1)
button3=Button(oyna,text="3",padx=40,pady=20,bg="yellow",font=14,command=lambda :ADD(3)) #command=lambda :ADD(1)
qushish=Button(oyna,text="+",padx=40,pady=20,bg="yellow",font=14, command=qushish_F) #command=lambda :ADD(1)
button4=Button(oyna,text="4",padx=40,pady=20,bg="yellow",font=14,command=lambda :ADD(4)) #command=lambda :ADD(1)
button5=Button(oyna,text="5",padx=40,pady=20,bg="yellow",font=14,command=lambda :ADD(5)) #command=lambda :ADD(1)
button6=Button(oyna,text="6",padx=40,pady=20,bg="yellow",font=14,command=lambda :ADD(6)) #command=lambda :ADD(1)
ayirish=Button(oyna,text="-",padx=40,pady=20,bg="yellow",font=14, command=ayirish_F) #command=lambda :ADD(1)
button7=Button(oyna,text="7",padx=40,pady=20,bg="yellow",font=14,command=lambda :ADD(7)) #command=lambda :ADD(1)
button8=Button(oyna,text="8",padx=40,pady=20,bg="yellow",font=14,command=lambda :ADD(8)) #command=lambda :ADD(1)
button9=Button(oyna,text="9",padx=40,pady=20,bg="yellow",font=14,command=lambda :ADD(9)) #command=lambda :ADD(1)
kupaytirish=Button(oyna,text="x",padx=40,pady=20,bg="yellow",font=14, command= kupaytirish_F) #command=lambda :ADD(1)

button0=Button(oyna,text="0",padx=40,pady=20,bg="yellow",font=14,command=lambda :ADD(0)) #command=lambda :ADD(1)
butun=Button(oyna,text=",",padx=40,pady=20,bg="yellow",font=14, command=butun_F) #command=lambda :ADD(1)
tenglik=Button(oyna,text="=",padx=40,pady=20,bg="yellow",font=14,command= TENGLIK_F) #command=lambda :ADD(1)
bulish=Button(oyna,text="/",padx=40,pady=20,bg="yellow",font=14,command=bulish_F) #command=lambda :ADD(1)
uchirish=Button(oyna,text="<",padx=40,pady=20,bg="yellow",font=14) #command=lambda :ADD(1)
tozalash=Button(oyna,text="C",padx=40,pady=20,bg="yellow",font=14,command=lambda : e.delete(0,END)) #command=lambda :ADD(1)
chiqish=Button(oyna,text="Exit",padx=80,pady=20,bg="yellow",font=14,command=lambda : oyna.quit())
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
qushish.grid(row=1,column=3)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
ayirish.grid(row=2,column=3)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
kupaytirish.grid(row=3,column=3)
button0.grid(row=4,column=0)
butun.grid(row=4,column=1)
tenglik.grid(row=4,column=2)
bulish.grid(row=4,column=3)
uchirish.grid(row=5,column=0)
tozalash.grid(row=5,column=1)
chiqish.grid(row=5,column=2,columnspan=3)
oyna.mainloop()