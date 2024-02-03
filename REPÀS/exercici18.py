'''
Demanar a l’usuari posar 2 paraules. Afegir aquestes a una tupla i 
mostrar per pantalla quantes vegades apareix cada lletra.
'''

valor1 = input("Introdueix primera paraula >>>")
valor2 = input("Introdueix segona paraula >>>")
count = 0
visto = set()
freq = {}

tupla = (valor1, valor2)
#conseguir la lista de letras unicas
for i in tupla:
    for j in i:
        if j not in visto:
            visto.add(j)
            count += 1

#convertir en string
str = ''.join(tupla)

#contar frequencia de cada letra
for i in visto:
    freq[i] = str.count(i)

print("Freqüència de cada lletra:")
for i in visto:
    print(f"Lletra: {i}  Vegades: {freq[i]}")