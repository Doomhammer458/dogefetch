import requests

class bter_API():
    def __init__(self):
        url = 'http://data.bter.com/api/1/pairs/'
	r = requests.get(url).json()
        self.trading_pairs = r
        
        
    def get_price(self,cur_a,cur_b,price_type="avg"):
        """
        returns the current exhange rate between currency A and Currency B
        optional price_type parm can be avg, low, high, buy, sell
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
                    return float(r[price_type])**-1
                else:
                    raise Exception("Can not connect to API")
            
        else:
            url = 'http://data.bter.com/api/1/ticker/'+pair
            r = requests.get(url).json()

            if r["result"]=="true":
                return float(r["price_type"])
            else:
                raise Exception("Can not connect to API")
x = bter_API()