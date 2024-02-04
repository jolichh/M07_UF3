'''
Demanar a l’usuari que introdueixi 10 números separats per un espai. 
Al acabar, el programa els introduirà en una tupla 
i els ordenarà (major o menor, com volgueu), 
mostrant per pantalla el contingut de la tupla.
'''
valor = input("Introdueix 10 números separats per un espai >>> ")

if valor == 10:
    # dividir y guardar en lista en forma de enteros
    lista = [int(x) for x in valor.split()]

    # convertir en lista, ordenar y volver a convertir en tupla
    print("Tupla:", tuple(sorted(list(lista))))
else:
    print("Has d'introduir  10 números!")