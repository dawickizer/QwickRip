import openpyxl
import UserInput

#################################################################### 
# SarObject (class)- This class takes in a BSA ID and a narrative
# as parameters and pairs them together as a Sar Object.
####################################################################
class SarObject:

	# Variables
	sarCount = 0
	
	#################################################################### 
	# __init__() - This is the constructor for the SarObject class. It 
	# takes in a BSA ID and a narrative.
	#
	# @param self
	# @param narrative The SAR Narrative
	# @param bsaID The Sar BSA ID
	####################################################################
	def __init__(self, narrative, bsaID):
		self.narrative = narrative
		self.bsaID = bsaID
		SarObject.sarCount += 1

	#################################################################### 
	# displayCount() - Displays the count of Sar Objects created
	#
	# @param self
	####################################################################   
	def displayCount(self):
		print("Total SARs created %d\n" % SarObject.sarCount)

	#################################################################### 
	# toString() - Prints a String representation of the Sar Object
	#
	# @param self
	####################################################################
	def toString(self):
		print("Narrative:\n\n" + self.narrative +  "\n\n BSA ID: " + self.bsaID + "\n")

#################################################################### 
# ripData()- Rips data from a specified excel file (.xlsx). The
# function then creates a list of Sar Objects (narratives paired 
# with BSA IDs).
#
# @param fileName The excel file name
# @return sars The list of Sar Objects
####################################################################
def ripData(fileName):	

	# Variables
	bsaIDs = []
	narratives = []
	temp = []
	temp2 = []
	sars = []
	
	# Open Workbook
	while 1:
		try:
			wb = openpyxl.load_workbook(fileName)
			break
		except IOError:
			return None
	
	# Get sheet
	sheet = wb.active

	# Get first column
	for cellObj in sheet.columns[0]:
		temp.append(cellObj.value)

	# Determine content of column
	if temp[0] == "BSA_ID":
		bsaIDs = temp
	else:
		narratives = temp
	
	# Get second column
	for cellObj in sheet.columns[1]:
		temp2.append(cellObj.value)

	# Determine content of second column
	if temp2[0] == "BSA_ID":
		bsaIDs = temp2
	else:
		narratives = temp2
		
	# Create Sars
	i = 1
	while i < len(bsaIDs):
		sars.append(SarObject(str(narratives[i]), str(bsaIDs[i])))
		i += 1
		
	return sars
