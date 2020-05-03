from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title('First window')
root.iconbitmap('images/a.ico')
root.geometry('400x400')

#var = IntVar()
var = StringVar()

def show():
	mylabel = Label(root, text = var.get())
	mylabel.pack()

c = Checkbutton(root, text = 'Try to click me' , variable = var, onvalue = 'on', offvalue = 'off')
c.deselect() #unckeck the box
c.pack()



mybutton = Button(root, text = 'click me to see whats behind the scene', command = show)
mybutton.pack()

root.mainloop()

