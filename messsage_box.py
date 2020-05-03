from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title('Image Viewer')
root.iconbitmap('images/a.ico')
 
#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
	response = messagebox.askyesno('This is my popup!','Hello world!')
	Label (root, text = response).pack()
	if response == 1:
		Label (root, text = 'You clicked yes').pack()
	else:
		Label (root, text = 'You clicked no').pack()


Button(root, text = 'popup', command  = popup).pack()



root.mainloop()

