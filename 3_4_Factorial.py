#Programa que calcula el factorial d'un nombre
nombre=int(input('Entra el nombre del que vols calcular el factorial:'))
multiple=1
factorial=1
while multiple <= nombre :
    factorial=factorial*multiple
    multiple=multiple+1
print('El factorial de ',nombre,' és ',factorial)
    
