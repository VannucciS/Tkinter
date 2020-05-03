from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title('First window')
root.iconbitmap('images/a.ico')
root.geometry('400x400')

vertical = Scale(root, from_ = 0 , to = 400)
vertical.pack()

Horizontal = Scale(root, from_ = 0 , to = 400, orient = HORIZONTAL)
Horizontal.pack()

my_label = Label(root, text = Horizontal.get()).pack()

def slider():
	my_label = Label(root, text = Horizontal.get()).pack()
	root.geometry(str(Horizontal.get())+'x' + str(vertical.get()))	

my_button = Button(root, text = 'click here', command = slider).pack()

root.mainloop()

