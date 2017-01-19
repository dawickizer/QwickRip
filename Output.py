import collections
# from tkinter import * #Windows
# from tkinter import messagebox #Windows
from Tkinter import * #Mac
import tkMessageBox #Mac

#################################################################### 
# alphabetize()- Alphabetizes a dictionary and writes it to an 
# output file.
#
# @param dictionary The dictionary to be alphabetized 
# @param outputFile The file to be written to
####################################################################
def alphabetize(dictionary, outputFile):

	od = collections.OrderedDict(sorted(dictionary.items()))
	for k, v in od.items(): 
		string = k + " " + str(v) + "\n"
		outputFile.write(string)

#################################################################### 
# alphaByDomain()- Alphabetizes a dictionary of emails by the domain
# name of the email, and writes it to an output file.
#
# @param dictionary The dictionary to be alphabetized 
# @param outputFile The file to be written to
####################################################################
def alphaByDomain(dictionary, outputFile):

	# Create list of tuples containing key/value pairs sorted by domain name...then by user name
	list = sorted(dictionary.items(), key=lambda item: (item[0][item[0].find("@") + 1:], item[0])) #item[1] for frequency
	
	# Write to file
	for tuple in list:
		line = ' '.join(str(x) for x in tuple)
		outputFile.write(line + '\n')	

#################################################################### 
# descendingKey()- Sorts a dictionary in descending order by key,
# and stores the dictionary to an output file.
#
# @param dictionary The dictionary to be sorted 
# @param outputFile The file to be written to
####################################################################
def descendingKey(dictionary, outputFile):

	# Sort dictionary in descending order by key
	# Store in list of tuples
	# Write to file
	list = sorted(dictionary.items(), key=lambda x: (-float(x[0][1:])))
	for tuple in list:
		line = ' '.join(str(x) for x in tuple)
		outputFile.write(line + '\n')		
	
#################################################################### 
# descendingValue()- Sorts a dictionary in descending order by value,
# then by alphabetical order, and stores the dictionary to an output file.
#
# @param dictionary The dictionary to be sorted 
# @param outputFile The file to be written to
####################################################################
def descendingValue(dictionary, outputFile):

	# Sort dictionary in descending order by value (frequency of occurrence), then by alphabetical order
	# Store in list of tuples
	# Write to file
	list = sorted(dictionary.items(), key=lambda x: (-x[1], x[0][1:])) #-float(x[0][1:])
	for tuple in list:
		line = ' '.join(str(x) for x in tuple)
		outputFile.write(line + '\n')	
		
