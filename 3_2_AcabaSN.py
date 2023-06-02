#Acabar en S o N
paraula=input("Entra una paraula")
acabar=True
while acabar==True:
    if paraula=="s" or paraula=="n":
        print ("perfecte")
        acabar=False
    else:
        print("Torna a entrar una paraula")
        paraula=input()
        acabar=True
