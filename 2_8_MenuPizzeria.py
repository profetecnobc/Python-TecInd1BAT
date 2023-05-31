#Programa selecciona el menú d'una pizzeria
print('Benvingut a la Pizzeria Bella Roma')
print('Tipus de pizza:\n  1-Vegetariana \n  2-No Vegetariana')
tipusPizza=int(input('Introdueix el número de pizza que desitges: '))
if tipusPizza==1 :
    pizza='vegetariana'
    print('Ingredients de pizzes vegetarianes:\n  1-Pebrot \n  2-Tofu')
elif tipusPizza==2:
    pizza='no vegetariana'
    print ('Ingredients de pizzes vegetarianes:\n  1-Peperoni \n  2-Pernil \  3-Salmó')
ingredient=int(input('Introdueix l\'ingredient que desitges: '))
if tipusPizza==1 and ingredient==1 :
    seleccio='pebrot'
elif tipusPizza==1 and ingredient==2 :
    seleccio='tofu'
elif ingredient==1 :
    seleccio='peperoni'
elif ingredient==2 :
    seleccio='pernil'
else :
    seleccio='salmó'
print('Heu escollit pizza '+pizza+' amb mozzarella, tomàquet i '+seleccio)
    
    

