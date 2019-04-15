#!usr/bin/env python

import webbrowser	#to open browser
import osascript 	#to run applescripts
import time			#sleep
import sys			#loading
import urllib2		#check connection

#Main
def Main():
	print "\n=== GOOD MORNING  ===\n"
	time.sleep(1)

	print "--- VOLUME LOWERING ---\n"

	loading()

	volume = 0
	
	osascript.osascript("set volume output volume %d" %volume)
	print "\n\nVolume lowerd succesfully"

	if check_connection() == True:
		#url Registro elettronico
		url = "https://registroelettronico.nettunopa.it/ulogin.php"
		count = 5

		#open browser and webpage
		print "\n\n--- OPENING BROSER ---\n"
		
		loading()

		print "\n\n"
		time.sleep(2)
		webbrowser.open_new(url)

	elif check_connection() == False:
		print "\n\nNo Connection"

#Loading bar
def loading():
	toolbar_width = 50
	sys.stdout.write("[%s]" % (" " * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1))

	for i in xrange(toolbar_width):
		time.sleep(0.1)
		sys.stdout.write("-")
		sys.stdout.flush()

#Connection check
def check_connection():
	try:
		urllib2.urlopen('https://google.com', timeout=1)
		return True

	except urllib2.URLError as err: 
		return False


if __name__ == '__main__':
	Main()