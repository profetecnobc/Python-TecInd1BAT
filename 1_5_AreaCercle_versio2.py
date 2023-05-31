#Programa que calcula l'àrea d'un cercle a partir del radi
from math import pi #importem el valor de pi de la llibreria math
print('Anem a calcular l\'àrea d un cercle')
radi=int(input('Quin és el valor del radi del cercle en centímetres?: '))
area=pi*radi**2
print ('L\'àrea d aquest cerccle val %.2f '%(area))
