from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title('It is a database')
root.iconbitmap('images/a.ico')
#root.geometry('400x400')

# Database

# Create or connect to a database
connection = sqlite3.connect('addressBook.db')

# Create a cursor or instantiate
c = connection.cursor()

"""
# Unable this chunk of code, cause we only want to create the database once
# Create Table
c.execute('''CREATE TABLE adressBook (
			firstName text, 
			lastName text,
			adress text,
			city text,
			state text, 
			phoneNumber integer,
			photo BLOB,
			zipcode real
			)''')
"""

fields = ['fName', 'lName', 'address', 'city', 'state', 'phoneNumber', 'zipcode', 'photo']

# Create a save function
def save():
	# Create or connect to a database
	connection = sqlite3.connect('addressBook.db')
	# Create a cursor or instantiate
	c = connection.cursor()



	# Insert  Into Table
	c.execute("""UPDATE adressBook SET 
		firstName = :first, 
		lastName = :last,
		adress = :address,
		city = :city, 
		state = :state, 
		phoneNumber = :phoneNumber,
		photo = :photo,
		zipcode = :zipcode

		WHERE oid = :oid""",

		{
		'first' : fNameUpdate.get(),
		'last' : lNameUpdate.get(),
		'address' : addressUpdate.get(),
		'city' : cityUpdate.get(),
		'state' : stateUpdate.get(),
		'phoneNumber' : phoneNumberUpdate.get(),
		'photo' : photoUpdate.get(),
		'zipcode' : zipcodeUpdate.get(),
		'oid' : recordId
		}
			)
	# Commit changes
	connection.commit()
	# Close connection	
	connection.close()

	# Clear the text box
	fNameUpdate.delete(0, END)
	lNameUpdate.delete(0, END)
	addressUpdate.delete(0, END)
	cityUpdate.delete(0, END)
	stateUpdate.delete(0, END)
	phoneNumberUpdate.delete(0, END)
	zipcodeUpdate.delete(0, END)
	photoUpdate.delete(0, END)


def update():
	update = Tk()
	update.title('It´s time to update')
	update.iconbitmap('images/a.ico')
	#update.geometry('400x400')	# Create or connect to a database
	
	# Create or connect to a database
	connection = sqlite3.connect('addressBook.db')
	# Create a cursor or instantiate
	c = connection.cursor()

	global recordId
	recordId = deleteBox.get()
	# Query the database
	c.execute("SELECT * FROM adressBook WHERE oid = " + recordId)

	# It can be fetchall = bring all records , fetchone = bring only one record, fetchmany(50) = bring the number written
	records = c.fetchall()
	#print(records)
	'''
	# Loop thru Results
	for record in records:
		fNameUpdate.insert(0, record[0])
		lNameUpdate.insert(0, record[1])
		addressUpdate.insert(0,record[2])
		cityUpdate.insert(0,record[3])
		stateUpdate.insert(0,record[4])
		phoneNumberUpdate.insert(0,record[5])
		zipcodeUpdate.insert(0,record[6])
		photoUpdate.insert(0,record[7])

	'''
	# Create Global Variables for text box names
	global fNameUpdate
	global lNameUpdate
	global addressUpdate
	global cityUpdate
	global stateUpdate
	global phoneNumberUpdate
	global zipcodeUpdate
	global photoUpdate

	# Create the text boxes
	fNameUpdate = Entry(update, width = 30)
	fNameUpdate.grid(row = 0, column = 1, padx = 20, pady = (20,0))
	lNameUpdate = Entry(update, width = 30)
	lNameUpdate.grid(row = 0, column = 3, padx = 20, pady = (20,0))
	addressUpdate = Entry(update, width = 30)
	addressUpdate.grid(row = 1, column = 1)
	cityUpdate = Entry(update, width = 30)
	cityUpdate.grid(row = 1, column = 3)
	stateUpdate = Entry(update, width = 5)
	stateUpdate.grid(row = 1, column = 5)
	phoneNumberUpdate = Entry(update, width = 30)
	phoneNumberUpdate.grid(row = 2, column = 1)
	zipcodeUpdate = Entry(update, width = 30)
	zipcodeUpdate.grid(row = 3, column = 1)
	photoUpdate = Entry(update, width = 30)
	photoUpdate.grid(row = 4, column = 1) # padx = 100, pady = 100)

	

	# Now we gonna create the label of the boxes
	fNameLabelUpdate = Label(update, text = 'Fist Name')
	fNameLabelUpdate.grid(row = 0, column = 0, padx = 20, pady = (20,0))
	lNameLabelUpdate = Label(update, text = 'Last Name')
	lNameLabelUpdate.grid(row = 0, column = 2, padx = 20, pady = (20,0))
	addressLabelUpdate = Label(update, text = 'Address')
	addressLabelUpdate.grid(row = 1, column = 0)
	cityLabelUpdate = Label(update, text = 'City')
	cityLabelUpdate.grid(row = 1, column = 2)
	stateLabelUpdate = Label(update, text = 'State')
	stateLabelUpdate.grid(row = 1, column = 4)
	phoneNumberLabelUpdate = Label(update, text = 'Phone Number')
	phoneNumberLabelUpdate.grid(row = 2, column = 0)
	zipcodeLabelUpdate = Label(update, text = 'Zip Code')
	zipcodeLabelUpdate.grid(row = 3, column = 0)
	photoLabelUpdate = Label(update, text = 'Photo')
	photoLabelUpdate.grid(row = 4, column = 0)

	# Close the window
	exitButton = Button(update, text = 'Close window', command = update.destroy)
	exitButton.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 80 )

	

	# loop thru results
	for record in records:
		fNameUpdate.insert(0, record[0])
		lNameUpdate.insert(0, record[1])
		addressUpdate.insert(0, record[2])
		cityUpdate.insert(0, record[3])
		stateUpdate.insert(0, record[4])
		phoneNumberUpdate.insert(0, record[5])
		zipcodeUpdate.insert(0, record[6])
		photoUpdate.insert(0, record[7])

	# Create a save button to save edited record
	saveButton = Button(update, text = 'Click to save the changes', command = save, fg = 'black', bg = 'red')
	saveButton.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 50)



	# Commit changes
	connection.commit()
	# Close connection
	connection.close()



