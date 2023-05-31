#Programa que assigna el valor nominal d'una nota

nota=int(input('Introdueix el valor de la nota (ha de ser un nombre enter entre 0 i 10): '))
if nota>0 and nota<5 :
    print ('Insuficient')
elif nota<6 :
    print ('Suficient')
elif nota<7 :
    print ('Bé')
elif nota<9 :
    print ('Notable')
else :
    print ('Excel·lent!')
    
    
