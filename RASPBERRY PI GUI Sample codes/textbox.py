from tkinter import *
from tkinter.scrolledtext import ScrolledText
root=Tk();
def hallo(events):
    global k
    scale3=IntVar()
    print(scale3.cget())
scale1=Scale(label='red_light',from_=1,to_=100,length=100,orient='horizontal',tickinterval='10');
scale1.pack()
scale2=Scale(label='yellow_light',from_=1,to_=100,length=100,orient='horizontal');
scale2.pack()
scale3=Scale(label='green_light',from_=1,to_=100,length=100,orient='horizontal',command=hallo);
scale3.pack()
mainloop();

