#Programa que mostra les taules de multiplicar
nombres=int(input('Quants nombres vols entrar?: '))
negatius=0
for i in range (nombres) :
    nouNombre=int(input('Entra un nombre: '))
    if nouNombre<0 :
        negatius=negatius+1
print ('Has entrat ',negatius,' nombres negatius')
