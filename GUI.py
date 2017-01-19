#from tkinter import * #Windows
#from tkinter import messagebox #Windows
from Tkinter import * #Mac
import tkMessageBox #Mac
import UserInput
import ExcelRip
import ExtractData
import SummaryData
import Output

#################################################################### 
# QwickRip (class)- When a QwickRip Object is created this class 
# builds the Graphical User Interface for the program. The class 
# takes in a window parameter.
####################################################################
class QwickRip:
	 
	#################################################################### 
	# __init__() - This is the constructor for the QwickRip class. It 
	# takes in a window parameter to be built upon. It sets the title 
	# of the window, and calls the builGUI() to set up the appearance 
	# of the GUI.
	#
	# @param self
	# @param master The window to be built upon
	####################################################################
	def __init__(self, master):
		self.master = master
		master.title("Qwick Rip")
		self.buildGUI()
	
	#################################################################### 
	# allSelect() - Handles the actions of the "All" checkbox. 
	# Responsible for toggling all of the other check boxes depending on
	# whether or not it is checked
	#
	# @param self
	####################################################################
	def allSelect(self):
		if self.allCheckVar.get() == 1:
			self.moneyCheck.select()
			self.banksCheck.select()
			self.cardsCheck.select()
			self.bitCoinsCheck.select()
			self.emailsCheck.select()
			self.websitesCheck.select()
			self.ipCheck.select()	
			self.countriesCheck.select()
		else:
			self.moneyCheck.deselect()
			self.banksCheck.deselect()
			self.cardsCheck.deselect()
			self.bitCoinsCheck.deselect()
			self.emailsCheck.deselect()
			self.websitesCheck.deselect()
			self.ipCheck.deselect()	
			self.countriesCheck.deselect()	
		
	#################################################################### 
	# buildGUI() - Builds the Graphical User Interface. Adds components 
	# to the master parameter that was passed in to the class. 
	#
	# @param self
	####################################################################
	def buildGUI(self):
		
		# Build Frames
		self.top = Frame(self.master)
		self.top.pack()

		self.bottom = Frame(self.master)
		self.bottom.pack()

		# Money
		self.moneyCheckVar = IntVar()
		self.moneyCheck = Checkbutton (self.top, text="Money", variable = self.moneyCheckVar, command=self.toggleAll)
		self.moneyCheck.grid(row=0, column=0, sticky='w')

		self.moneyRadioButtons = Frame(self.top)
		self.moneyRadioButtons.grid(row=0, column=1, sticky='w')

		self.moneyVar = IntVar()
		self.moneyVar.set("1")
		self.moneyFrequencyRadio = Radiobutton(self.moneyRadioButtons, text="Frequency", variable=self.moneyVar, value=1)
		self.moneyFrequencyRadio.pack(side=LEFT)
		self.moneyDescendingRadio = Radiobutton(self.moneyRadioButtons, text="Descending Order", variable=self.moneyVar, value=2)
		self.moneyDescendingRadio.pack(side=LEFT)
	
		# Banks
		self.banksCheckVar = IntVar()
		self.banksCheck = Checkbutton (self.top, text="Banks", variable = self.banksCheckVar, command=self.toggleAll)
		self.banksCheck.grid(row=1, column=0, sticky='w')

		self.banksRadioButtons = Frame(self.top)
		self.banksRadioButtons.grid(row=1, column=1, sticky='w')

		self.banksVar = IntVar()
		self.banksVar.set("1")
		self.banksFrequencyRadio = Radiobutton(self.banksRadioButtons, text="Frequency", variable=self.banksVar, value=1)
		self.banksFrequencyRadio.pack(side=LEFT)
		self.banksAlphaRadio = Radiobutton(self.banksRadioButtons, text="Aphabetized", variable=self.banksVar, value=2)
		self.banksAlphaRadio.pack(side=LEFT)

		# Cards
		self.cardsCheckVar = IntVar()
		self.cardsCheck = Checkbutton (self.top, text="Credit/Debit Cards", variable = self.cardsCheckVar, command=self.toggleAll)
		self.cardsCheck.grid(row=2, column=0, sticky='w')

		self.cardsRadioButtons = Frame(self.top)
		self.cardsRadioButtons.grid(row=2, column=1, sticky='w')

		self.cardsVar = IntVar()
		self.cardsVar.set("1")
		self.cardsFrequencyRadio = Radiobutton(self.cardsRadioButtons, text="Frequency", variable=self.cardsVar, value=1)
		self.cardsFrequencyRadio.pack(side=LEFT)

		# Bitcoin Addresses
		self.bitCoinsCheckVar = IntVar()
		self.bitCoinsCheck = Checkbutton (self.top, text="Bitcoin Addresses", variable = self.bitCoinsCheckVar, command=self.toggleAll)
		self.bitCoinsCheck.grid(row=3, column=0, sticky='w')

		self.bitRadioButtons = Frame(self.top)
		self.bitRadioButtons.grid(row=3, column=1, sticky='w')

		self.bitCoinsVar = IntVar()
		self.bitCoinsVar.set("1")
		self.bitCoinsFrequencyRadio = Radiobutton(self.bitRadioButtons, text="Frequency", variable=self.bitCoinsVar, value=1)
		self.bitCoinsFrequencyRadio.pack(side=LEFT)

		# Emails
		self.emailsCheckVar = IntVar()
		self.emailsCheck = Checkbutton (self.top, text="Emails", variable = self.emailsCheckVar, command=self.toggleAll)
		self.emailsCheck.grid(row=4, column=0, sticky='w')

		self.emailsRadioButtons = Frame(self.top)
		self.emailsRadioButtons.grid(row=4, column=1, sticky='w')

		self.emailsVar = IntVar()
		self.emailsVar.set("1")
		self.emailsFrequencyRadio = Radiobutton(self.emailsRadioButtons, text="Frequency", variable=self.emailsVar, value=1)
		self.emailsFrequencyRadio.pack(side=LEFT)
		self.emailsUserAlphaRadio = Radiobutton(self.emailsRadioButtons, text="Aphabetized by User Name", variable=self.emailsVar, value=2)
		self.emailsUserAlphaRadio.pack(side=LEFT)
		self.emailsDomainAlphaRadio = Radiobutton(self.emailsRadioButtons, text="Aphabetized by Domain Name", variable=self.emailsVar, value=3)
		self.emailsDomainAlphaRadio.pack(side=LEFT)

		# Websites
		self.websitesCheckVar = IntVar()
		self.websitesCheck = Checkbutton (self.top, text="Websites", variable=self.websitesCheckVar, command=self.toggleAll)
		self.websitesCheck.grid(row=5, column=0, sticky='w')

		self.websitesRadioButtons = Frame(self.top)
		self.websitesRadioButtons.grid(row=5, column=1, sticky='w')

		self.websitesVar = IntVar()
		self.websitesVar.set("1")
		self.websitesFrequencyRadio = Radiobutton(self.websitesRadioButtons, text="Frequency", variable=self.websitesVar, value=1)
		self.websitesFrequencyRadio.pack(side=LEFT)
		self.websitesAlphaRadio = Radiobutton(self.websitesRadioButtons, text="Aphabetized", variable=self.websitesVar, value=2)
		self.websitesAlphaRadio.pack(side=LEFT)

		# IP Addresses
		self.ipCheckVar = IntVar()
		self.ipCheck = Checkbutton (self.top, text="IP Addresses", variable=self.ipCheckVar, command=self.toggleAll)
		self.ipCheck.grid(row=6, column=0, sticky='w')

		self.ipRadioButtons = Frame(self.top)
		self.ipRadioButtons.grid(row=6, column=1, sticky='w')

		self.ipVar = IntVar()
		self.ipVar.set("1")
		self.ipFrequencyRadio = Radiobutton(self.ipRadioButtons, text="Frequency", variable=self.ipVar, value=1)
		self.ipFrequencyRadio.pack(side=LEFT)

		# Countries
		self.countriesCheckVar = IntVar()
		self.countriesCheck = Checkbutton (self.top, text="Countries", variable=self.countriesCheckVar, command=self.toggleAll)
		self.countriesCheck.grid(row=7, column=0, sticky='w')

		self.countriesRadioButtons = Frame(self.top)
		self.countriesRadioButtons.grid(row=7, column=1, sticky='w')

		self.countriesVar = IntVar()
		self.countriesVar.set("1")
		self.countriesFrequencyRadio = Radiobutton(self.countriesRadioButtons, text="Frequency", variable=self.countriesVar, value=1)
		self.countriesFrequencyRadio.pack(side=LEFT)
		self.countriesAlphaRadio = Radiobutton(self.countriesRadioButtons, text="Alphabetized", variable=self.countriesVar, value=2)
		self.countriesAlphaRadio.pack(side=LEFT)
		
		# All
		self.allCheckVar = IntVar()
		self.allCheck = Checkbutton (self.top, text="All", variable=self.allCheckVar, command=self.allSelect)
		self.allCheck.grid(row=8, column=0, sticky='w')

		# Summary Data Only
		self.onlyFrame = Frame(self.top)
		self.onlyFrame.grid(row=9, column=0, sticky='w')

		self.onlyCheckVar = IntVar()
		self.onlyCheck = Checkbutton (self.onlyFrame, text="Summary Data Only", variable=self.onlyCheckVar, pady=15)
		self.onlyCheck.pack()

		# Input Label
		self.inputLabel = Label(self.bottom, text="Enter file name:")
		self.inputLabel.pack(side=LEFT)

		# Input Text Field
		self.inputBox = Entry(self.bottom)
		self.inputBox.pack(side=LEFT)

		# Browse Button
		self.browseButton = Button(self.bottom, text="Browse", padx=10)
		self.browseButton.pack(side=LEFT)

		# Clear Button
		self.clearButton = Button(self.bottom, text="Clear", padx=10, command=self.clearButtonClick)
		self.clearButton.pack(side=LEFT)

		# Search Button
		self.searchButton = Button(self.bottom, text="Search", padx=10, command=self.searchButtonClick)
		self.searchButton.pack(side=LEFT)

	#################################################################### 
	# clearButtonClick() - Handles the actions of the "Clear" button.
	# When clicked the button should clear the text field, uncheck all
	# check boxes, and reset all radio buttons to their default position.
	#
	# @param self
	####################################################################
	def clearButtonClick(self):
		
		# Clear text field
		self.inputBox.delete(0, END)
		
		# Clear checkboxes
		self.moneyCheck.deselect()
		self.banksCheck.deselect()
		self.cardsCheck.deselect()
		self.bitCoinsCheck.deselect()
		self.emailsCheck.deselect()
		self.websitesCheck.deselect()
		self.ipCheck.deselect()
		self.countriesCheck.deselect()
		self.allCheck.deselect()
		self.onlyCheck.deselect()
		
		# Reset radio buttons
		self.moneyVar.set("1")
		self.banksVar.set("1")
		self.cardsVar.set("1")
		self.bitCoinsVar.set("1")
		self.emailsVar.set("1")
		self.websitesVar.set("1")
		self.ipVar.set("1")
		self.countriesVar.set("1")
	
	#################################################################### 
	# searchButtonClick() - Handles the actions of the "Search" button.
	# When the button is clicked the method gets the user input from the 
	# text field, and makes sure it is valid (If input is invalid an
	# error message will pop up telling the user the appropriate message).
	# The method will then proceed to rip the narratives and BSA IDs 
	# from the specified excel file (If an error occurs let the user	
	# know). The method will then proceed to extract all of the
	# data that the user has checked off that they want. Once the data
	# is obtained the method will summarize the data and send it out for 
	# output. 
	#
	# @param self
	####################################################################
	def searchButtonClick(self):
		
		# Variables
		moneySummary = {}
		banksSummary = {}
		cardsSummary = {}
		bitCoinsSummary = {}
		emailsSummary = {}
		websitesSummary = {}
		ipSummary = {}
		countriesSummary = {}
		
		# Get file name from entry box and make sure it exists
		fileName = UserInput.process(self.inputBox.get())
		
		# Prompt user to enter a file name if the entry box is empty
		if fileName is None:
