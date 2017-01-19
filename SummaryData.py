#################################################################### 
# buildSummaryDict()- Builds a dictionary of summary data. Takes all
# of the dictionaries per field and totals the values up so that one
# summary dictionary can be returned.
#
# @param summaryDict The dictionary to be returned with the summary 
# values
# @param dict The dictionary being added to the summaryDict
# @return summaryDict The dictionary containing summary values 
####################################################################
def buildSummaryDict(summaryDict, dict):
	for key in dict:
		
		# If key is in summary dict add value to existing value...else add new key/value
		if key in summaryDict:
			summaryDict[key] += dict[key]
		else:
			summaryDict[key] = dict[key]

#######################################################################################
# get()- Gets the appropriate summary information based on what the 
# user wants. 
#
# @param extractedSars The extracted SAR data to make summary data from
# @param moneySummary The summary money dictionary to be updated
# @param banksSummary The summary banks dictionary to be updated
# @param cardsSummary The summary cards dictionary to be updated
# @param bitCoinsSummary The summary bit coin address dictionary to be updated
# @param emailsSummary The summary emails dictionary to be updated
# @param websitesSummary The summary websites dictionary to be updated
# @param ipSummary The summary IP addresses dictionary to be updated
# @param countriesSummary The summary countries dictionary to be updated
# @param moneyChecked Check box for money. 1 if selected...0 if not
# @param banksChecked Check box for banks. 1 if selected...0 if not
# @param cardsChecked Check box for cards. 1 if selected...0 if not
# @param bitsChecked Check box for bitcoin addresses. 1 if selected...0 if not
# @param emailsChecked Check box for emails. 1 if selected...0 if not
# @param websitesChecked Check box for websites. 1 if selected...0 if not
# @param ipChecked Check box for IP addresses. 1 if selected...0 if not
# @param countriesChecked Check box for countries. 1 if selected...0 if not
#######################################################################################
def get(extractedSars, moneySummary, banksSummary, cardsSummary, bitCoinsSummary, \
		emailsSummary, websitesSummary, ipSummary, countriesSummary, moneyChecked, \
		banksChecked, cardsChecked, bitsChecked, emailsChecked, websitesChecked, \
		ipChecked, countriesChecked):
		
	# Sift through extracted sars
	for sar in extractedSars:

		# Determine which dicts to build
		if moneyChecked == True:
			buildSummaryDict(moneySummary, getattr(sar, "moneyDict"))			
		if banksChecked == True:
			buildSummaryDict(banksSummary, getattr(sar, "banksDict"))		
		if cardsChecked == True:
			buildSummaryDict(cardsSummary, getattr(sar, "creditCardsDict"))			
		if bitsChecked == True:
			buildSummaryDict(bitCoinsSummary, getattr(sar, "bitCoinAddressesDict"))		
		if emailsChecked == True:
			buildSummaryDict(emailsSummary, getattr(sar, "emailsDict"))		
		if websitesChecked == True:
			buildSummaryDict(websitesSummary, getattr(sar, "websitesDict"))		
		if ipChecked == True:
			buildSummaryDict(ipSummary, getattr(sar, "ipAddressesDict"))		
		if countriesChecked == True:
			buildSummaryDict(countriesSummary, getattr(sar, "countriesDict"))	