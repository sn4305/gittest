# coding=gbk
import numpy as np
from tkinter import *
import tkinter.messagebox as mb
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math
from LLC_calc import *
from mpl_toolkits.axisartist.parasite_axes import HostAxes,ParasiteAxes
from mpl_toolkits.mplot3d import Axes3D
#----------------------------------------------------------------------
def parallel(x,y):
	return x*y/(x+y)
    
#design input parameter
Vin = 450
Lr = 12e-6
Cr = 328e-9
Lm = 90e-6
Rl_list = (10,1,0.5,0.1)
n = 14
Pi = math.pi


Omiga0 = (Lr*Cr)**-0.5
#Omiga = 40e4
Freq_base = Omiga0/(2*Pi)
    
'''
M_:volt transmit ratio
        |           s*Lm // Rac         |
M_ =    | ----------------------------  |
        | s*Lm // Rac + s*Lr + 1/(s*Cr) |
'''
def Gain(Freq_ratio,Rl):
    #Freq = Freq_base * Freq_ratio
    Omiga = Omiga0 * Freq_ratio
    # Z0 = (Lr/Cr)**0.5
    # ratio = (Lm/Lr)**0.5
    Rac = 8*Rl*n*n/(Pi**2)
    # Q = n*n*Rl/Z0
    #calculate Gain:M_
    s = Omiga*1j
    Lm_Rac = parallel(s*Lm,Rac)
    M_ = Lm_Rac
    M_ = M_/(M_ + s*Lr + (s*Cr)**-1)
    vir = M_.imag
    M_ = abs(M_)
    
    Vo = Vin*M_/(2*n)
    return M_
        
def d3():
    y = np.linspace(0,1.2,12)
    x = np.ones(y.size)
    K = 7
    X = np.arange(0.1,1.8,0.05)
    Y = np.arange(0.5,1.5,0.05) 
    X,Y = np.meshgrid(X,Y)
    # Z = K*X/sqrt((1/X-K*X-X)**2 + (Y*K-Y*X**2*K)**2)
    Z = K*X/np.sqrt((1/X-K*X-X)**2 + (Y*K-Y*X**2*K)**2)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X,Y,Z,cmap = mp.cm.coolwarm,antialiased=False)
    plt.show()
    
def drawPic():
    #define LLC object
    try:
        llc = LLC(float(inputEntry.get()),float(inputEntry4.get()),float(inputEntry3.get()),float(inputEntry2.get()),int(inputEntry5.get()))
    except:
        mb.showinfo('Alarm!','Please input right data!')
        return
    if llc.Vo_min > llc.Vo_nor or llc.Vo_nor > llc.Vo_max:
        mb.showinfo('Alarm!','Vo_min < Vo_nor < Vo_max should be satisfied!')
        return
    if llc.Vo_min > 500 or llc.Vo_max <5 or 10 > llc.Po > 6000:
        mb.showinfo('Alarm!','Are you kidding me!')
        return
    
    #清空图像，以使得前后两次绘制的图像不会重叠
    drawPic.f.clf()
    #Create two graphs
    drawPic.a=drawPic.f.add_subplot(221)
    drawPic.b=drawPic.f.add_subplot(222,projection='3d')
    drawPic.c=drawPic.f.add_subplot(223)
    drawPic.d=drawPic.f.add_subplot(224,projection='3d')

    X = np.arange(llc.Vo_min,llc.Vo_max,0.2)
    y1=[]
    y2=[]
    y3=[]
    for x in X:
        try:
            tmp = llc.Power_Split(x)
            y1.append(tmp)
            y2.append(tmp*llc.Power_Coefficient)
            y3.append(x**2/tmp)
        except:
            break
    drawPic.a.plot(X,y1)
    drawPic.a.plot(X,y2,color = 'red',linestyle = '--')
    color=['b','r','y','g']
    
    # drawPic.a.set_xlabel("Vo/V",fontsize='small')
    drawPic.a.set_ylabel("Power/Watts",fontsize='small')
    drawPic.a.set_title('Power/Vo',fontsize='small')
    drawPic.f.text(0.16,0.5,"Vo",fontsize='small')
    drawPic.a.tick_params(labelsize=8)
    
    ax = drawPic.f.add_axes([0.35,0.58,0.1,0.1])
    ax.plot(X,y3)
    ax.set_title("Rload",fontsize='small')
    ax.set_ylabel("Rl/Ohm",fontsize='small')
    ax.tick_params(labelsize=5)
    
    Z0 = (Lr/Cr)**0.5
    ratio = (Lm/Lr)**0.5
    Q = n*n*Rl_list[1]/Z0
    Vin_max = int(inputEntry4.get())
    power = int(inputEntry5.get())
    
    #3d 
    # X = np.arange(-5,5,0.1)
    # Y = np.arange(-5,5,0.1)
    # X,Y = np.meshgrid(X,Y)
    # R = np.sqrt(X**2+Y**2)
    # Z = np.sin(R)
    # surf = drawPic.b.plot_surface(X,Y,Z,cmap=matplotlib.cm.coolwarm,antialiased=False)
    # drawPic.b.set_zlim(-1.01,1.01)
    
    K = 7
    X = np.arange(0.1,1.8,0.05)
    Y = np.arange(0.1,1.5,0.05)
            
    X,Y = np.meshgrid(X,Y)
    Z = K*X/np.sqrt((1/X-K*X-X)**2 + (Y*K-Y*X**2*K)**2)
    surf = drawPic.d.plot_surface(X,Y,Z,cmap=matplotlib.cm.coolwarm,alpha = 0.5,antialiased=False)
    drawPic.d.tick_params(labelsize=8)
    drawPic.d.set_zlim(.1,1.3)

    drawPic.d.set_xlabel("Freq",fontsize='small')
    drawPic.d.set_ylabel("Q",fontsize='small')
    drawPic.d.set_zlabel("M",fontsize='small')
    
    inputEntry6.insert(0,Lr*1e6)
    inputEntry7.insert(0,Cr*1e9)
    inputEntry8.insert(0,Lm*1e6)
    inputEntry9.insert(0,str(round(Q,2)) + ", " + str(round(Freq_base/1e3,2)) + "kHz, " + str(n))
    
    x = np.arange(0.01,1.6,0.01)
    for Rl in Rl_list:
        drawPic.c.plot(x,Gain(x,Rl))
    
    
    Gain_max = max(Gain(x,Rl_list[1]))
    #print("max gain:", Gain_max)
    
    y = np.linspace(0,1.2,12)
    x = np.ones(y.size)
    drawPic.c.plot(x,y,color = 'blue',linestyle = '--')
    
    x = np.linspace(0,0.5,12)
    y = np.ones(x.size)*Gain_max
    drawPic.c.plot(x,y,color = 'red',linestyle = '--')
    
    drawPic.c.set_title('LLC Gain vs Freq',fontsize='small')
    drawPic.c.set_ylim(0.2,2)
    drawPic.c.set_xlabel("X:Freq_Ratio",fontsize='small')
    drawPic.c.set_ylabel("Gain",fontsize='small')
    drawPic.c.tick_params(labelsize=8)
    drawPic.canvas.draw()
    
    
