from tkinter import *
root=Tk()
def Myclick():
    Mylabel=label(root,text="Hello fucker!")
    Mylabel.pack()
MyB=Button(root,text="Click me!",command=Myclick)
MyB.pack()


root.mainloop()