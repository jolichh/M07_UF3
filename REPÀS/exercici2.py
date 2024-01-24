valor = int(input("introdueix valor en euro >>> "))
iva = int(input("introdueix IVA a aplicar (4%, 10% o 21%) >>> "))

def calcular_valor_con_porcentaje(valor, iva):
    valor_con_iva = valor + (valor * (iva / 100))
    return valor_con_iva

print(f"Valor base: {valor}")
print(f"IVA: {iva}")
print(f"Valor amb iva: {calcular_valor_con_porcentaje(valor, iva)}")