def Clear():
    inputEntry.delete(0,END)
    inputEntry2.delete(0,END)
    inputEntry3.delete(0,END)
    inputEntry4.delete(0,END)
    inputEntry5.delete(0,END)
    inputEntry6.delete(0,END)
    inputEntry7.delete(0,END)
    inputEntry8.delete(0,END)
    inputEntry9.delete(0,END)
    drawPic.f.clf()
    
if __name__ == '__main__':
    
    matplotlib.use('TkAgg')
    root=Tk()
    root.title('LLC calculation')
    
    #在Tk的GUI上放置一个画布，并用.grid()来调整布局
    drawPic.f = Figure(figsize=(6,4.8), dpi=150) 
    drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root)
    drawPic.canvas.draw()
    drawPic.canvas.get_tk_widget().grid(row=0, columnspan=5)    
 
#---------------------------------------------------------
#   User input variables
    Label(root,text='Vin/V').grid(row=1,column=0)
    inputEntry=Entry(root)
    inputEntry.grid(row=1,column=1)
    inputEntry.insert(0,'450')

    Label(root,text='Vout min/V').grid(row=2,column=0)
    inputEntry2=Entry(root)
    inputEntry2.grid(row=2,column=1)
    inputEntry2.insert(0,'9')
    
    Label(root,text='Vout nor/V').grid(row=3,column=0)
    inputEntry3=Entry(root)
    inputEntry3.grid(row=3,column=1)
    inputEntry3.insert(0,'14.5')
    
    Label(root,text='Vout max/V').grid(row=4,column=0)
    inputEntry4=Entry(root)
    inputEntry4.grid(row=4,column=1)
    inputEntry4.insert(0,'16')
    
    Label(root,text='Power/Watt(int)').grid(row=5,column=0)
    inputEntry5=Entry(root)
    inputEntry5.grid(row=5,column=1)
    inputEntry5.insert(0,'1600')
#-----------------------------------------------------------
#   Values Calculated by software
    Label(root,text='Lr/uH').grid(row=2,column=2)
    inputEntry6=Entry(root)
    inputEntry6.grid(row=2,column=3)
    
    Label(root,text='Cr/nF').grid(row=3,column=2)
    inputEntry7=Entry(root)
    inputEntry7.grid(row=3,column=3)
    
    Label(root,text='Lm/uH').grid(row=4,column=2)
    inputEntry8=Entry(root)
    inputEntry8.grid(row=4,column=3)
    
    Label(root,text='Q, f0, N').grid(row=5,column=2)
    inputEntry9=Entry(root)
    inputEntry9.grid(row=5,column=3)
#-------------------------------------------------------------

    Button(root,text='Start',command=drawPic).grid(row=1,column=3,columnspan=5)
    Button(root,text='Clear',command=Clear).grid(row=1,column=4,columnspan=5)
    
    #启动事件循环
    root.mainloop()