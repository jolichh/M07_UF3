'''
Crear una funció que rebi una frase per paràmetre. 
Aquesta frase es demana a l’usuari. 
Ha de retornar un diccionari amb les paraules que conte i la longitud de cada paraula.
'''
def diccionariParaules(frase):
    # Dividir la frase
    palabras = frase.split()
    # Crear un diccionario
    diccionario_long = {}

    # Calcular la longitud de cada palabra
    for palabra in palabras:
        longitud = len(palabra)
        # Añadir longitud
        diccionario_long[palabra] = longitud

    return diccionario_long

# Solicitar una frase al usuario
frase_usuario = input("Introdueix una frase >>> ")

# Llamar a la función y mostrar el resultado
resultado = diccionariParaules(frase_usuario)
print(resultado)
