from tkinter import *

class Application(Frame):
    """ Build the basic window frame template """

    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.varSuger=IntVar()
        self.varSoda=IntVar()
        self.createFrameTop()
        


    def createFrameTop(self):
        #定义一个标签
        self.label1=Label(self,text="test!")
        self.label1.grid(row=0,column=0,sticky=NE)

        #创建一个
        self.text1=Entry(self)
        self.text1.grid(row=1,column=2)
        
        #定义两个可选中标签
        self.check1=Checkbutton(self,text="Suger",variable=self.varSuger)
        self.check1.grid(row=1,column=1)
        
        self.check2=Checkbutton(self,text="Soda",variable=self.varSoda)
        self.check2.grid(row=2,column=1)   
        
        #定义一个按键，功能自拟
        self.button1=Button(self,text="确定",command=self.display,underline=0)
        self.button1.grid(row=3,column=1,sticky=N)

        self.button2=Button(self,text="Conver",command=self.convert)
        self.button2.grid(row=3,column=2)
        
        self.button3=Button(self,text="Clear",command=self.clear)
        self.button3.grid(row=4,column=2)

    def display(self):
        if (self.varSuger.get()):
            print("You want some Suger!")

        if (self.varSoda.get()):
            print("You want some Soda!")
        print("The button was clicked in the window")

    def convert(self):
        varText=self.text1.get()
        varReplaced=varText.upper()
        self.text1.delete(0,END)
        self.text1.insert(END,varReplaced)

    def clear(self):
        self.text1.delete(0,END)
        self.text1.focus_set()





if __name__=="__main__":
    try:
        root=Tk()
        root.title('grid GUI style')
        root.geometry('300x200')
        app=Application(root)       #实例化子类，并继承父类方法与属性
        app.mainloop()
    except KeyboardInterrupt:
        pass


