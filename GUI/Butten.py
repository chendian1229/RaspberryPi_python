from tkinter import *
import random

g_show_flag=True

class Application():
    def __init__(self,root):

        self.root=root
        self.createFrameTop()

    def createFrameTop(self):

        self.frm_top=LabelFrame(self.root,text="Test")
        self.frm_top.pack()

        self.frm_label=Label(self.frm_top,text='0')
        self.frm_label.pack()

        self.frm_button=Button(self.frm_top,text='start',command=self.click)
        self.frm_button.pack()

    def click(self):
        global g_show_flag

        if self.frm_button['text']=="start":
            g_show_flag=True
            self.frm_button['text']="stop"
            self.show()
        else:
            self.frm_button['text']="start"
            g_show_flag=False

    def show(self):
        global g_show_flag
        self.frm_label['text']=random.choice(list(range(0,99)))
        if g_show_flag:
            self.root.after(64,self.show)


if __name__=="__main__":

    root=Tk()
    root.title("Label")

    Application(root)
    root.mainloop()
    











        
