import tkinter as tk
import numpy as np
from tkinter import *
import tkinter.messagebox as mb
import matplotlib as mp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math
from mpl_toolkits.axisartist.parasite_axes import HostAxes,ParasiteAxes
# from mpl_toolkits.mplot3d import Axes3D
import qrcode

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()

def d3():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    y = np.linspace(0,1.2,12)
    x = np.ones(y.size)
    K = 7
    X = np.linspace(0.1,1.8,50)
    Y = np.linspace(0.5,1.5,50) 
    X,Y = np.meshgrid(X,Y)
    # Z = K*X/sqrt((1/X-K*X-X)**2 + (Y*K-Y*X**2*K)**2)
    Z = K*X/np.sqrt((1/X-K*X-X)**2 + (Y*K-Y*X**2*K)**2)
    # print(Z)
    ax.plot_surface(X,Y,Z,color = 'r',alpha = 0.5,antialiased=False)
    
    X = np.linspace(0.45,1.3,40)
    Y = np.linspace(0.5,1.3,50) 
    X,Y = np.meshgrid(X,Y)
    Z = K*X/np.sqrt((1/X-K*X-X)**2 + (Y*K-Y*X**2*K)**2)
    ax.plot_surface(X,Y,Z,color = 'g',alpha = 0.5,antialiased=False)
    plt.show()
    
def Gain(w):
    return 1/(1 + w*1j)
def LOG(x):
    return 20*math.log(x,10)
def Angle(w):
    return 1/(1 + w*1j)
    
def bode():
    x = np.linspace(0.01,1e6,100)
    print(20*np.log(np.abs(Gain(x)),10))
    # plt.plot(x,1/x)
    plt.plot(x,20*np.log(np.abs(Gain(x)),10))
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Amp")
    
    plt.show()
def qr():
    img = qrcode.make("http://www.baoan-marathon.com/")
    img.save("test.png")
if __name__ == '__main__':
    # d3()
    bode()
    # qr()
    

