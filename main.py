import random

def juego_adivinar_juego():
    print("Bienvenido al juego de adivinar números")
    print("Estoy pensando un número del 1 - 10")

    # Generar un número al azar
    numero_secreto =  random.randint(1,10)

    # Inicializar variables
    intentos = 0
    adivinado = False
    max_intentos = 7

    while not adivinado:
        try:
            # Pedir un númeroal jugador
            jugador_numero = int(input("Adivina el número: "))
            intentos+=1
            if intentos<=max_intentos:
                if jugador_numero < numero_secreto:
                    print("¡Demasiado bajo! Intenta con un número más alto.")
                elif jugador_numero > numero_secreto:
                    print("¡Demasiado alto! Intenta con un número más abajo")
                else:
                    print(f"Excelentente lograste adivinar el número en {intentos} intentos.")
                    adivinado = True
            else:
                print("Te exediste con el npumero de intentos. Perdiste")
                adivinado = True

        except ValueError:
            print("Por favor ingresa un número valido")

# Llamar al juego
juego_adivinar_juego()
