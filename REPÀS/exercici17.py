'''
Igual que l’anterior però a la tupla afegir la frase sense els caràcters repetits i mostrar el contingut de la tupla. 
Exemple: Usuari indica la paula caracteristica. 
Es mostra per pantalla carteis.
'''

valor = input("Escriu una frase >>> ")
tupla = tuple(valor.split())
usados = set()

for i in range(0, len(tupla)):
    '''
    resultado = [] # guardar en orden original cara letra
    for j in range(0, len(tupla[i])):
        #comprovar que no se repite
        if j not in usados:
            #agregar a la lista
            resultado.append(tupla[i][j])
            usados.add(j)
    
    # une los caaracteres
    tupla[i] = ''.join(resultado)
    '''
    new_tupla = tuple(set(tupla[i], key=tupla[i].index))
print(new_tupla)