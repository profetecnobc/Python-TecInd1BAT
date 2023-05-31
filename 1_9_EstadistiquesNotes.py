#Programa que fa l'estadística de les notes
print ('Entra el nombre de cada una de les notes')
suspesos=int(input('Nombre d\'alumnes suspesos: '))
suficient=int(input('Nombre d\'alumnes amb suficient: '))
be=int(input('Nombre d\'alumnes amb bé: '))
notable=int(input('Nombre d\'alumnes amb notable: '))
execelent=int(input('Nombre d\'alumnes amb excel·lent: '))
total=suspesos+suficient+be+notable+execelent
peraprovats=((total-suspesos)/total)*100
persuspesos=(suspesos/total)*100
persuficient=(suficient/total)*100
perbe=(be/total)*100
pernotable=(notable/total)*100
perexcelent=(execelent/total)*100
print('El percentatge d\'alumnes aprovats és %.2f'%(peraprovats))
print('Suspesos  %.2f'%(persuspesos))
print('Suficient  %.2f'%(persuficient))
print('Bé  %.2f'%(perbe))
print('Notable  %.2f'%(pernotable))
print('Excel·lent  %.2f'%(perexcelent))



