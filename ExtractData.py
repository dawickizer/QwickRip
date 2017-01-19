#################################################################### 
# ExtractedSar (class)- This class represents the extracted data 
# from a Sar. This includes the BSA ID, narrative, words, money 
# values, bank names, credit/debit card numbers, bitcoin addresses,
# emails, websites, IP addresses, and country names. 
####################################################################
class ExtractedSar:
	
	#######################################################################################
	# __init__() - This is the constructor for the ExtractedSar class. 
	#
	# @param self
	# @param bsaID The BSA ID of the SAR
	# @param narrative The narrative of the SAR
	# @param words A tokenized list of the words in the narrative
	# @param moneyDict A dictionary of money amounts paired with frequency
	# @param banksDict A dictionary of bank names paired with frequency
	# @param creditCardsDict A dictionary of credit/debit cards paired with frequency
	# @param bitCoinAddressesDict A dictionary of bitcoin addresses paired with frequency
	# @param emailsDict A dictionary of emails paired with frequency
	# @param websitesDict A dictionary of websites paired with frequency
	# @param ipAddresses A dictionary of IP addresses paired with frequency
	# @param countriesDict A dictionary of country names paired with frequency
	#######################################################################################
	def __init__(self, bsaID, narrative, words, moneyDict, banksDict, \
				creditCardsDict, bitCoinAddressesDict, emailsDict, \
				websitesDict, ipAddressesDict, countriesDict):
		self.bsaID = bsaID
		self.narrative = narrative
		self.words = words
		self.moneyDict = moneyDict
		self.banksDict = banksDict
		self.creditCardsDict = creditCardsDict
		self.bitCoinAddressesDict = bitCoinAddressesDict
		self.emailsDict = emailsDict
		self.websitesDict = websitesDict
		self.ipAddressesDict = ipAddressesDict
		self.countriesDict = countriesDict
		
	#################################################################### 
	# toString() - Prints a String representation of the Sar Object
	#
	# @param self
	####################################################################
	def toString(self):
	
		# BSA ID
		print("BSA ID: " + self.bsaID)
		print("-----------------------\n")
		
		# Money
		print("Money:")
		print("-----------------------")
		for money in self.moneyDict:
			print(money + " " + str(self.moneyDict[money]))

		# Banks
		print("\nBanks:")
		print("-----------------------")
		for bank in self.banksDict:
			print(bank + " " + str(self.banksDict[bank]))

		# Credit Cards
		print("\nCredit/Debit Cards:")
		print("-----------------------")
		for card in self.creditCardsDict:
			print(card + " " + str(self.creditCardsDict[card]))

		# Bitcoin Addresses
		print("\nBitcoin Addresses:")
		print("-----------------------")
		for bitCoin in self.bitCoinAddressesDict:
			print(bitCoin + " " + str(self.bitCoinAddressesDict[bitCoin]))
							
		# Emails
		print("\nEmails:")
		print("-----------------------")
		for email in self.emailsDict:
			print(email + " " + str(self.emailsDict[email]))

		# Websites
		print("\nWebsites:")
		print("-----------------------")
		for website in self.websitesDict:
			print(website + " " + str(self.websitesDict[website]))
						
		# IP Addresses
		print("\nIP Addresses:")
		print("-----------------------")
		for ip in self.ipAddressesDict:
			print(ip + " " + str(self.ipAddressesDict[ip]))
									
		print("\n")

		# Countries
		print("\nCountries:")
		print("-----------------------")
		for country in self.countriesDict:
			print(country + " " + str(self.countriesDict[country]))
									
		print("\n")	

#################################################################### 
# buildBankDict()- Builds a dictionary of bank names from the 
# bankList.txt file.
#
# @return bankDict The dictionary of bank names
####################################################################
def buildBankDict():
	bankDict = {}
	with open("bankList.txt") as f:
		bankList = f.readlines()
	bankList = [line.strip() for line in bankList]
	bankDict = bankDict.fromkeys(bankList, 0)
	return bankDict