#########################################################################################
# handle()- Handles the output based on the users desired specifications.
#
# @param extractedSars Contains the data to be output
# @param summaryDataOnlyChecked Check box for Summary Data Only. 1 if selected...0 if not
# @param allChecked Check box for All. 1 if selected...0 if not
# @param moneyChecked Check box for money. 1 if selected...0 if not
# @param moneyRadio Radio button for money to determine output format
# @param moneySummary Dictionary containing summary data for money
# @param banksChecked Check box for banks. 1 if selected...0 if not
# @param banksRadio Radio button for banks to determine output format
# @param banksSummary Dictionary containing summary data for banks
# @param cardsChecked Check box for cards. 1 if selected...0 if not
# @param cardsRadio Radio button for cards to determine output format
# @param cardsSummary Dictionary containing summary data for cards
# @param bitCoinsChecked Check box for bitcoin addresses. 1 if selected...0 if not
# @param bitsRadio Radio button for bitcoin addresses to determine output format
# @param bitsSummary Dictionary containing summary data for bitcoin addresses
# @param emailsChecked Check box for emails. 1 if selected...0 if not
# @param emailsRadio Radio button for emails to determine output format
# @param emailsSummary Dictionary containing summary data for emails
# @param websitesChecked Check box for websites. 1 if selected...0 if not
# @param websitesRadio Radio button for websites to determine output format
# @param websitesSummary Dictionary containing summary data for websites
# @param ipChecked Check box for IP addresses. 1 if selected...0 if not
# @param ipRadio Radio button for IP addresses to determine output format
# @param ipSummary Dictionary containing summary data for IP addresses
# @param countriesChecked Check box for countries. 1 if selected...0 if not
# @param countriesRadio Radio button for countries to determine output format
# @param countriesSummary Dictionary containing summary data for countries
#########################################################################################
def handle(extractedSars, summaryDataOnlyChecked, allChecked, moneyChecked, moneyRadio, moneySummary, \
		   banksChecked, banksRadio, banksSummary, cardsChecked, cardsRadio, cardsSummary, \
		   bitCoinsChecked, bitsRadio, bitsSummary, emailsChecked, emailsRadio, emailsSummary, \
		   websitesChecked, websitesRadio, websitesSummary, ipChecked, ipRadio, ipSummary, \
		   countriesChecked, countriesRadio, countriesSummary):
		   
	# Open outpuut file
	outputFile = open("RippedData.txt", "w")
	
	# Set data to false as default until found
	data = False
				
	# Handle individual output
	for sar in extractedSars:
	
		# Check to see if data was found in search
		if data == False:
			if len(getattr(sar, "moneyDict")) > 0 or len(getattr(sar, "banksDict")) > 0 \
			or len(getattr(sar, "creditCardsDict")) > 0 or len(getattr(sar, "bitCoinAddressesDict")) > 0 \
			or len(getattr(sar, "emailsDict")) > 0 or len(getattr(sar, "websitesDict")) > 0 \
			or len(getattr(sar, "ipAddressesDict")) > 0 or len(getattr(sar, "countriesDict")) > 0:
				data = True
		
		# Handle individual output if summary data only is NOT checked
		if summaryDataOnlyChecked == False:
			bsa = True
		
			# Only output money if checked and dict contains values
			if moneyChecked == True and len(getattr(sar, "moneyDict")) > 0:
				if bsa == True:					
					outputFile.write("BSA ID: " + getattr(sar, "bsaID"))
					outputFile.write("\n-------------------------------\n\n")
					bsa = False
				outputMoney(getattr(sar, "moneyDict"), moneyRadio, outputFile)
				outputFile.write("\n")
				
			# Only output banks if checked and dict contains values			
			if banksChecked == True and len(getattr(sar, "banksDict")) > 0:
				if bsa == True:					
					outputFile.write("BSA ID: " + getattr(sar, "bsaID"))
					outputFile.write("\n-------------------------------\n\n")
					bsa = False
				outputBanks(getattr(sar, "banksDict"), banksRadio, outputFile)
				outputFile.write("\n")
				
			# Only output cards if checked and dict contains values		
			if cardsChecked == True and len(getattr(sar, "creditCardsDict")) > 0:
				if bsa == True:					
					outputFile.write("BSA ID: " + getattr(sar, "bsaID"))
					outputFile.write("\n-------------------------------\n\n")
					bsa = False
				outputCards(getattr(sar, "creditCardsDict"), cardsRadio, outputFile)
				outputFile.write("\n")
				
			# Only output bitcoin addresses if checked and dict contains values	
			if bitCoinsChecked == True and len(getattr(sar, "bitCoinAddressesDict")) > 0:
				if bsa == True:					
					outputFile.write("BSA ID: " + getattr(sar, "bsaID"))
					outputFile.write("\n-------------------------------\n\n")
					bsa = False
				outputBitCoins(getattr(sar, "bitCoinAddressesDict"), bitsRadio, outputFile)
				outputFile.write("\n")
				
			# Only output emails if checked and dict contains values	
			if emailsChecked == True and len(getattr(sar, "emailsDict")) > 0:	
				if bsa == True:					
					outputFile.write("BSA ID: " + getattr(sar, "bsaID"))
					outputFile.write("\n-------------------------------\n\n")
					bsa = False
				outputEmails(getattr(sar, "emailsDict"), emailsRadio, outputFile)
				outputFile.write("\n")
				
			# Only output websites if checked and dict contains values	
			if websitesChecked == True and len(getattr(sar, "websitesDict")) > 0:
				if bsa == True:					
					outputFile.write("BSA ID: " + getattr(sar, "bsaID"))
					outputFile.write("\n-------------------------------\n\n")
					bsa = False
				outputWebsites(getattr(sar, "websitesDict"), websitesRadio, outputFile)
				outputFile.write("\n")
				
			# Only output ip addresses if checked and dict contains values
			if ipChecked == True and len(getattr(sar, "ipAddressesDict")) > 0:
				if bsa == True:					
					outputFile.write("BSA ID: " + getattr(sar, "bsaID"))
					outputFile.write("\n-------------------------------\n\n")
					bsa = False
				outputIp(getattr(sar, "ipAddressesDict"), ipRadio, outputFile)
				outputFile.write("\n")
				
			# Only output countries if checked and dict contains values	
			if countriesChecked == True and len(getattr(sar, "countriesDict")) > 0:
				if bsa == True:					
					outputFile.write("BSA ID: " + getattr(sar, "bsaID"))
					outputFile.write("\n-------------------------------\n\n")
					bsa = False
				outputCountries(getattr(sar, "countriesDict"), countriesRadio, outputFile)
				outputFile.write("\n")
		
	# Determine if there is data to be output
	if data == True:
		outputSummaryData(outputFile, moneyChecked, moneyRadio, moneySummary, \
					  banksChecked, banksRadio, banksSummary, cardsChecked, cardsRadio, \
					  cardsSummary, bitCoinsChecked, bitsRadio, bitsSummary, emailsChecked, \
					  emailsRadio, emailsSummary, websitesChecked, websitesRadio, websitesSummary, \
					  ipChecked, ipRadio, ipSummary, countriesChecked, countriesRadio, countriesSummary)
		
	else:
		messagebox.showinfo("Notice", "No data was found in search") #Windows
		#tkMessageBox.showinfo("Error", "Please enter a file name in the text field")
		
	# Close output file
	outputFile.close()

