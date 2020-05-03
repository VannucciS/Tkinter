from tkinter import *

root = Tk()
root.title('Code with images')
root.iconbitmap('c:/.../...')


my_img = ImageTk.PhotoImage(Image.open('images/something.png'))
my_label = Label(image = my_img)
my_label.pack()


root.mainloop()
