import sys
#import requests



# the function for the buying information
def getbuyinformation():
# # open the file called cryptobuy if not exist create one
	f = open("cryptobuy.txt", "a")
	crypto = input("Which Cryptocurrency is being purchased? \n")
<<<<<<< HEAD
	#print("\n")
	cryptoamount = input("How Much " + crypto + " did you purchase? \n")
	#print("\n")
	usdamount = input("How much USD did the " + cryptoamount + "  " + crypto + " cost you in this buy? \n")
	#print("\n")
	exchangerate = input("How much USD is 1.0 " + crypto + " currently? \n")
	#print("\n")
	notes = input("Any notes on why you are making this buy of " + cryptoamount + " " + crypto + " today? REMEMBER: Don't invest more than you're willing to lose. Never feel guilty, if you feel like you have a problem there is plenty of help out there . Everyone has experiences with loss. Someone spent 10,000 BTC on a pizza when the exchange rate was low. Everything will be ok no matter how the market treats you :) \n")
	#print("\n")
=======
	cryptoamount = input("How Much " + crypto + " did you purchase?\n ")
	usdamount = input("How much USD did the " + cryptoamount + "  " + crypto + " cost you in this buy?\n ")
	exchangerate = input("How much USD is 1.0 " + crypto + " currently? \n")
	notes = input("Any notes on why you are making this buy of " + cryptoamount + " " + crypto + " today? REMEMBER: Don't invest more than you're willing to lose. Never feel guilty, if you feel like you have a problem there is plenty of help out there . Everyone has experiences with loss. Someone spent 10,000 BTC on a pizza when the exchange rate was low. Everything will be ok no matter how the market treats you :)\n")
#write to the file what is recording from the user input and format it
>>>>>>> origin/main
	f.write("Bought " + cryptoamount + " " + crypto + "\n")
	f.write("The purchase of " + cryptoamount + " " + crypto + " cost " + usdamount  + " USD." + "\n")
	f.write("The Exchange rate at the time of this sale was 1.0 " + crypto + "=" + exchangerate + " USD." + "\n")
	f.write("Notes: " + notes + "\n" + "\n" + "NEW BUY RECORD" + "\n" + "\n")
	f.close()

# the function for the selling information
def getsellinformation():

	f = open("cryptosell.txt", "a")
<<<<<<< HEAD
	
	
	crypto = input("Which Cryptocurrency is being sold? \n")
	
	cryptoamount = input("How Much " + crypto + " are you selling? \n")
	#print("\n")
	usdamount = input("How much USD did you receive from selling your " + cryptoamount + " " + crypto + " " + " in this sell order? \n")
	#print("\n")
	exchangerate = input("How much USD is 1.0 " + crypto + " currently? \n")
	#print("\n")
	notes = input("Any notes on why you are selling " + cryptoamount + "of your " + crypto + " today? REMEMBER: Hold if you can, but if you need the money, it's ok :) \n")
	#print("\n")
=======
# open the file called cryptosell if not exist create one
	crypto = input("Which Cryptocurrency is being sold? \n")
	cryptoamount = input("How Much " + crypto + " are you selling?\n")
	usdamount = input("How much USD did you receive from selling your " + cryptoamount + " " + crypto + " " + " in this sell order? \n ")
	exchangerate = input("How much USD is 1.0 " + crypto + " currently? \n")
	notes = input("Any notes on why you are selling " + cryptoamount + "of your " + crypto + " today? REMEMBER: Hold if you can, but if you need the money, it's ok :) \n")
>>>>>>> origin/main
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
    	buyorsell = input("Is this a record of a buy or a sell order? Type 'q' to quit. \n")
    	if buyorsell == "buy":
    		getbuyinformation()
    	elif buyorsell == "sell":
    		getsellinformation()
    	elif buyorsell == "q":
    		break
    	else:
    		print("Only 'buy' or 'sell' orders are are accepted, along with the quit command 'q'. please enter one of the three. \n")
