#!usr/bin/env python

#Script che stampa le previsioni di fino a 10 giorni in base alla location

from weather import Weather, Unit #weather-api
import subprocess as sp #per comandi di sistema

sp.call('clear', shell = True)

weather = Weather(unit = Unit.CELSIUS)

luogo = weather.lookup_by_location('milan')#cmabiare in base alla città
previsioni = luogo.forecast

risp = " " 

for forecast in previsioni:
	print "\n--------\n"

	print "Data: ", forecast.date
	print "Condizioni: ", forecast.text
	print "\n- Temperature -"
	print "MAX:", forecast.high, "C ---  MIN:", forecast.low, "C"

	print "\n--------\n"

	print"\n\n\n\n Voui vedere le previsioni del giono seguente? (y/n)"
	risp = raw_input()

	if risp == "n" or risp == "N":
		break

	else:
		sp.call('clear', shell = True)

print "Premi INVIO per uscire..."
aspetta = raw_input()
sp.call('clear', shell = True)