'''
En el següent codi es vol demanar a l’usuari un número enter i 
mostri un triangle rectangle segons el número aportat per l’usuari.
'''
n = int(input("Introdueix l’alçada del triangle (enter positiu): "))
#de 1 hasta n+1
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

# Hay que hacer recorrido de fila donde se incremente de 1 hasta n incluido haciendo saltos de 2 (impares), donde en cada fila se recorre de j=i hasta 1 con saltos de 2