#################################################################### 
# buildCountriesDict()- Builds a dictionary of country names from 
# the countryList.txt file.
#
# @return countriesDict The dictionary of country names
####################################################################
def buildCountriesDict():
	countriesDict = {}
	with open("countryList.txt") as f:
		countriesList = f.readlines()
	countriesList = [line.strip() for line in countriesList]
	countriesDict = countriesDict.fromkeys(countriesList, 0)
	return countriesDict	

#################################################################### 
# buildTLDList()- Builds a list of Top Level Domains from the
# tldList.txt file.
#
# @return tldList The list of TLDs
####################################################################
def buildTLDList():
	with open("TLDList.txt") as f:
		tldList = f.readlines()
	return tldList

#################################################################### 
# countOccurrences()- Counts the number of times an item occurs in a
# list and returns a dictionary with keys representing the items of 
# the list, and values representing the number count of each 
# occurrence of each item
#
# @param dict The dictionary to store the items of a list paired with
# the number of occurrences of each item.
# @param list The list to be counted.
# @return dict The dictionary that has been setup
####################################################################
def countOccurrences(dict, list):
	for item in list:
		for key in dict:
			if key == item:
				dict[key] += 1
	return dict
				
#################################################################### 
# extractFrom()- Extract key data from a list of SAR Objects.
#
# @param sars The list of SARs to be extracted from
# @param money Determines if moneyDict is to be built
# @param banks Determines if banksDict is to be built
# @param cards Determines if creditCardsDict is to be built
# @param bits Determines if bitCoinAddressesDict is to be built
# @param emails Determines if emailsDict is to be built
# @param websites Determines if websitesDict is to be built
# @param ip Determines if ipAddressesDict is to be built
# @param countries Determines if countriesDict is to be built
# @return extractedSars A list of ExtractedSar Objects
#################################################################### 
def extractFrom(sars, money, banks, cards, bits, emails, websites, ip, countries):

	# Variables
	extractedSars = []
	moneyDict = {}
	banksDict ={}
	creditCardsDict = {}
	bitCoinAddressesDict = {}
	emailsDict = {}
	websitesDict = {}
	ipAddressesDict = {}
	countriesDict = {}
	
	# Extract important data from list of SARs
	for sar in sars:
		bsaID = getattr(sar, "bsaID")
		narrative = getattr(sar, "narrative")
		words = ripWords(narrative)
		if money == 1:
			moneyDict = ripMoney(words)
		if banks == 1:
			banksDict = ripBanks(narrative)
		if cards == 1: 
			creditCardsDict = ripCreditCards(words)
		if bits == 1:
			bitCoinAddressesDict = ripBitCoinAddresses(words)
		if emails == 1:  
			emailsDict = ripEmails(words)
		if websites == 1: 
			websitesDict = ripWebsites(words)
		if ip == 1:
			ipAddressesDict = ripIpAddresses(words) 
		if countries == 1:
			countriesDict = ripCountries(narrative)
	
		# Add object to extractedSars 
		extractedSars.append(ExtractedSar(bsaID, narrative, words, moneyDict, banksDict, \
										  creditCardsDict, bitCoinAddressesDict, \
										  emailsDict, websitesDict, ipAddressesDict, countriesDict))	
	return extractedSars	

#################################################################### 
# ripBanks()- Identify banks found in a narrative, and how many
# times they show up within the narrative.
#
# @param narrative The narrative being searched
# @return banksDict The dictionary of banks paired with number of 
# occurrence per bank.
####################################################################
def ripBanks(narrative):
	banksDict = {}
	
	# Build bank dict 
	banksNames = buildBankDict()	
	
	# Search narrative for bank name
	for key in banksNames:		
		index = 0
		count = 0
		while index < len(narrative):
			index = narrative.lower().find(key.lower(), index)
			if index == -1:
				break
			count += 1 # If found, increment count
			index += len(key) # Increment index by length of word being sought after
		if count > 0:
			banksNames[key] += count
			banksDict[key] = banksNames[key]
	return banksDict