# Create a function to delete a record
def delete():
	# Create or connect to a database
	connection = sqlite3.connect('addressBook.db')
	# Create a cursor or instantiate
	c = connection.cursor()

	# Delete a record
	c.execute("DELETE FROM adressBook WHERE oid = " + deleteBox.get())

	deleteBox.delete(0, END)

	# Commit changes
	connection.commit()
	# Close connection
	connection.close()




# create a submit function for database
def submit():
	# Create or connect to a database
	connection = sqlite3.connect('addressBook.db')
	# Create a cursor or instantiate
	c = connection.cursor()

	# Insert  Into Table
	c.execute("INSERT INTO adressBook VALUES (:fName, :lName, :address, :city, :state, :phoneNumber, :zipcode, :photo)",
			{ 
				'fName' : fName.get(),
				'lName' : lName.get(),
				'address' : address.get(),
				'city' : city.get(),
				'state' : state.get(),
				'phoneNumber' : phoneNumber.get(),
 				'zipcode' : zipcode.get(),
 				'photo' : photo.get()
			})

	# Commit changes
	connection.commit()
	# Close connection
	connection.close()

	# Clear the text box
	fName.delete(0, END)
	lName.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	phoneNumber.delete(0, END)
	zipcode.delete(0, END)
	photo.delete(0, END)

# Create a query function

def query():
	# Create or connect to a database
	connection = sqlite3.connect('addressBook.db')
	# Create a cursor or instantiate
	c = connection.cursor()

	# Query the database
	c.execute("SELECT *, oid from adressBook")
	# It can be fetchall = bring all records , fetchone = bring only one record, fetchmany(50) = bring the number written
	records = c.fetchall()
	print(records)

	# Loop thru results
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + '\t' +str(record[8]) +'\n'

	queryLabel = Label(root, text = print_records)
	queryLabel.grid(row = 7,column = 0)

	# Commit changes
	connection.commit()
	# Close connection
	connection.close()


# Create the text boxes

fName = Entry(root, width = 30)
fName.grid(row = 0, column = 1, padx = 20, pady = (20,0))
lName = Entry(root, width = 30)
lName.grid(row = 0, column = 3, padx = 20, pady = (20,0))
address = Entry(root, width = 30)
address.grid(row = 1, column = 1)
city = Entry(root, width = 30)
city.grid(row = 1, column = 3)
state = Entry(root, width = 5)
state.grid(row = 1, column = 5)
phoneNumber = Entry(root, width = 30)
phoneNumber.grid(row = 2, column = 1)
zipcode = Entry(root, width = 30)
zipcode.grid(row = 3, column = 1)
photo = Entry(root, width = 30)
photo.grid(row = 4, column = 1) # padx = 100, pady = 100)

deleteBox = Entry(root, width =30, bg = 'yellow', fg = 'blue')
deleteBox.grid(row = 9, column = 1)

# Now we gonna create the label of the boxes

fNameLabel = Label(root, text = 'Fist Name')
fNameLabel.grid(row = 0, column = 0, padx = 20, pady = (20,0))
lNameLabel = Label(root, text = 'Last Name')
lNameLabel.grid(row = 0, column = 2, padx = 20, pady = (20,0))
addressLabel = Label(root, text = 'Address')
addressLabel.grid(row = 1, column = 0)
cityLabel = Label(root, text = 'City')
cityLabel.grid(row = 1, column = 2)
stateLabel = Label(root, text = 'State')
stateLabel.grid(row = 1, column = 4)
phoneNumberLabel = Label(root, text = 'Phone Number')
phoneNumberLabel.grid(row = 2, column = 0)
zipcodeLabel = Label(root, text = 'Zip Code')
zipcodeLabel.grid(row = 3, column = 0)
photoLabel = Label(root, text = 'Photo')
photoLabel.grid(row = 4, column = 0)

deleteBoxLabel = Label(root, text = 'Select ID').grid(row = 9, column = 0)

# Create a submit button
submitButton = Button(root, text = 'Submit button', command = submit)
submitButton.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 100)

# Create a query button
queryButton = Button(root, text = 'Click to query', command = query)
queryButton.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# Create a delete button
deleteButton = Button(root, text = 'Click to delete a record', command = delete)
deleteButton.grid(row = 9, column = 2, columnspan = 2, pady = 10, padx = 10, ipadx = 50)

# Create a update button
updateButton = Button(root, text = 'Click to update a record', command = update,bg = 'pink', fg = 'white')
updateButton.grid(row = 10, column = 2, columnspan = 2, pady = 10, padx = 10, ipadx = 50)

# exit the program
exitButton = Button(root, text = 'Exit', command = root.quit)
exitButton.grid(row = 8, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100 )

# Commit changes
connection.commit()

# Close connection
connection.close()


root.mainloop()

