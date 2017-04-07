from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel=Label(self,text='This is test')
        self.helloLabel.grid(row=0,column=0,sticky=W)
        self.quitButton=Button(self,text='Q',command=self.quit)
        self.quitButton.pack()

def loop():
    app.helloLabel=Label(text='str(i)')
    


app=Application()
app.master.title('hello windows')
app.geometry('300x200')
app.mainloop()

    
