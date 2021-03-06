#!/usr/bin/env bash



   main () {

   	cat testin.txt | ./venv/bin/python3 -m cryptotrading test

   	if cmp cryptobuy.txt expected_buy.txt; then
   		echo "Outputted cryptobuy.txt matches expected_buy.txt, the correct outputs for this list of inputs."

   	else
   		echo "Mismatch in expected cryptobuy.txt output."

   	fi

   	if cmp cryptosell.txt expected_sell.txt; then
   		echo "Outputted cryptosell.txt matches expected_sell.txt, the correct outputs for this list of inputs."

   	else
   		echo "Mismatch in expected cryptosell.txt output."
   	fi


}


main "$@"