#################################################################### 
# ripBitCoinAddresses()- Identify Bitcoin Addresses found in a 
# narrative, and how many times they show up within the narrative.
#
# @param words The list of words being searched
# @return bitCoinAddressesDict The dictionary of Bitcoin Addresses
# paired with number of occurrence per Bitcoin Address
####################################################################
def ripBitCoinAddresses(words):
	bitCoinAddressesList = []
	bitCoinAddressesDict = {}
	for word in words:
		if (word.startswith('1') == True or word.startswith('3') >= True) and (len(word) > 25 and len(word) < 36) and word.isalnum() \
		and (word.find("0") < 0 and word.find("O") < 0 and word.find("I") < 0 and word.find("l") < 0):
			bitCoinAddressesList.append(word)
			
	# Make dictionary from non duplicate list of IP Addresses
	bitCoinAddressesDict = bitCoinAddressesDict.fromkeys(list(set(bitCoinAddressesList)), 0)
	bitCoinAddressesDict = countOccurrences(bitCoinAddressesDict, bitCoinAddressesList)			
	return bitCoinAddressesDict

#################################################################### 
# ripCountries()- Identify countries found in a narrative, and how 
# many times they show up within the narrative.
#
# @param narrative The narrative being searched
# @return countriesDict The dictionary of countries paired with 
# number of occurrence per country.
####################################################################
def ripCountries(narrative):
	countriesDict = {}
	
	# Build bank dict 
	countryNames = buildCountriesDict()	
	
	# Search narrative for bank name
	for key in countryNames:		
		index = 0
		count = 0
		while index < len(narrative):
			index = narrative.lower().find(key.lower(), index)
			if index == -1:
				break
			count += 1 # If found, increment count
			index += len(key) # increment index by length of word being sought after
		if count > 0:
			countryNames[key] += count
			countriesDict[key] = countryNames[key]
	return countriesDict

#################################################################### 
# ripCreditCards()- Identify credit/debit cards found in a narrative,
# and how many times they show up within the narrative.
#
# @param words The list of words being searched
# @return creditCardsDict The dictionary of cards paired with 
# number of occurrence per card.
####################################################################
def ripCreditCards(words):
	creditCardsList = []
	creditCardsDict = {}
	for word in words:
		if word.isdigit() == True and len(word) == 16:
			creditCardsList.append(word)
	
	# Make dictionary from non duplicate list of emails
	creditCardsDict = creditCardsDict.fromkeys(list(set(creditCardsList)), 0)
	creditCardsDict = countOccurrences(creditCardsDict, creditCardsList)			
	return creditCardsDict
	
#################################################################### 
# ripEmails()- Identify emails found in a narrative,
# and how many times they show up within the narrative.
#
# @param words The list of words being searched
# @return emailsDict The dictionary of emails paired with 
# number of occurrence per email.
####################################################################
def ripEmails(words):
	emailsList = []
	emailsDict = {}
	for word in words:
		if word.find('@') >= 0:
			emailsList.append(word)

	# Make dictionary from non duplicate list of emails
	emailsDict = emailsDict.fromkeys(list(set(emailsList)), 0)
	emailsDict = countOccurrences(emailsDict, emailsList)
	return emailsDict

#################################################################### 
# ripIpAddresses()- Identify IP Addresses found in a narrative,
# and how many times they show up within the narrative.
#
# @param words The list of words being searched
# @return ipAddressesDict The dictionary of IP Addresses paired with 
# number of occurrence per IP.
####################################################################
def ripIpAddresses(words):
	ipAddressesList = []
	ipAddressesDict = {}
	for word in words:
		if word.find('.') >= 0:
			if validateIP(word) == True:
				ipAddressesList.append(word)	
				
	# Make dictionary from non duplicate list of IP Addresses
	ipAddressesDict = ipAddressesDict.fromkeys(list(set(ipAddressesList)), 0)
	ipAddressesDict = countOccurrences(ipAddressesDict, ipAddressesList)			
	return ipAddressesDict

