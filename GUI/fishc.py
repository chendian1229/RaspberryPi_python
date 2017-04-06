from tkinter import *
import time

root=Tk()
root.title('To fishc')



label1=Label(root,text="This is a \n cat !")
label1.pack(side=LEFT)

photo=PhotoImage(file="cat.png")

label2=Label(root,image=photo)
label2.pack(side=RIGHT)

mainloop()
