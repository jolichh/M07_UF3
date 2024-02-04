import exercici28 
import exercici32
import exercici30
import exercici35

'''
ATENCION: antes de provar esta clase, es necesario comentar parte del codigo de los ficheros involucrados. De lo contrario puede entrar en bucle sin fin
'''
#ex 28
exercici28.randomNums()

#ex 30
exercici30.holaMon("Joana")

#ex 32
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = exercici32.calculAlCuadrat(nums)
print(result)

#ex 35
frase_usuario = input("Introdueix una frase >>> ")
resultado = exercici35.diccionariParaules(frase_usuario)
print(resultado)
