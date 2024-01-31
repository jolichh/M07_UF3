'''
Crear una tupla amb els mesos de l’any. 
Demanar a l’usuari que posi un número entre 0 i 12 i mostrar per pantalla el mes corresponent al número indicat per l’usuari. 
El programa finalitza només quan l’usuari posa 0.
'''

mesos = ("gener","febrer","març","abril","maig","juny","juliol","agost","setembre","octubre","novembre","decembre")

x = int(input("Introdueix un numero entre 0 i 12 >>> "))

if x == 0:
    print("Bye bye")
elif 0 <= x <= 12:
    print("Mes corresponent:", mesos[x-1])
else:
    print("Només entre 0 i 12!!")