#################################################################### 
# outputBanks()- Output banks
#
# @param banksDict The dictionary to be output
# @param banksRadio Radio button for determining format of output
# @param outputFile File to be written to
####################################################################					  
def outputBanks(banksDict, banksRadio, outputFile):
	outputFile.write("Banks:\n")
	outputFile.write("------\n")
	
	# If 1...order by frequency...else alphabetize
	if banksRadio == 1:
		descendingValue(banksDict, outputFile)
	else:
		alphabetize(banksDict, outputFile)

#################################################################### 
# outputBitCoins()- Output bitcoin addresses
#
# @param bitCoinsDict The dictionary to be output
# @param bitsRadio Radio button for determining format of output
# @param outputFile File to be written to
####################################################################						  
def outputBitCoins(bitCoinsDict, bitsRadio, outputFile):
	outputFile.write("Bitcoin Addresses:\n")
	outputFile.write("------------------\n")
	if bitsRadio == 1:
		descendingValue(bitCoinsDict, outputFile)

#################################################################### 
# outputCards()- Output credit/debit cards
#
# @param cardsDict The dictionary to be output
# @param cardsRadio Radio button for determining format of output
# @param outputFile File to be written to
####################################################################							  
def outputCards(cardsDict, cardsRadio, outputFile):
	outputFile.write("Credit/Debit Cards:\n")
	outputFile.write("-------------------\n")
	if cardsRadio == 1:
		descendingValue(cardsDict, outputFile)

#################################################################### 
# outputCountries()- Output countries
#
# @param countriesDict The dictionary to be output
# @param countriesRadio Radio button for determining format of output
# @param outputFile File to be written to
####################################################################			
def outputCountries(countriesDict, countriesRadio, outputFile):
	outputFile.write("Countries:\n")
	outputFile.write("----------\n")
	
	# If 1...order by frequency...else alphabetize
	if countriesRadio == 1:
		descendingValue(countriesDict, outputFile)
	else:
		alphabetize(countriesDict, outputFile)
		
#################################################################### 
# outputEmails()- Output emails
#
# @param emailsDict The dictionary to be output
# @param emailsRadio Radio button for determining format of output
# @param outputFile File to be written to
####################################################################							  
def outputEmails(emailsDict, emailsRadio, outputFile):
	outputFile.write("Emails:\n")
	outputFile.write("-------\n")
	
	# If 1 order by frequency...if 2 alphabetize by user name...if 3 alphabetize by domain name
	if emailsRadio == 1:
		descendingValue(emailsDict, outputFile)
	elif emailsRadio == 2:
		alphabetize(emailsDict, outputFile)	
	elif emailsRadio == 3:
		alphaByDomain(emailsDict, outputFile)

#################################################################### 
# outputIp()- Output IP addresses
#
# @param ipDict The dictionary to be output
# @param ipRadio Radio button for determining format of output
# @param outputFile File to be written to
####################################################################				  
def outputIp(ipDict, ipRadio, outputFile):
	outputFile.write("IP Addresses:\n")
	outputFile.write("-------------\n")
	if ipRadio == 1:
		descendingValue(ipDict, outputFile)
	
