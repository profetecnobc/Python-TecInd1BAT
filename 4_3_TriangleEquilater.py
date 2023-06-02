#Programa que dibuixa un triangle d'estrelles
n= int(input('Quina és l\'alçada del triangle(enter positiu)?:'))
for i in range (n) :
    for j in range (i+1) :
        print ('*', end='')
    print('')
for i in range (n) :
    for j in range (n-i-1) :
        print ('*', end='')
    print('')
