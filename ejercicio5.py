# Lista que almacenará los productos con su precio
inventario = []

# Pido al usuario que ingrese productos hasta escribir 'fin'
while True:
    nombre = input("Producto (o 'fin' para salir): ")
    if nombre.lower() == "fin":
        break
    precio = float(input("Precio del producto: "))
    # Guardo cada producto en forma de diccionario
    inventario.append({"nombre": nombre, "precio": precio})

# Función que devuelve la cantidad total de productos
def total_items(lista):
    return len(lista)

# Calcula el precio promedio
def promedio(lista):
    return sum(p["precio"] for p in lista) / len(lista) if lista else 0

# Encuentra el producto más caro
def mas_caro(lista):
    return max(lista, key=lambda x: x["precio"])

# Encuentra el producto más barato
def mas_barato(lista):
    return min(lista, key=lambda x: x["precio"])

# Muestro un reporte con toda la información
print("\n====== REPORTE ======")
print(f"Cantidad de productos: {total_items(inventario)}")
print(f"Promedio de precios: {promedio(inventario):.2f}")

caro = mas_caro(inventario)
barato = mas_barato(inventario)

print(f"Más caro → {caro['nombre']} (${caro['precio']})")
print(f"Más barato → {barato['nombre']} (${barato['precio']})")

# Ordeno los productos de mayor a menor precio
ordenados = sorted(inventario, key=lambda x: x["precio"], reverse=True)
print("\nOrdenados por precio (descendente):")
for p in ordenados:
    print(f"{p['nombre']} - ${p['precio']}")
