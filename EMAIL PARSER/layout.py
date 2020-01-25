from tkinter import *
from tkinter import ttk
gui = Tk()
gui.geometry("400x400")
def login(us1,pw1):
    print(us1,pw1)
gui.title("First title")
a1 = Label(gui ,text="username").grid(row=3,column = 0)
b1 = Label(gui ,text="password").grid(row=4,column=0)
e1 = Entry(gui).grid(row=3,column=1)
f1 = Entry(gui,show="*").grid(row=4,column=1)
c1 = Button(gui, text="LOGIN",command=lambda : login(e1,f1)).grid(row=5,column = 0)
gui.mainloop()
