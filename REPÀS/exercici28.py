'''
Crear una funció que passats dos números per paràmetre (demanats a l’usuari) 
ens mostri per pantalla un número aleatori entre aquests dos números.
'''
import random
from math import floor
def randomNums():
    # Solicitar numeros
    numero1 = int(input("Introdueix primer num >>> "))
    numero2 = int(input("Introdueix segon num >>> "))

    # Generar numero aleatorio entre los rangos dados (entero)
    aleatorio = random.uniform(min(numero1, numero2), max(numero1, numero2))
    print(f"Número aleatorio entre {numero1} y {numero2}: {floor(aleatorio)}")

# Llamar a la función
randomNums()
