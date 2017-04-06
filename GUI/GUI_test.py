from tkinter import *

class Application(Frame):

    def __int__(self,master):
        super(Application,self).__int__(master)
        #self.grid()
        self.creat_widgets()

    def creat_widgets(self):
        self.label1=Label(self,text='This is a window')
        self.pack()
        self.label1.grid(row=0,column=0,sticky=W)
        self.button1=Button(self,text='Quit',command=self.quit)


root=Tk()
root.title('UART-Value')
root.geometry('300x100')
app=Application(root)
app.mainloop()
