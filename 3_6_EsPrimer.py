#Programa que determina si un nombre és primer
nombre=int(input('Quin nombre vols consultar? '))
primer = 1
divisor=2
while divisor<nombre :
    if nombre%divisor==0 :
        primer=0
    divisor=divisor+1
if primer == 1 :
    print('És primer')
else :
    print ('No és primer')
    
