from tkinter import*
root=Tk()

#create a frame
my_label=Label(root,text="Hello world")
my_label2=Label(root,text="Hello world!")


#show it on screen
my_label1.grid(row=0,column=2)
my_label2.grid(row=1,column=0)
root.mainloop()