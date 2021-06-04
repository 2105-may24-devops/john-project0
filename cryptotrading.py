import sys
#import requests




def getbuyinformation():
	f = open("cryptobuy.txt", "a")
	crypto = input("Which Cryptocurrency is being purchased? ")
	print("\n")
	cryptoamount = input("How Much " + crypto + " did you purchase? ")
	print("\n")
	usdamount = input("How much USD did the " + cryptoamount + "  " + crypto + " cost you in this buy? ")
	print("\n")
	exchangerate = input("How much USD is 1.0 " + crypto + " currently? ")
	print("\n")
	notes = input("Any notes on why you are making this buy of " + cryptoamount + " " + crypto + " today? REMEMBER: Don't invest more than you're willing to lose. Never feel guilty, if you feel like you have a problem there is plenty of help out there . Everyone has experiences with loss. Someone spent 10,000 BTC on a pizza when the exchange rate was low. Everything will be ok no matter how the market treats you :)")
	print("\n")
	f.write("Bought " + cryptoamount + " " + crypto + "\n")
	f.write("The purchase of " + cryptoamount + " " + crypto + " cost " + usdamount  + " USD." + "\n")
	f.write("The Exchange rate at the time of this sale was 1.0 " + crypto + "=" + exchangerate + " USD." + "\n")
	f.write("Notes: " + notes + "\n" + "\n" + "NEW BUY RECORD" + "\n" + "\n")
	f.close()


def getsellinformation():
	f = open("cryptosell.txt", "a")
	
	
	crypto = input("Which Cryptocurrency is being sold? ")
	print("\n")
	cryptoamount = input("How Much " + crypto + " are you selling?")
	print("\n")
	usdamount = input("How much USD did you receive from selling your " + cryptoamount + " " + crypto + " " + " in this sell order? ")
	print("\n")
	exchangerate = input("How much USD is 1.0 " + crypto + " currently? ")
	print("\n")
	notes = input("Any notes on why you are selling " + cryptoamount + "of your " + crypto + " today? REMEMBER: Hold if you can, but if you need the money, it's ok :) ")
	print("\n")
	f.write("Sold " + cryptoamount + " " + crypto + "\n")
	f.write("The sale of " + cryptoamount + " " + crypto + " netted " + usdamount  + " USD." + "\n")
	f.write("The Exchange rate at the time of this sale was 1.0 " + crypto + "=" + exchangerate + " USD." + "\n")
	f.write("Notes: " + notes + "\n" + "\n" + "NEW SELL RECORD" + "\n" + "\n")
	f.close()






if __name__ == "__main__":
    
    #response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    #data = response.json()
    #print(data["bpi"]["USD"]["rate"])
    while(True):
    	buyorsell = input("Is this a record of a buy or a sell order? Type 'q' to quit. ")
    	if buyorsell == "buy":
    		getbuyinformation()
    	elif buyorsell == "sell":
    		getsellinformation()
    	elif buyorsell == "q":
    		break
    	else:
    		print("Only 'buy' or 'sell' orders are are accepted, along with the quit command 'q'. please enter one of the three.")
