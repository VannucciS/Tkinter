from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title('First window')
root.iconbitmap('images/a.ico')
my_image2 = ImageTk.PhotoImage(Image.open('images/b.jpg'))
mylabel = Label(root, image = my_image2).pack(anchor = E)

def open_window():
	global my_image
	top = Toplevel()
	top.title('This is a second window')
	my_image = ImageTk.PhotoImage(Image.open('images/a.jpg'))
	mylabel = Label(top, image = my_image).pack(anchor = E)
	button2 = Button(top, text = 'click me to close this window', command = top.destroy).pack()


button = Button(root, text = 'click me to open a new window', command = open_window).pack()


 



mainloop()

