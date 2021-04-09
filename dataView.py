from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt




root = Tk()
root.title('It is a data presentation app')
root.iconbitmap('images/a.ico')
root.geometry('400x200')

numberBins = Entry(root)
numberBins.pack()

def graph():
	bins = int(numberBins.get())
	housePrices = np.random.normal(200000, 2500, 5000)
	plt.hist(housePrices, bins)
	plt.show()



graphButton = Button(root, text = "Click the button to generate the graph", command = graph)
graphButton.pack()



root.mainloop()

