# Función que revisa lista de números y muestra pares o impares
def analizar_numeros(*args, **kwargs):
    if kwargs.get("mostrar_pares", False):
        # Solo los pares
        lista_pares = [n for n in args if n % 2 == 0]
        print(f"Pares encontrados: {lista_pares} → Total: {len(lista_pares)}")
    if kwargs.get("mostrar_impares", False):
        # Solo los impares
        lista_impares = [n for n in args if n % 2 != 0]
        print(f"Impares encontrados: {lista_impares} → Total: {len(lista_impares)}")

# Ejemplo lista de números
analizar_numeros(1, 2, 3, 4, 5, 6, mostrar_pares=True, mostrar_impares=True)
