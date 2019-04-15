#!usr/bin/env python

import random

#Apertura file
lista = open("list.txt", "w" ) # "w" sta per WRITE

try:
    for i in range(int(input('How many random numbers?: '))):
        line = str(random.randint(1, 100))
        lista.write(line)
        lista.write(' ')
        print(line)
        
except ValueError:
    print 'Error'

lista.close()