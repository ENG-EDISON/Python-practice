from tkinter import *
def callback(event):
    print(event.delta)
root = Tk()
root.bind('<Key>', callback)
mainloop()
