from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
# root.iconbitmap('c:/.../...') # change the default ico


my_img1 = ImageTk.PhotoImage(Image.open('images/a.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('images/b.jpg'))
# my_img3 = ImageTk.PhotoImage(Image.open('images/something3.png'))
# my_img4 = ImageTk.PhotoImage(Image.open('images/something4.png'))

image_list = [my_img1, my_img2] # my_img3, my_img4]

my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0 , columnspan = 3)


def forward(imagenumber):
	global button_back
	global button_forward
	global my_label

	my_label.grid_foget()
	my_label = Label(image = image_list[imagenumber - 1])
	button_forward = Button(root, text = '>>>', command = lambda: forward(imagenumber - 2))
	button_back = Button(root, text = '<<<', command = lambda: back(imagenumber - 1))		

	if imagenumber == 2:
		button_forward = Button(root, text = '>>>', state = DISABLED)

	my_label.grid(row=0, column=0, columnspan = 3)
	button_back.grid(row = 1, column = 0)
	button_forward.grid(row = 1, column= 2)

def back(imagenumber):
	global button_back
	global button_forward
	global my_label

	my_label.grid_foget()
	my_label = Label(image = image_list[imagenumber - 1])
	button_forward = Button(root, text = '>>>', command = lambda: forward(imagenumber - 2))
	button_back = Button(root, text = '<<<', command = lambda: back(imagenumber - 1))		

	if imagenumber == 0:
		button_forward = Button(root, text = '>>>', state = DISABLED)

	my_label.grid(row=0, column=0, columnspan = 3)
	button_back.grid(row = 1, column = 2)
	button_forward.grid(row = 1, column= 0)


button_back = Button(root, text = '<<<', command = lambda: back(imagenumber - 1))
button_exit = Button(root, text = 'Exit Program', command = root.quit)
button_forward = Button(root, text = '>>>', command = lambda: forward(-2))

button_forward.grid(row = 1, column= 0)
button_exit.grid(row = 1, column=1)
button_back.grid(row = 1, column = 2)


root.mainloop()

