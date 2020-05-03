from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap('images/a.ico')

frame = LabelFrame(root, text= 'This is a frame', padx = 10, pady = 10)
frame.pack(padx=10,pady=10)

b = Button(frame, text = 'This is not a button.', command = root.quit, padx = 10, pady = 10)
b.grid(row = 0, column = 0)
b2 = Button(frame, text = 'This is  a button.', command = root.quit, padx = 10, pady = 10)
b2.grid(row = 1, column =1)

root.mainloop()

