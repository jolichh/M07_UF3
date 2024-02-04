# Joc d'endevinar numero
import random

x = random.randint(1, 100)
counter = 0
while True:
    valor = int(input("Introdueix un valor ('-1' per sortir)>>> "))
    if valor == -1:
        print("T'has rendit... La resposta era", x)
        break
    elif valor > x:
        print("És més petit que",valor)
    elif valor < x:
        print("És més gran que", valor)
    elif valor == x:
        print("Has encertat!")
        break

    counter = counter +1

print("Has utilitzat un total de:", counter, "intents")