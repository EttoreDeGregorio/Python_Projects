import random

#Apertura file
lista = open("lista.txt", "w" )

try:
    for i in range(int(input('How many random numbers?: '))):
        line = str(random.randint(1, 100))
        lista.write(line)
        lista.write(' ')
        print(line)
        
except ValueError:
    print 'Error'


lista.close()