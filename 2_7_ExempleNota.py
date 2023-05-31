#Programa calcula una nota a partir d'unes premises

e1=int(input('Introdueix el valor de la primera nota: '))
e2=int(input('Introdueix el valor de la segona nota: '))
e3=int(input('Introdueix el valor de la tercera nota: '))
if e1<4 and e2<4 and e3<4 :
    print ('La nota final és 0')
elif e1<4 or e2<4 or e3<4 :
    print ('La nota final és 2')
else :
    nota=e1*0.3+e2*0.2+e3*0.5
    print ('La nota final és ',nota)
    
    
