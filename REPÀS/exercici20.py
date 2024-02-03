'''
Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat. 
S’haura de demanar a l’usuari que posi contactes (noms i edats). Si algun nom es repeteix no s’fageirà al diccionari (indicant-ho a l’usuari). 
Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més
'''
myDict = {}

while True:
    print("Per sortir escriviu 'surt'")
    nom = input("Introdueix nom:")
    if nom.lower() == 'surt':
        break

    edat = input("Introdueix edat:")
    #mirar si ja existeix
    if nom in myDict:
        print("Aquest contacte ja existeix...")
    else:
        myDict[nom] = int(edat)

print("Diccionari:",myDict)