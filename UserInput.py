import sys

#################################################################### 
# process()- Handles the input from the user. If the text field is 
# empty the method returns None and the calling method displays an
# error message. If the text field contains text the method will 
# add ".xlsx" to the end of the file name if it does not already 
# contain it.
#
# @param fileName
####################################################################
def process(fileName):

	# Exit if user input is null
	if fileName is None:
		print("Error in UserInput. Exiting program...")
		sys.exit()
	
	# Return None if the entry box is empty so the calling method can re-prompt the user for input
	if fileName is "":
		return None
		
	# Make sure file is .xlsx formatted
	if fileName.find(".xlsx") < 0:
		fileName += ".xlsx"
		
	return fileName