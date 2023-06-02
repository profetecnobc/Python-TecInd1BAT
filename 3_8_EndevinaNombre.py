#Programa que encerta un nombre de l'1 al 10
import random
print ('Intenta encertar amb el mínim d\'intents un nombre de l\'1 al 10')
nombreSecret = random.randint(1, 10)
nombreJugador = 0
intents = 0
while nombreJugador != nombreSecret :
    nombreJugador=int(input('Encerta el nombre: '))
    intents = intents + 1
print ('L\'has encertat amb ',intents,' intents')

