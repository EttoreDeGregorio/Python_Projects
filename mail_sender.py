#Script che permette di madare email da un account GMAIL
#email formate sono da testo

import smtplib

#Dati di Log-In
gmail_user = ''#La tua mail
gmail_password = ''#La tua password


#Dati dell'email
sent_from = gmail_user

print '\nReciver: '
x = raw_input()
to = [x]

print '\nSubject: '
subject = raw_input()

print '\nBody: '
body = raw_input()

email_text = """\
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)


#Connesione al server
try:
	server = smtplib.SMTP('smtp.gmail.com')
	server.ehlo()
	server.starttls()
	print '\n\nConnected'

	server.login(gmail_user, gmail_password)
	print '\nLogged In'

	server.sendmail(sent_from, to, email_text)
	server.close()
	print '\nMail sent\n\n'

except:
	print '\nError\n\n'