# 			messagebox.showinfo("Error", "Please enter a file name in the text field") #Windows
			tkMessageBox.showinfo("Error", "Please enter a file name in the text field") #Mac
			return 
			
		# Rip data from excel spreadsheet 
		sars = ExcelRip.ripData(fileName)
			
		# Handle potential file errors
		if sars is None:
# 			messagebox.showinfo("File Not Found", "Make sure the file name is spelled correctly.\n" + \
# 				                "If spelled correctly, make sure file is saved as .xlsx")	#Windows
			
			tkMessageBox.showinfo("File Not Found",	"Make sure the file name is spelled correctly.\n" + \
				                  "If spelled correctly, make sure file is saved as .xlsx") #Mac
			return

		# Extract data from SARs
		extractedSars = ExtractData.extractFrom(sars, self.moneyCheckVar.get(), self.banksCheckVar.get(), \
												self.cardsCheckVar.get(), self.bitCoinsCheckVar.get(), \
												self.emailsCheckVar.get(), self.websitesCheckVar.get(), \
												self.ipCheckVar.get(), self.countriesCheckVar.get())
		
		# Get summary data from the extracted data
		SummaryData.get(extractedSars, moneySummary, banksSummary, cardsSummary, bitCoinsSummary, \
						emailsSummary, websitesSummary, ipSummary, countriesSummary, \
						self.moneyCheckVar.get(), self.banksCheckVar.get(), self.cardsCheckVar.get(), \
						self.bitCoinsCheckVar.get(), self.emailsCheckVar.get(), self.websitesCheckVar.get(), \
						self.ipCheckVar.get(), self.countriesCheckVar.get())
		
		# Handle Output
		Output.handle(extractedSars, self.onlyCheckVar.get(), self.allCheckVar.get(), \
					  self.moneyCheckVar.get(), self.moneyVar.get(), moneySummary, \
					  self.banksCheckVar.get(), self.banksVar.get(), banksSummary, \
					  self.cardsCheckVar.get(), self.cardsVar.get(), cardsSummary,\
					  self.bitCoinsCheckVar.get(), self.bitCoinsVar.get(), bitCoinsSummary, \
					  self.emailsCheckVar.get(), self.emailsVar.get(), emailsSummary,\
					  self.websitesCheckVar.get(), self.websitesVar.get(), websitesSummary, \
					  self.ipCheckVar.get(), self.ipVar.get(), ipSummary, \
					  self.countriesCheckVar.get(), self.countriesVar.get(), countriesSummary)
			
	#################################################################### 
	# toggleAll() - Toggles the "All" check box on and off based on the
	# other check boxes.
	#
	# @param self
	####################################################################
	def toggleAll(self):

		# All is only to be checked if all other check boxes are selected
		if self.moneyCheckVar.get() == 1 and self.banksCheckVar.get() == 1 and self.cardsCheckVar.get() ==  1 and \
		   self.bitCoinsCheckVar.get() == 1 and self.emailsCheckVar.get() == 1 and self.websitesCheckVar.get() == 1 and \
		   self.ipCheckVar.get() == 1 and self.countriesCheckVar.get() == 1:
			self.allCheck.select()
		else:	
			self.allCheck.deselect()
		
#################################################################### 
# initializeGUI() - Passes a window object to the QwickRip class to
# create a QwickRip Object and a GUI for the program.
####################################################################	
def initializeGUI():
	root = Tk()
	qwickRip = QwickRip(root)
	root.mainloop()
	
	

