# from tkinter import *
# from tkinter.messagebox import *
# asoy=Tk(className="KALK")
# asoy.title="AX 3-kurs kalkulyatori"
# asoy.geometry("300x400")
# oyna=Text(asoy,width=40, height=2)
# #oyna.place(x=10,y=10,width=300, height=50)
# oyna.grid(row=0,column=0)
# oyna.pack()
# bir=Button(asoy,text="1")
# bir.grid(row=1,column=0)
# bir.pack()
# ikki=Button(asoy,text="2")
# ikki.grid(row=1,column=1)
# ikki.pack()
# uch=Button(asoy,text="3").grid(row=1,column=2)
# uch.pack()
# kup=Button(asoy,text="X").grid(row=1,column=3)
# kup.pack()
# turt=Button(asoy,text="4").grid(row=2,column=0)
# turt.pack()
# asoy.mainloop()
import tkinter as tk

window = tk.Tk()
window.geometry("300x400")
# oyna=tk.Text(window)
# oyna.pack()
frame = tk.Frame(
    master=window
)
frame.grid(row=0)
oyna = tk.Text(master=frame,width=40, height=2)
oyna.pack()
for i in range(3):
    for j in range(3):
        frame2 = tk.Frame(
            master=window
        )
        frame2.grid(row=i+1, column=j)
        label = tk.Button(master=frame2, text=f"{i*3+1+j}",width=5, height=2 )
        label.pack()
        if i==1 and j==2:
            frame2.grid(row=i + 1, column=j+1)
            kup=tk.Button(master=frame2,text=f"X",width=5, height=2)
            kup.pack
        if j==2 and i==2:
            frame2.grid(row=i + 1, column=j+1)
            minus=tk.Button(master=frame2,text=f"-",width=5, height=2)
            minus.pack
        if j==2 and i==3:
            frame2.grid(row=i + 1, column=j+1)
            plus=tk.Button(master=frame2,text=f"+",width=5, height=2)
            plus.pack
frame2 = tk.Frame(
    master=window
)
frame2.grid(row=4, column=0)
label = tk.Button(master=frame2, text=f"+/-", width=5, height=2)
label.pack()
frame2 = tk.Frame(
    master=window
)
frame2.grid(row=4, column=0)
label = tk.Button(master=frame2, text=f"0", width=5, height=2)
label.pack()
frame2.grid(row=4, column=1)
label = tk.Button(master=frame2, text=f",", width=5, height=2)
label.pack()
label = tk.Button(master=frame2, text=f",", width=5, height=2)
label.pack()
frame2.grid(row=4, column=2)
label = tk.Button(master=frame2, text=f"=", width=5, height=2)
label.pack()
window.mainloop()