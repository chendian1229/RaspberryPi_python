from tkinter import *
import time

root=Tk()
root.title('To fishc')

label1=Label(root,text='This is a cat !',font=('Tempus Sans ITC',20),fg='Red')
label1.pack(side=LEFT)

photo=PhotoImage(file="cat.png")

label2=Label(root,image=photo)
label2.pack(side=RIGHT)




    


mainloop()
