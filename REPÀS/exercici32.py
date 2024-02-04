'''
Crear una funció que agafi una llista amb 10 números, 
i retorni una altra llista amb els seus quadrats.
'''
def calculAlCuadrat(listaNums):
    # Utilizar comprensión de listas para calcular los cuadrados
    cuadrados = [num ** 2 for num in listaNums]
    return cuadrados


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#provar
result = calculAlCuadrat(nums)
print(result)
