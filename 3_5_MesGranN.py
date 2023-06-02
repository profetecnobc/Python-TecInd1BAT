#Programa que determina el nombre més gran de N nombres
n=int(input('Quants nombres vols entrar?'))
ElMesGran=0
i=1
while i<=n :
    nombre=int(input('Entra un nombre: '))
    if nombre > ElMesGran :
        ElMesGran = nombre
    i=i+1
print('El més gran és ',ElMesGran)
    
