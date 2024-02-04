'''
Demanar a l’usuari que posi 10 números separats per espais. 
Afegir aquests números a una llista. 
Calcular la suma de tots els números i la seva mitjana i 
afegir aquests 2 números a la llista. 
Mostrar per pantalla la llista.
'''
valor = input("Introdueix 10 numeros separats per espais >>> ")
tmp = [float(i) for i in valor.split()]
lista = []
#calcular total i la mitjana
total = sum(tmp)
mitja = total/len(tmp)
print(total)
lista.extend([total, mitja])

print("Numeros de l'usuari:", tmp, "\nSuma total:", lista[0], "\nMitjana:", lista[1])