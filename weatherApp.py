# Learn to connect tkinter to API site
# url docs.airnowapi.org
# http://docs.airnowapi.org/CurrentObservationsByZip/query
# http://docs.airnowapi.org/CurrentObservationsByZip/docs
# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=32821&distance=25&API_KEY=6266EDAD-0636-43F3-922C-4B5361865A0D


from tkinter import *
from PIL import ImageTk, Image
import requests
import json



root = Tk()
root.title('It is a weather desktop app')
root.iconbitmap('images/a.ico')
root.geometry('350x80')

zip = 32821



def zipLookup():
	#result = zip.get()
	#zipLabel = Label(root, text = result)
	#zipLabel.pack()

	try:
		api_url = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=6266EDAD-0636-43F3-922C-4B5361865A0D"
		api_requests = requests.get(api_url)
		api = json.loads(api_requests.content)
		quality = api[0]['AQI']
		city = api[0]['ReportingArea']
		category = api[0]['Category']['Name']

		if category == "Good":
			weatherColor = 'green'
		elif category == "Moderate":
			weatherColor = 'yellow'
		elif category == "Moderate":
			weatherColor = 'yellow'
		elif category == "Unhealthy for Sensitive Groups":
			weatherColor = 'orange'
		elif category == "Unhealthy":
			weatherColor = 'pink'
		elif category == "Very Unhealthy":
			weatherColor = 'light red'
		elif category == "Hazardous":
			weatherColor = 'dark red'

		root.configure(background = weatherColor)

		myLabel = Label(root, text = city + " " +" Air Quality" + " " +str(quality) + " " + category, bg= weatherColor, font = ('Helvetica', 16))
		myLabel.pack()

	except Exception as e:
		api = 'Error...'




zip = Entry(root)
zip.pack()

zipButton = Button(root, text= 'Lookup Zipcode', bg = 'black', fg = 'white', command= zipLookup)
zipButton.pack()






root.mainloop()

