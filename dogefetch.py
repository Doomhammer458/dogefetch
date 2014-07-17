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
class bter_API():
    def __init__(self):
        import requests
        url = 'http://data.bter.com/api/1/pairs/'
	r = requests.get(url).json()
        self.trading_pairs = r
        
        
    def get_price(self,cur_a,cur_b):
        """
        returns the current exhange rate between currency A and Currency B
        """
        cur_a = cur_a.lower()
        cur_b = cur_b.lower()
        pair = cur_a+"_"+cur_b 
        if pair not in self.trading_pairs:
            pair = cur_b+"_"+cur_a
            
            
            if pair not in self.trading_pairs:
                raise Exception("trading pair not found")
            else:
                url = 'http://data.bter.com/api/1/ticker/'+pair
                r = requests.get(url).json()
                if r["result"]=="true":
                    return r["avg"]**-1
                else:
                    raise Exception("Can not connect to API")
            
        else:
            url = 'http://data.bter.com/api/1/ticker/'+pair
            r = requests.get(url).json()
            if r["result"]=="true":
                return r["avg"]
            else:
                raise Exception("Can not connect to API")
        
"""        
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
"""
x = bter_API()

# Return dogecoin value:
# print doge_usd()
#
# Return lightcoin value:
# print ltc_usd()
#
# Return bitcoin value:
# print btc_usd()
