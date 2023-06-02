#Programa que descomposa factorialment un nombre
nombre=int(input('Quin nombre vols consultar? '))
print ('Descomposició factorial: 1 ', end=' ')
primer=1
divisor=2
while divisor<nombre :
    if nombre%divisor==0 :
        print (divisor, end=" ")
        primer = 0
    divisor=divisor+1
if primer == 1 :
    print (nombre)