#################################################################### 
# ripMoney()- Identify money values found in a narrative,
# and how many times they show up within the narrative.
#
# @param words The list of words being searched
# @return moneyDict The dictionary of money values paired with 
# number of occurrence per money value
####################################################################
def ripMoney(words):
	moneyList = []
	moneyDict = {}
	for word in words:
		if word.startswith('$') == True:
			moneyList.append(word)
	
	# Strip moneyList of invalid money values

	# Make dictionary from non duplicate list of money
	moneyDict = moneyDict.fromkeys(list(set(moneyList)), 0)
	moneyDict = countOccurrences(moneyDict, moneyList)
	return moneyDict	
	
#################################################################### 
# ripWebsites()- Identify websites found in a narrative,
# and how many times they show up within the narrative.
#
# @param words The list of words being searched
# @return websitesDict The dictionary of websites paired with 
# number of occurrence per website
####################################################################
def ripWebsites(words):
	websitesList = []
	websitesDict = {}
	
	# Build tld list
	tldList = buildTLDList() 
	
	# Create website list
	for word in words:
		for tld in tldList:
			if (word.lower().find(tld.lower().rstrip()) >= 0) and word.find('@') < 0:
				websitesList.append(word)
				break
								
	# Make dictionary from non duplicate list of websites
	websitesDict = websitesDict.fromkeys(list(set(websitesList)), 0)
	websitesDict = countOccurrences(websitesDict, websitesList)			
	return websitesDict

#################################################################### 
# ripWords()- Tokenize the words of a narrative to a list.
#
# @param narrative The narrative being tokenized
# @return words The list of tokenized words
####################################################################
def ripWords(narrative):
	
	# Handle bad input ($ 50.00 should be $50.00) and remove parentheses
#	i = 0
#	while i < len(narrative):
#		if narrative[i] == "$" and narrative[i + 1] == " ":
#			narrative = narrative[:i] + "$" + narrative[i + 2:]
#		if narrative[i] == "(" or narrative[i] == ")":
#			narrative = narrative[:i] + "" + narrative[i + 1:]
#		i += 1

	# Tokenize String
	words = narrative.split( )

	# Remove unnecessary punctuation
	for i, e in enumerate(words):
		
		# Remove from end of word
		if (e[-1] == ',') or (e[-1] == '.') or (e[-1] == ':') or (e[-1] == ';') \
		or (e[-1] == '!') or (e[-1] == '?')  or (e[-1] == '"') or (e[-1] == "'") \
		or (e[-1] == '}') or (e[-1] == '>') or (e[-1] == ')') or (e[-1] == ']'):
			words[i] = words[i][:-1] 
		
		# Remove from beginning of word
		if (e[0] == '{') or (e[0] == '<') or (e[0] == '(') or (e[0] == '[') \
		or (e[0] == '"') or (e[0] == "'"):
			words[i] = words[i][1:] 
			
	# Remove any blank slots in array due to punctuation error
	i = 0
	while i < len(words):
		if words[i] == "":
			del words[i]
		i += 1
		
	return words

#################################################################### 
# validateIP()- Validates if a candidate for an IP Address is valid.
#
# @param ip The candidate for the IP Address being evaluated
# @return A boolean expression depending on if the candidate is a 
#         valid IP
####################################################################
def validateIP(ip):
	a = ip.split('.')
	if len(a) != 4:
		return False
	for x in a:
		if not x.isdigit():
			return False
		i = int(x)
		if i < 0 or i > 255:
			return False
	return True

