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

    #创建总框架方法
    def createFrameTop(self):
        #总框架结构，填充整个空白区域
        self.frm_top=LabelFrame(self.root,text="电压",font=("Helvetica",32))
        self.frm_top.pack(expand=1,fill=BOTH)

        #数值标签，显示电压数值
        self.value_label=Label(self.frm_top,text='0.00V',font=("Helvetica",50))
        self.value_label.pack(side='left',expand=1)

        #建立显示进度条，电压范围
        self.scale=Scale(self.frm_top,from_=0,to=3.3,orient=VERTICAL,
                         length=200,resolution=0.001)
        self.scale.pack(side='right',expand=1)

        #开始按钮
        self.start_button=Button(self.frm_top,text='开始',command=self.click,font=("Helvetica",25))
        self.start_button.pack(expand=1)

        #结束进程按钮
        self.quit_button=Button(self.frm_top,text="关闭",command=self.root.quit,font=("Helvetica",25))
        self.quit_button.pack(side='right',expand=1)

    #单击开始按钮事件方法
    def click(self):
        global g_show_flag

        if self.start_button['text']=="开始":
            g_show_flag=True
            self.start_button['text']="停止"
            self.show()
        else:
            self.start_button['text']="开始"
            g_show_flag=False


    #显示电压数值方法
    def show(self):
        global g_show_flag
        bus.write_byte(address,A3)
        value=bus.read_byte(address)
        #self.frm_label['text']=random.choice(list(range(0,99)))
        self.scale.set(value*3.3/256)
        self.value_label['text']=str(value*3.3/256)[0:5]+"V"
        time.sleep(0.05)
        if g_show_flag:
            self.root.after(64,self.show)


if __name__=="__main__":

    root=Tk()
    root.geometry('400x300')        #设定TK尺寸
    root.title("电压测量")           #设定TK的title

    Application(root)               #实例化root
    root.mainloop()

    











        
