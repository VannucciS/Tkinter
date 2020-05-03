from tkinter import *

root = Tk()

e = Entry(root, width=50, fg = 'green', bg = 'purple', borderwidth = 5)
e.pack()
e.insert(0, 'enter your name')

# Make the buttons works

def myClick():
	myLabel = Label(root, text='hello ' + e.get())
	myLabel.pack()

# Create buttons

myButton = Button(root, text='Enter your name: ', padx=50, pady=50, command = myClick, fg = 'blue', bg = 'yellow')
myButton.pack()

root.mainloop()
