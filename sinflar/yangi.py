# from tkinter import *
# from tkinter.messagebox import *
# top = Tk()
# def helloCallBack():
#     showinfo("Hello Python", "Hello World")
# B = Button(top, text="Hello Abbosbek \n How are you ?", command=helloCallBack,
#            activebackground="yellow", activeforeground="red", bd=2, bg="blue",
#            fg="white", font="italic", height=2, highlightcolor="black", justify=CENTER,
#            padx=10, pady=10, relief=GROOVE, state=NORMAL, underline=1, width=15, wraplength=120)
# B.pack()
# # top.mainloop()
# from tkinter import *
# forma=Tk()
# lab=Label()
# tex=Text()
# lab.text="Salom DUnyo"
# forma.title="Assalomu alaykum"
# btugma=Button(forma,text='Salom Dunyo')
# btugma.pack()
# tex.pack()
# from tkinter.messagebox import *
# showinfo("Assalomu alaykum","Assalomu alaykum")
# lab.pack()
# forma.mainloop()
# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Salom Dunyo! ").grid(column=0, row=0)
# ttk.Button(frm, text="Chiqish", command=root.destroy).grid(column=7, row=0)
#
# root.mainloop()
from tkinter import *
root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
print(h)
gui = Tk(className='Oyna o’lchamlarini sozlash')
gui.geometry(400,400) # O’lchamlarni berish
gui.state('zoomed')
gui.iconify()
gui.mainloop()


