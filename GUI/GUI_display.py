#!/usr/bin/python
# -*- coding:utf-8 -*-

from tkinter import *
import random
import time
import smbus

g_show_flag=True

address=0x48
A3=0x43
bus=smbus.SMBus(1)

class Application():
    def __init__(self,root):

        self.root=root
        self.createFrameTop()

    def createFrameTop(self):

        self.frm_top=LabelFrame(self.root,text="Vol")
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
        bus.write_byte(address,A3)
        value=bus.read_byte(address)
        #self.frm_label['text']=random.choice(list(range(0,99)))
        self.frm_label['text']=str(value*3.3/256)[0:5]+"V"
        time.sleep(0.3)
        if g_show_flag:
            self.root.after(64,self.show)


if __name__=="__main__":

    root=Tk()
    root.title("Display")

    Application(root)
    root.mainloop()
    











        
