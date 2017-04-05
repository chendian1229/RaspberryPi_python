from tkinter import *

class Application(Frame):

    def __int__(self,master):
        super(Application,self).__int__(master)
        self.grid()
        self.creat_widgets()

    def creat_widgets(self):
        self.label1=Lable(self,text="This is a window")
        self.label1.grid(row=0,column=0,sticky=W)


for value in range(0,10):
    value=value+1
root=Tk()
root.title('UART-Value')
#root.geometry('300*100')
app=Application(root)
app.mainloop()
