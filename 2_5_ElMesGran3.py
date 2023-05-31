#Programa que determina el més gran de tres nombres
print ('Entra 3 nombres i determinarem quin és el més gran:')
a=int(input('Introdueix el valor del primer nombre: '))
b=int(input('Introdueix el valor del segon nombre: '))
c=int(input('Introdueix el valor del darrer nombre: '))
if a>b and a>c :
    print ('El més gran és ',a)
elif b>c :
    print ('El més gran és ',b)
else :
    print ('El més gran és ',c)
    
    
