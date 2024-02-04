# Demanar a l’usuari un nùmero entre 10 i 100. 
# Posar els números a una tupla desde 1 fins al número indicat per l’usuari. 
# Exemple: usuari indica 34, es crea una tupla i es mostra per pantalla els números de l’1 al 34 (imprimint la tupla).

valor = int(input("Introdueix un valor entre 10 i 100 >>> "))

# funció que crea la tupla del tamany que li passi
def crea_tupla(valor):
    tupla = tuple(range(1, valor +1))
    return tupla

x = crea_tupla(valor)

print("Tupla:",x)