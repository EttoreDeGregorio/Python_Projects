#Script che stampa il meteo in base alla location

from weather import Weather, Unit 		#weather-api
import subprocess as sp 				#per comandi di sistema

sp.call('clear',shell=True)

weather = Weather(unit = Unit.CELSIUS)

location = weather.lookup_by_location('milan')
condition = location.condition

print(condition.text)

aspetta = raw_input()
sp.call('clear',shell=True)