'''
Demanar a l’usuari un número de l’1 al 10 
i mostrar per pantalla la seva taula de multiplicar fins el 10. 
Exemple: l’usuari marca 3, es mostra per pantalla: 3,6,9,12,15,18,21,24,27 i 30
'''
x = int(input("Introdueix un numero entre 1 i 10 >>> "))
tupla = set() #tupla vacía

if 1 <= x <= 10:
    for i in range(1, 11):
        resultado = x * i
        tupla.add(resultado)
        
    # convertir en lista, ordenar y volver a convertir en tupla
    print(tuple(sorted(list(tupla))))
else:
    print("Fora de rang aceptat")