#################################################################### 
# outputMoney()- Output money
#
# @param moneyDict The dictionary to be output
# @param moneyRadio Radio button for determining format of output
# @param outputFile File to be written to
####################################################################						  
def outputMoney(moneyDict, moneyRadio, outputFile):
	outputFile.write("Money:\n")
	outputFile.write("------\n")
	
	# If 1...order by frequency...else order in descending order
	if moneyRadio == 1:
		descendingValue(moneyDict, outputFile) # Works but order by desc after freq
	else:
		descendingKey(moneyDict, outputFile)

#######################################################################################
# outputSummaryData()- Output the summary data
#
# @param outputFile The file to be written to
# @param moneyChecked Check box for money. 1 if selected...0 if not
# @param moneyRadio Radio button for money to determine output format
# @param moneySummary Dictionary containing summary data for money
# @param banksChecked Check box for banks. 1 if selected...0 if not
# @param banksRadio Radio button for banks to determine output format
# @param banksSummary Dictionary containing summary data for banks
# @param cardsChecked Check box for cards. 1 if selected...0 if not
# @param cardsRadio Radio button for cards to determine output format
# @param cardsSummary Dictionary containing summary data for cards
# @param bitCoinsChecked Check box for bitcoin addresses. 1 if selected...0 if not
# @param bitsRadio Radio button for bitcoin addresses to determine output format
# @param bitsSummary Dictionary containing summary data for bitcoin addresses
# @param emailsChecked Check box for emails. 1 if selected...0 if not
# @param emailsRadio Radio button for emails to determine output format
# @param emailsSummary Dictionary containing summary data for emails
# @param websitesChecked Check box for websites. 1 if selected...0 if not
# @param websitesRadio Radio button for websites to determine output format
# @param websitesSummary Dictionary containing summary data for websites
# @param ipChecked Check box for IP addresses. 1 if selected...0 if not
# @param ipRadio Radio button for IP addresses to determine output format
# @param ipSummary Dictionary containing summary data for IP addresses
# @param countriesChecked Check box for countries. 1 if selected...0 if not
# @param countriesRadio Radio button for countries to determine output format
# @param countriesSummary Dictionary containing summary data for countries
#######################################################################################	
def outputSummaryData(outputFile, moneyChecked, moneyRadio, moneySummary, \
					  banksChecked, banksRadio, banksSummary, cardsChecked, cardsRadio, \
					  cardsSummary, bitCoinsChecked, bitsRadio, bitsSummary, emailsChecked, \
					  emailsRadio, emailsSummary, websitesChecked, websitesRadio, websitesSummary, \
					  ipChecked, ipRadio, ipSummary, countriesChecked, countriesRadio, countriesSummary):
	
	
	outputFile.write("Summary Data:\n")
	outputFile.write("------------------------------------\n\n")
	
	# Output summary data based on checkboxes and if dictionaries have values
	if moneyChecked == True and len(moneySummary) > 0:
		outputMoney(moneySummary, moneyRadio, outputFile)
		outputFile.write("\n")		
	if banksChecked == True and len(banksSummary) > 0:
		outputBanks(banksSummary, banksRadio, outputFile)
		outputFile.write("\n")
	if cardsChecked == True and len(cardsSummary) > 0:
		outputCards(cardsSummary, cardsRadio, outputFile)
		outputFile.write("\n")
	if bitCoinsChecked == True and len(bitsSummary) > 0:
		outputBitCoins(bitsSummary, bitsRadio, outputFile)
		outputFile.write("\n")
	if emailsChecked == True and len(emailsSummary) > 0:
		outputEmails(emailsSummary, emailsRadio, outputFile)
		outputFile.write("\n")
	if websitesChecked == True and len(websitesSummary) > 0:
		outputWebsites(websitesSummary, websitesRadio, outputFile)
		outputFile.write("\n")	
	if ipChecked == True and len(ipSummary) > 0:
		outputIp(ipSummary, ipRadio, outputFile)
		outputFile.write("\n")
	if countriesChecked == True and len(countriesSummary) > 0:
		outputCountries(countriesSummary, countriesRadio, outputFile)
		outputFile.write("\n")	
	
#################################################################### 
# outputWebsites()- Output websites
#
# @param websitesDict The dictionary to be output
# @param websitesRadio Radio button for determining format of output
# @param outputFile File to be written to
####################################################################						  
def outputWebsites(websitesDict, websitesRadio, outputFile):
	outputFile.write("Websites:\n")
	outputFile.write("---------\n")
	
	# If 1 order by frequency...else alphabetize
	if websitesRadio == 1:
		descendingValue(websitesDict, outputFile)
	else:
		alphabetize(websitesDict, outputFile)	

