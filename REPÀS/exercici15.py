'''
El mateix que l’anterior exercici, però sense demanar un màxim de números. 
L’usuari indicarà quan ha acabat posant un 0.

'''
lista = set()

while True:
    valor = int(input("Ves introduïnt número (0 per finalitzar)>>> "))
    
    if valor == 0:
        break
    else:
        lista.add(valor)
        
# convertir en lista, ordenar y volver a convertir en tupla
print("Tupla:", tuple(sorted(list(lista))))