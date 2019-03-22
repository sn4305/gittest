# coding=gbk
import numpy as np
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
 
#----------------------------------------------------------------------
def drawPic():
    ###��ȡGUI�����ϵĲ���
    try:
        sampleCount=int(inputEntry.get())
    except:
        sampleCount=50
        print('����������')
        inputEntry.delete(0,END)
        inputEntry.insert(0,'50')
    
    #���ͼ����ʹ��ǰ�����λ��Ƶ�ͼ�񲻻��ص�
    drawPic.f.clf()
    drawPic.a=drawPic.f.add_subplot(111)
    
    #��[0,100]��Χ���������sampleCount�����ݵ�
    x=np.random.randint(0,100,size=sampleCount)
    y=np.random.randint(0,100,size=sampleCount)
    color=['b','r','y','g']
    
    #������Щ������ɢ��ͼ����ɫ���ѡȡ
    drawPic.a.scatter(x,y,s=3,color=color[np.random.randint(len(color))])
    drawPic.a.set_title('Demo: Draw N Random Dot')
    drawPic.canvas.draw()
    
    
if __name__ == '__main__':
    
    matplotlib.use('TkAgg')
    root=Tk()
    
    #��Tk��GUI�Ϸ���һ������������.grid()����������
    drawPic.f = Figure(figsize=(5,4), dpi=100) 
    drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root)
    drawPic.canvas.draw()
    drawPic.canvas.get_tk_widget().grid(row=0, columnspan=3)    
 
    #���ñ�ǩ���ı���Ͱ�ť�Ȳ������������ı����Ĭ��ֵ�Ͱ�ť���¼�����
    Label(root,text='����������������').grid(row=1,column=0)
    inputEntry=Entry(root)
    inputEntry.grid(row=1,column=1)
    inputEntry.insert(0,'50')
    Button(root,text='��ͼ',command=drawPic).grid(row=1,column=2,columnspan=3)
    
    #�����¼�ѭ��
    root.mainloop()