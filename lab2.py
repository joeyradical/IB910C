#!/usr/bin/env python
# -*- coding: utf-8 -*-
#IB910C -S VT2016 Laboration 2:
#Written in Python 2.7.9 using Mac OSX 10.3

import random
import sys

#Skriver ut introduktionstext
def intro():
	print 'Välkommen till spelet "Gissa mitt tal"!'
	print 'Du ska gissa på det tal jag tänker på, vilket är ett heltal mellan 1-100'
	print 'Lycka till'
	
#Låter användaren mata in ett tal	
def gissa():
	indata = int(raw_input('Vilket tal gissar du på? \t\t'))
	if indata < 1 or indata >100:
		print "Varning: det tal du matade in var ej i det givna intervallet. Gissa mellan 1-100 nästa gång förslagsvis"
	return indata
	
	
def main():
	try:
		intro()
		#Genererar talet som användaren ska gissa på
		ratt_svar = random.randint(1,100);
		gissning = gissa()
		antal_gissningar = 1;
		#Användaren måste gissa om och om igen tills han eller hon har gissat på rätt tal.
		while gissning != ratt_svar:
			if gissning > ratt_svar:
				print 'Fel! Gissa på ett lägre tal' 
			elif gissning < ratt_svar:
				print 'Fel! Gissa på ett högre tal'
			antal_gissningar += 1
			gissning = gissa()
			
	except ValueError:
		print "Du matade inte in ett heltal när du gissade. Avslutar programmet."
		sys.exit(-1)

	#Skriv ut vinstmeddelande	
	print "Rätt! Det rätta svaret var " + str(ratt_svar) + " och det tog dig " + str(antal_gissningar) + " försök att komma fram till det. Bra jobbat!"
	
	
if __name__ == "__main__":
    main()