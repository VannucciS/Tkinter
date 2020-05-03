from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title('First window')
root.iconbitmap('images/a.ico')
root.geometry('400x400')

# Dropdown boxes

optionList = [
'Monday', 
'Tuesday', 
'Wednesday', 
'Thurday', 
'Friday'
]

clicked = StringVar()
clicked.set(optionList[1])

drop = OptionMenu(root, clicked, *optionList)
drop.pack()

def show():
	mylabel = Label(root, text = clicked.get())
	mylabel.pack()

myButton = Button(root, text = 'Click here to see the variable', command = show)
myButton.pack()

root.mainloop()

