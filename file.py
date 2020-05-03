from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title('First window')
root.iconbitmap('images/a.ico')

'''
root.filename = filedialog.askopenfilename(initialdir = '/Users/Tomcat/Documents/Python/tkinter/images', title = 'Choose the file to show', 
	filetypes = (('JPG files', '*.jpg'), ("PNG files", "*.png"), ("Whatever files", "*.*")))
my_label = Label(root, text = root.filename).pack()
my_image = ImageTk.PhotoImage(Image.open(root.filename))
my_image_label = Label(image = my_image).pack()
'''

def open():
	root.filename = filedialog.askopenfilename(initialdir = '/Users/Tomcat/Documents/Python/tkinter/images', title = 'Choose the file to show', 
	filetypes = (('JPG files', '*.jpg'), ("PNG files", "*.png"), ("Whatever files", "*.*")))
	my_label = Label(root, text = root.filename).pack()
	my_image = ImageTk.PhotoImage(Image.open(root.filename))
	my_image_label = Label(image = my_image).pack()


my_button = Button(root, text = 'Click to open a file', command = open).pack()

root.mainloop()

