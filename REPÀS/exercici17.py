'''
Igual que l’anterior però a la tupla afegir la frase sense els caràcters repetits i mostrar el contingut de la tupla. 
Exemple: Usuari indica la paula caracteristica. 
Es mostra per pantalla carteis.
'''

valor = input("Escriu una frase >>> ")
unics = []
usats = set()

for i in valor:
    #para que respete espacios entre palabras
    if i == ' ' or i not in usats:
        usats.add(i)
        unics.append(i)

tupla = tuple(unics)
#convertir tupla en string
str = ''.join(tupla)
##convertir string en tupla separada por palabras (espacios)
new_tup = tuple(str.split())
print(new_tup)