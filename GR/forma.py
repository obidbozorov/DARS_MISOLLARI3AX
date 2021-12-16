# import tkinter
# forma=tkinter.Tk()
# # forma.mainloop()
# from tkinter import *
# forma2=Tk(className='1-oyna')
# w, h = forma2.winfo_screenwidth(), forma2.winfo_screenheight()
# print(h)
# forma2.geometry('500x300')
# forma2.minsize(200,200)
# forma2.maxsize(700,700)
# forma2.mainloop()
# from tkinter.messagebox import *
# from tkinter import *
# def salomlash():
#     showinfo("Assalomu Alaykum, Qodirov Shuxrat Aka!", message="Salom")
# forma=Tk(className="Salomlashgich")
# forma.geometry('400x400')
# tugma=Button(forma,text="Salomlash",command=salomlash)
# print(tugma.winfo_screenheight())
# tugma.place(x=200,y=200)
# forma.mainloop()
from tkinter import *
def hisobla():
    a = int(bir_son.get())
    b = int(ikkinchi_son.get())
    c = a + b
    natija.delete(0,END)
    natija.insert(0,str(c))
kalk=Tk(className="Kalkulyaot")
bir_son=Entry(kalk)
bir_son.pack()
plus=Label(text="+")
plus.pack()
ikkinchi_son=Entry(kalk)
ikkinchi_son.pack()
teng=Button(kalk, text="=",command=hisobla)
teng.pack()
natija=Entry(kalk)
natija.pack()
kalk.mainloop()