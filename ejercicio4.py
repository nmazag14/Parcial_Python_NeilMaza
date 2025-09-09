# Simulación de un cajero automático
try:
    saldo = int(input("Saldo inicial: "))
    retiro = int(input("Monto a retirar: "))

    # Si el retiro es negativo, muestro error
    if retiro < 0:
        print("No se puede retirar un número negativo.")

    # Si el retiro es mayor que el saldo, muestro error
    elif retiro > saldo:
        print("Fondos insuficientes, operación cancelada.")
    else:
        # Si todo está bien, actualizo el saldo
        saldo -= retiro
        print(f"Operación realizada. Saldo actual: {saldo}")

# Si el usuario no escribe un número, capturo el error
except ValueError:
    print("Debe escribir un número válido.")
