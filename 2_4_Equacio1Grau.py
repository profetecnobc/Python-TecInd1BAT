#Programa que resol equacions de primer grau
print ('Anem a resoldre una equació del tipus ax+b=0')
a=int(input('Introdueix el valor d\'a: '))
b=int(input('Introdueix el valor de b: '))
if a!=0 :
    print ('La solució és',-b/a)
elif b!=0 :
    print ('Solució impossible')
else :
    print ('Solució indeterminada')

