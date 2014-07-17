#!/usr/bin/python

# Wow such python
# Feel free to modify
# So generous: DGSWzqyofHC6YDSA34hwVQpWGQHnzJm1sk
#
# Remember to make this file executable ( "$chmod +x ./dogefetch1" )
#
# To add other coins, use the template below, and modify the while
# loop accordingly.
#
###########################################################
#
# def <function name>():
#	url = '<http://data.bter.com/api/1/ticker/*>'
#	r = requests.get(url)
#	out = r.json()['avg']
#	return out
#
#############################################################

import requests

def doge_usd():
	"""
	Fetch USD - DOGE
	"""
	url = 'http://data.bter.com/api/1/ticker/doge_usd'
	r = requests.get(url)
	out = r.json()['avg']
	return out
	
def btc_usd():
	"""
	Fetch USD - BTC
	"""
	url = 'http://data.bter.com/api/1/ticker/btc_usd'
	r = requests.get(url)
	out = r.json()['avg']
	return out

def ltc_usd():
	"""
	Fetch LTC - USD
	"""
	url = 'http://data.bter.com/api/1/ticker/ltc_usd'
	r = requests.get(url)
	out = r.json()['avg']
	return out

        
     
while True:
	coin = raw_input("DOGE-USD [wow], LTC-USD [l], BTC-USD [b]? ")
	if coin == "wow":
		print "1 DOGE = $" + str(doge_usd())
		break
	elif coin == "l":
		print "1 LTC = $" + str(ltc_usd())
		break
	elif coin == "b":
		print "1 BTC = $" + str(btc_usd())
		break
	print "Invalid input (this is case sensitive!)"
	


# Return dogecoin value:
# print doge_usd()
#
# Return lightcoin value:
# print ltc_usd()
#
# Return bitcoin value:
# print btc_usd()
