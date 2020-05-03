from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap('images/a.ico')

"""
r = IntVar()
r.set('4')
"""
TOPS = [
('Pepperoni', 'Pepperoni')
('Cheese', 'Cheese'),
('Onions', 'Onions'),
]

pizza = StringVar()
pizza.set(3)

for text, code in TOPS:
	Radiobutton(root, text = text, variable = pizza, value = code).pack(anchor = W)
# Radiobutton(root, text = 'it´s a second radio button!', variable = r, value = 2).pack()
# Radiobutton(root, text = 'it´s a third radio button!', variable = r, value = 3).pack()
# Radiobutton(root, text = 'it´s a fourth radio button!', variable = r, value = 4).pack()

#myLabel = Label(root, text = r.get())
#myLabel.pack()

def clicked():
	myLabel = Label(root, text = value)
	myLabel.pack()

myLabel = Label(root, text = pizza.get())
myLabel.pack()


mybutton = Button(root, text = 'Click here', command = lambda: clicked(pizza.get())
mybutton.pack()	


root.mainloop()

