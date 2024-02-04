'''
Demanar a l’usuari una frase. 
El programa eliminarà els espais i s'afegirà a una tupla. 
Mostrar per pantalla el contingut de la tupla.
'''
valor = input("Escriu una frase >>> ")
tupla = tuple(valor.split())

print(tupla)