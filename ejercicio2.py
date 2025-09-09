# Función que calcula el precio final sumando el impuesto
def calcular_impuesto(valor, impuesto=19):
    return valor + (valor * impuesto / 100)

# Guardo los precios de 3 artículos en una lista
valores = []
for i in range(3):
    precio = float(input(f"Digite el valor del artículo {i+1}: "))
    valores.append(precio)

# Calculo el total aplicando la función a cada producto
total = sum(calcular_impuesto(p) for p in valores)

# Resultado final
print(f"\nEl monto final con impuestos es: {total}")
