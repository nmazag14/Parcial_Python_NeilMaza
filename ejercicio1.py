# Pido un número al usuario
limite = int(input("Digite un número positivo: "))

# Recorro desde 1 hasta el número que ingresó el usuario
for i in range(1, limite + 1):
    print(f"\n--- Tabla del {i} ---")

    # Imprimo la tabla del número actual
    for j in range(1, 11):
        print(f"{i} por {j} es {i*j}")

# Al final indico cuál fue la última tabla (la más grande)
print(f"\nLa tabla más grande fue la del {limite}.")
