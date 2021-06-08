import sys
import time
#import requests



# Function called for buying cryptocurrency and logging the sale
def getbuyinformation(curtime):
	#If this is the first recorded buy, create a log file for buy orders. If the program has been used to record buys before, add another entry to this file. It is opened here.
	f = open("cryptobuy.txt", "a")
	crypto = input("Which Cryptocurrency is being purchased? \n")

	
	cryptoamount = input("How Much " + crypto + " did you purchase? \n")
	
	usdamount = input("How much USD did the " + cryptoamount + " " + crypto + " cost you in this buy? \n")
	
	exchangerate = input("How much USD is 1.0 " + crypto + " currently? \n")
	
	notes = input("Any notes on why you are making this buy of " + cryptoamount + " " + crypto + " today?  \n")
	#REMEMBER: Don't invest more than you're willing to lose. Never feel guilty, if you feel like you have a problem there is plenty of help out there . Everyone has experiences with loss. Someone spent 10,000 BTC on a pizza when the exchange rate was low. Everything will be ok no matter how the market treats you :)
	



	#Write to cryptobuy.txt with the information of the buy
	f.write("NEW BUY RECORD" + "\n" + "\n")
	f.write(time.strftime('%H:%M%p %Z on %b %d %Y'))
	f.write("\n")
	f.write("Bought " + cryptoamount + " " + crypto + "\n")
	f.write("The purchase of " + cryptoamount + " " + crypto + " cost " + usdamount  + " USD." + "\n")
	f.write("The Exchange rate at the time of this sale was 1.0 " + crypto + "=" + exchangerate + " USD." + "\n")
	f.write("Notes: " + notes +"\n" + "\n")
	f.close()

# Function called for selling cryptocurrency and logging the sale
def getsellinformation(curtime):
	#Create a log file for sales if it doesn't exist, or open it and continue writing for it if the program has previously been ran for a sell order
	f = open("cryptosell.txt", "a")

	
	
	crypto = input("Which Cryptocurrency is being sold? \n")
	
	cryptoamount = input("How Much " + crypto + " did you sell? \n")
	
	usdamount = input("How much USD did you receive from selling your " + cryptoamount + " " + crypto + " " + " in this sell order? \n")
	
	exchangerate = input("How much USD is 1.0 " + crypto + " currently? \n")
	
	notes = input("Any notes on why you are selling " + cryptoamount + " of your " + crypto + " today? \n")
	#REMEMBER: Hold if you can, but if you need the money, it's ok :)
	



	#Write to cryptosell.txt with information of this sell order
	f.write("NEW SELL RECORD" + "\n" + "\n")
	f.write(time.strftime('%H:%M%p %Z on %b %d %Y'))
	f.write("\n")
	f.write("Sold " + cryptoamount + " " + crypto + "\n")
	f.write("The sale of " + cryptoamount + " " + crypto + " netted " + usdamount  + " USD." + "\n")
	f.write("The Exchange rate at the time of this sale was 1.0 " + crypto + "=" + exchangerate + " USD." + "\n")
	f.write("Notes: " + notes+"\n" + "\n")
	f.close()


if __name__ == "__main__":
    
    #response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    #data = response.json()
    #print(data["bpi"]["USD"]["rate"])
    while(True):
    	#getting time to use in functions and log file
    	curtime = time.ctime()
    	#log file for last time application was run
    	f = open("logfile.txt", "a")
    	f.write("Application Run at " + time.strftime('%H:%M%p %Z on %b %d %Y') + "\n" + "\n")
    	f.close()
    	buyorsell = input("Is this a record of a buy or a sell order? Type 'q' to quit. \n")
    	if buyorsell == "buy":
    		getbuyinformation(curtime)
    		continue
    	elif buyorsell == "sell":
    		getsellinformation(curtime)
    		continue
    	elif buyorsell == "q":
    		break
    	else:
    		print("Only 'buy' or 'sell' orders are are accepted, along with the quit command 'q'. please enter one of the three. \n")
